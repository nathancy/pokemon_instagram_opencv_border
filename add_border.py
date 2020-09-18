import numpy as np
import os
import glob
import cv2

# Put images in same directory as this script 

def add_border_to_image(filename):
    
    new_filename = filename[2:-4]
    full_filename = new_filename + '__.png'
    
    if not os.path.exists('./done/' + full_filename):
        print(full_filename)
        image = cv2.imread(filename)
        row, col = image.shape[:2]

        bordersize = 200
        result = cv2.copyMakeBorder(
            image,
            top=bordersize,
            bottom=bordersize,
            left=bordersize,
            right=bordersize,
            borderType=cv2.BORDER_CONSTANT,
            value=[255, 255, 255]
        )
        cv2.imwrite('./done/' + full_filename, result)

if not os.path.exists('./done'):
    os.makedirs('./done')

for filename in glob.glob('./*.jpg'):
    if '__' not in filename:
        add_border_to_image(filename)

