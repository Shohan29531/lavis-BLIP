import pandas as pd
  
import sys
import glob
import pandas as pd
from natsort import natsorted
import csv


GT_root_dir = "/home/touhid/Downloads/Ground_Truth_Annotation/"

GPV_root_dir = "/home/touhid/Downloads/GPV-1 Outputs/acss_videos_elena_outputs_by_group_v2/"

GPV_output_dir = GPV_root_dir + "GT_comparison/"

LAVIS_root_dir = "/home/touhid/Downloads/Lavis Outputs/acss_videos_elena_outputs_by_group/"

LAVIS_output_dir = LAVIS_root_dir + "GT_comparison/"

csv_filenames = []
csv_filenames_full_path = []
for filename in glob.iglob(GT_root_dir + '**/*.csv', recursive=True):
        csv_filenames_full_path.append( filename )
        tokens = filename.split('/')
        file = tokens[ len(tokens) - 1 ]
        csv_filenames.append( file )

# print(csv_filenames)

with open("metrics.csv", "a") as csv_file:
    csvwriter = csv.writer( csv_file, delimiter=',')
    csvwriter.writerow( [ 'File Name', 'Precision-GPV', 'Precision-LAVIS',
                         'Recall-GPV', 'Recall-LAVIS', 'F1-GPV', 'F1-LAVIS',
                         'Accuracy-GPV', 'Accuracy-LAVIS'] )

for i in range( len(csv_filenames) ):
        
        GT_file = csv_filenames_full_path[i]

        GPV_file = GPV_root_dir + csv_filenames[i]

        LAVIS_file = LAVIS_root_dir + csv_filenames[i]

        GT_df = pd.read_csv(GT_file)
        GPV_df = pd.read_csv(GPV_file)
        LAVIS_df = pd.read_csv(LAVIS_file)

        GPV_output_df = GPV_df
        LAVIS_output_df = LAVIS_df

        TP_GPV = 0
        TP_LAVIS = 0

        TN_GPV = 0
        TN_LAVIS = 0

        FP_GPV = 0
        FP_LAVIS = 0

        FN_GPV = 0
        FN_LAVIS = 0

        for row in range(0, 79):
                for col in range(1, len(GT_df.columns)):
                        
                        GPV_flag = False
                        LAVIS_flag = False
                        
                        ##TP test

                        if str(GT_df.iloc[row, col]) == "1" and str(GPV_df.iloc[row, col]) == "1":
                                GPV_output_df.iloc[row, col] = 'TP'
                                GPV_flag = True
                                TP_GPV +=1
                        if str(GT_df.iloc[row, col]) == "1" and str(LAVIS_df.iloc[row, col]) == "1":
                                LAVIS_output_df.iloc[row, col] = 'TP'
                                LAVIS_flag = True   
                                TP_LAVIS += 1   

                        ##TN Test

                        if str(GT_df.iloc[row, col]) == "0" and str(GPV_df.iloc[row, col]) == "0":
                                GPV_output_df.iloc[row, col] = 'TN'
                                GPV_flag = True
                                TN_GPV += 1
                        if str(GT_df.iloc[row, col]) == "0" and str(LAVIS_df.iloc[row, col]) == "0":
                                LAVIS_output_df.iloc[row, col] = 'TN'   
                                LAVIS_flag = True
                                TN_LAVIS += 1   

                        ##FP Test
                        if str(GT_df.iloc[row, col]) == "0" and str(GPV_df.iloc[row, col]) == "1":
                                GPV_output_df.iloc[row, col] = 'FP'
                                GPV_flag = True
                                FP_GPV += 1
                        if str(GT_df.iloc[row, col]) == "0" and str(LAVIS_df.iloc[row, col]) == "1":
                                LAVIS_output_df.iloc[row, col] = 'FP'
                                LAVIS_flag = True
                                FP_LAVIS += 1 

                        ##FN Test

                        if str(GT_df.iloc[row, col]) == "1" and str(GPV_df.iloc[row, col]) == "0":
                                GPV_output_df.iloc[row, col] = 'FN'
                                GPV_flag = True
                                FN_GPV += 1
                        if str(GT_df.iloc[row, col]) == "1" and str(LAVIS_df.iloc[row, col]) == "0":
                                LAVIS_output_df.iloc[row, col] = 'FN' 
                                LAVIS_flag = True 
                                FN_LAVIS += 1

                        if GPV_flag == False:
                                if str(GT_df.iloc[row, col]) == "-1" and str(GPV_df.iloc[row, col]) == "1":
                                    GPV_output_df.iloc[row, col] = 'TP'
                                    TP_GPV +=1
                                if str(GT_df.iloc[row, col]) == "-1" and str(GPV_df.iloc[row, col]) == "0":
                                    GPV_output_df.iloc[row, col] = 'FN'  
                                    FN_GPV += 1                                  

                        if LAVIS_flag == False:
                                if str(GT_df.iloc[row, col]) == "-1" and str(LAVIS_df.iloc[row, col]) == "1":
                                    GPV_output_df.iloc[row, col] = 'TP'
                                    TP_LAVIS += 1
                                if str(GT_df.iloc[row, col]) == "-1" and str(LAVIS_df.iloc[row, col]) == "0":
                                    GPV_output_df.iloc[row, col] = 'FN' 
                                    TN_LAVIS += 1            
          

        LAVIS_output_df.to_csv( LAVIS_output_dir + csv_filenames[i], sep =',', index = False ) 
        GPV_output_df.to_csv( GPV_output_dir + csv_filenames[i], sep =',', index = False ) 

        precision_GPV = ( TP_GPV ) / ( TP_GPV + FP_GPV )
        precision_LAVIS = ( TP_LAVIS ) / ( TP_LAVIS + FP_LAVIS )

        recall_GPV = ( TP_GPV ) / ( TP_GPV + FN_GPV )
        recall_LAVIS = ( TP_LAVIS ) / ( TP_LAVIS + FN_LAVIS )

        F1_GPV = ( 2 * TP_GPV ) / ( 2 * TP_GPV + FP_GPV + FN_GPV )
        F1_LAVIS = ( 2 * TP_LAVIS ) / ( 2 * TP_LAVIS + FP_LAVIS + FN_LAVIS )

        accuracy_GPV = ( TP_GPV + TN_GPV ) / ( TP_GPV + TN_GPV + FP_GPV + FN_GPV)
        accuracy_LAVIS = ( TP_LAVIS + TN_LAVIS ) / ( TP_LAVIS + TN_LAVIS + FP_LAVIS + FN_LAVIS )

        with open("metrics.csv", "a") as csv_file:
            csvwriter = csv.writer( csv_file, delimiter=',')
            csvwriter.writerow( [ csv_filenames[i], precision_GPV, precision_LAVIS,
                         recall_GPV, recall_LAVIS, F1_GPV, F1_LAVIS,
                         accuracy_GPV, accuracy_LAVIS] )


