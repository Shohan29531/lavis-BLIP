import numpy as np
import PIL
from PIL import Image
import glob
from natsort import natsorted

root_dir = "/home/touhid/Downloads/accss_videos_elena/video_003/trimmed_video/keyframes_video_accss_003_elena_seg06.mp4/"








image_paths = []
for filename in glob.iglob(root_dir + '**/*.jpeg', recursive=True):
        image_paths.append( filename )


image_paths = natsorted( image_paths )

print(image_paths)

imgs    = [ Image.open(i) for i in image_paths ]

picked_images = [ ]

for i in range( len(imgs) ):
    if i%3==0:
        picked_images.append( imgs[i] )
                
        


# pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
min_shape = sorted( [(np.sum(i.size), i.size ) for i in picked_images])[0][1]
imgs_comb = np.hstack([i.resize(min_shape) for i in picked_images])

# save that beautiful picture
imgs_comb = Image.fromarray( imgs_comb)
imgs_comb.save( '3-6-frames-horizontal.pdf' )    

# for a vertical stacking it is simple: use vstack
imgs_comb = np.vstack([i.resize(min_shape) for i in picked_images])
imgs_comb = Image.fromarray( imgs_comb)
imgs_comb.save( '3-6-frames-vertical.pdf' )