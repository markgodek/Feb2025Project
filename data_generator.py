# random image generation attribution
# https://stackoverflow.com/questions/15261851/100x100-image-with-random-pixel-colour

import string, numpy, random, time, os
from datetime import datetime
from PIL import Image

# a method which given numbers for a cell line and perturbation, returns a database entry
def generate_data(cell_line, perturbation):

    random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    timestamp = datetime.now().strftime("%m-%d-%Y,%H:%M:%S")

    wd = os.getcwd()
    img_dir = wd + r'\images'
    os.makedirs(img_dir, exist_ok=True)  # Create the directory if it doesn't exist

    imarray = numpy.random.rand(100,100,3) * 255
    im = Image.fromarray(imarray.astype('uint8')).convert('RGBA')
    img_out = img_dir + '\\' + random_string + '.png'
    im.save(img_out)

    entry = {'Primary Key':random_string,
             'Timestamp':timestamp,
             'Cell line':cell_line,
             'Perturbation':perturbation,
             'Image Filename':img_out}
    print(entry)

    return entry

while True:
    cell_line_count = 3 #number of cell lines to simulate
    perturbation_count = 3 #number of perturbations to simulate
    for cell_line in range(1,cell_line_count+1):
        for perturbation in range(1, perturbation_count+1):
            generate_data(cell_line,perturbation)
            time.sleep(15)
