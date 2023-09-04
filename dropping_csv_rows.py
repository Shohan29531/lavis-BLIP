import pandas as pd
  
import sys
import glob
import pandas as pd
from natsort import natsorted


# root_dir = "/home/touhid/Downloads/Lavis Outputs/acss_videos_elena_outputs_by_group/"
root_dir = "/home/touhid/Downloads/Ground_Truth_Annotation/"

# root_dir = "/home/touhid/Downloads/new_video_outputs_LAVIS_by_group/"
# root_dir = "/home/touhid/Downloads/new_video_outputs_GPV_by_group/"




csv_filenames = []
csv_filenames_full_path = []
for filename in glob.iglob(root_dir + '**/*.csv', recursive=True):
        csv_filenames_full_path.append( filename )
        tokens = filename.split('/')
        file = tokens[ len(tokens) - 1 ]
        csv_filenames.append( file )



# to_be_deleted = ["Brick", "Cloudy", "Day", "Jaywalker", "Night", "Obstacle on the sidewalk",
#                  "Obstacle on the street", "Raining", "Stone Block", "Sunny", "Zebra Crossing"]

for csv_filename in csv_filenames_full_path:

    df_s1 = pd.read_csv(csv_filename)
  
    df_s1 = df_s1.drop(df_s1[
          (df_s1.Object == "Brick") | (df_s1.Object == "brick") |
          (df_s1.Object == "Cloudy") | (df_s1.Object == "cloudy") |
          (df_s1.Object == "Day") | (df_s1.Object == "day") |
          (df_s1.Object == "Jaywalker") | (df_s1.Object == "jaywalker") |
          (df_s1.Object == "Night") | (df_s1.Object == "night") |
          (df_s1.Object == "Obstacle on the sidewalk") | (df_s1.Object == "obstacle on the sidewalk") |
          (df_s1.Object == "Obstacle on the street") | (df_s1.Object == "obstacle on the street") |
          (df_s1.Object == "Raining") | (df_s1.Object == "raining") | 
          (df_s1.Object == "Stone Block") | (df_s1.Object == "stone block") |
          (df_s1.Object == "Sunny") | (df_s1.Object == "sunny") |
          (df_s1.Object == "Zebra Crossing") | (df_s1.Object == "zebra crossing")                         
                             ].index)

    df_s1.to_csv( csv_filename, sep =',', index = False )  