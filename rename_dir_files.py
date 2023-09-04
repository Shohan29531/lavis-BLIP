import pandas as pd
  
import sys
import glob
import pandas as pd
from natsort import natsorted
import re
import os

root_dir = "/home/touhid/Desktop/lavis"



for full_filepath in glob.iglob(root_dir + '**/*.csv', recursive=True):
        
        # tokens = full_filepath.split('/')
        # filename = tokens[ len(tokens) - 1 ]

        # new_filename = filename.replace(' - Sheet1', '')

        # new_filename = re.sub("_", "-", new_filename)

        # new_full_filepath = ''

        # for i in range( len(tokens) - 1 ):
        #         new_full_filepath += ( tokens[i] + "/")

        # new_full_filepath +=new_filename

        # os.rename(full_filepath, new_full_filepath)

        #############################

        # new_full_filepath = full_filepath.replace('hometouhidDownloadsGround_Truth_Annotation', '')

        # os.rename(full_filepath, new_full_filepath)


        print("None")
        





