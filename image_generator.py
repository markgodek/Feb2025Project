# random image generation attribution
# https://stackoverflow.com/questions/15261851/100x100-image-with-random-pixel-colour

import numpy, random, os
from PIL import Image

def generate_image(img_name):

    wd = os.getcwd()
    img_dir = wd + r'\images'
    os.makedirs(img_dir, exist_ok=True)  # Create the directory if it doesn't exist

    imarray = numpy.random.rand(100,100,3) * 255
    im = Image.fromarray(imarray.astype('uint8')).convert('RGBA')
    im.save(img_dir + '\\' + img_name + '.png')
    #print('wrote file here:', img_dir + '\\' + img_name + '.png')