import pandas as pd
  
import sys
import glob
import pandas as pd
from natsort import natsorted



# root_dir = "/home/touhid/Downloads/Lavis Outputs/acss_videos_elena_outputs_by_group/"
root_dir = "/home/touhid/Downloads/GPV-1 Outputs/acss_videos_elena_outputs_by_group_v2/GT_comparison/"

# root_dir = "/home/touhid/Downloads/new_video_outputs_LAVIS_by_group/"
# root_dir = "/home/touhid/Downloads/new_video_outputs_GPV_by_group/"


# /home/touhid/Downloads/GPV-1 Outputs/acss_videos_elena_outputs_by_group_v2/GT_comparison
# /home/touhid/Downloads/Lavis Outputs/acss_videos_elena_outputs_by_group/GT_comparison




csv_filenames = []
csv_filenames_full_path = []
for filename in glob.iglob(root_dir + '**/*.csv', recursive=True):
        csv_filenames_full_path.append( filename )
        tokens = filename.split('/')
        file = tokens[ len(tokens) - 1 ]
        csv_filenames.append( file )


for csv_filename in csv_filenames:
                
    for row in range(0, 79):
        for col in range(1, len(GT_df.columns)):