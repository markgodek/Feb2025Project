##TODO export Device JSON from home PC for ThingsBoard
##TODO make docker include root chain rule when container is created

# random image generation attribution
# https://stackoverflow.com/questions/15261851/100x100-image-with-random-pixel-colour

import string, numpy, random, time, os, json
import paho.mqtt.client as mqtt
from datetime import datetime
from PIL import Image

PORT = 9883
THINGSBOARD_HOST = 'localhost'
ACCESS_TOKEN = 'p5QFeCX5QoLshnYM2aL7' #device for home
ACCESS_TOKEN = 'LQFN5wQD8olOYQykhsAV' #device for laptop

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

    # simulates a numerical metric for cell culture health so ThingsBoard can alarm if it gets low
    health_metric = random.randint(0, 100)

    entry = {'Primary Key':random_string,
             'Timestamp':timestamp,
             'Cell line':cell_line,
             'Perturbation':perturbation,
             'Culture Health':health_metric,
             'Image Filename':img_out}
    print(entry)

    return entry

client = mqtt.Client()
# set access token
client.username_pw_set(ACCESS_TOKEN)

# connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(THINGSBOARD_HOST, PORT, 60)
client.loop_start()

try:
    while True:
        cell_line_count = 3 #number of cell lines to simulate
        perturbation_count = 3 #number of perturbations to simulate
        for cell_line in range(1,cell_line_count+1):
            for perturbation in range(1, perturbation_count+1):
                data = generate_data(cell_line,perturbation)
                #send data to ThingsBoard
                client.publish('v1/devices/me/telemetry', json.dumps(data),1)
                time.sleep(5)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()