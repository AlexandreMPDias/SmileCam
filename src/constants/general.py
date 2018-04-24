import os

"""
A Directory that has read rights but no write rights.
"""
READ_PATH = 'data/'

"""
A Directory that has both read and write rights.
"""
WRITE_PATH = os.getenv('APPDATA') + '/Cyberlabs/SmileCam/'


###### PATH TO READ ONLY DIRS

HAARCASCADE = READ_PATH + 'haarcascade_frontalface_default.xml'
EPOCH = READ_PATH + 'checkpoints/epoch_75.hdf5'
PNG_PATH = READ_PATH + 'png/'

###### PATH TO WRITABLE DIRS

"""
Directory that stores the png pictures
"""
FACE_IMAGES = WRITE_PATH + 'face_images/'


###### Constants

"""
Message that will be displayed on the console when a Smile is detected.
"""
HAPPY_MESSAGE = 'Happy Face!!!'

ALPHA = 0.5