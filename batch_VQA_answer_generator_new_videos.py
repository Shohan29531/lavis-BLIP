from lavis.models import model_zoo
import torch
from PIL import Image
import glob
from lavis.models import load_model_and_preprocess

import time
import math
import sys
import csv


from a11y_utils import utility



if __name__=="__main__":

    start_time = time.time()

    ## Load all input files

    root_dir = '/home/touhid/Downloads/new_videos/'

    input_names = []
    input_names_full_path = []
    for filename in glob.iglob(root_dir + '**/*.jpeg', recursive=True):
        input_names_full_path.append( filename )
        tokens = filename.split('/')
        file = tokens[ len(tokens) - 1 ]
        input_names.append( file ) 

    my_output_dir = "/home/touhid/Downloads/new_video_outputs_lavis/"

    #######################################################################

    ## Model load

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model, vis_processors, txt_processors = load_model_and_preprocess(name="blip_vqa", model_type="vqav2", is_eval=True, device=device)

    print(len(input_names))

    #######################################################################

    # Loop to process all frames

    for item in range( len(input_names) ):
        

        print( "Currently Processing " + str( item + 1 ) )  
        input_file = input_names[ item ]

        a11y_questions = utility.get_a11y_questions( 'a11y_questions_of_interest.txt' )

        a11y_objects = utility.get_a11y_objects( 'a11y_objects_of_interest.txt' )

        with open( my_output_dir + input_file.split('.')[0] + ".csv", "a") as csv_file:
            csvwriter = csv.writer( csv_file, delimiter=',')
            csvwriter.writerow( [ 'Object', 'LAVIS Prediction', 'Ground Truth'] )

        ## Load input   

        raw_image = Image.open( input_names_full_path[item] ).convert("RGB")
        image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)

        ## Ask 90 questions
        i = 0
        for a11y_question in a11y_questions:
            
            question = txt_processors["eval"](a11y_question)

            answer = model.predict_answers(samples={"image": image, "text_input": question}, inference_method="generate")[0]


            flag = answer
            if answer == 'yes' or answer == 'Yes':
                flag = "1"
            elif answer == 'no' or answer == 'No':
                flag = "0"    

            
            object = a11y_objects[i]

            with open(my_output_dir + input_file.split('.')[0] + ".csv", "a") as csv_file:
                csvwriter = csv.writer( csv_file, delimiter=',')
                csvwriter.writerow( [ object, flag, '0'] )

            i += 1


        print( time.time() - start_time, end = "")
        print( " seconds" ) 
