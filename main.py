# USAGE
# python emotion_detector.py --cascade HAARCASCADE_frontalface_default.xml --model checkpoints/EPOCH_75.hdf5

#for pyinstaller:
from scipy import optimize

import modules.popup as popup
from modules.debug import Log
from modules.debug import IntegrityTest

log = Log()
check = IntegrityTest()
import warnings
log.info('Supressing Imports\' Warnings')
warnings.simplefilter(action='ignore', category=FutureWarning)
# import the necessary packages
log.info('Importing Keras')
from keras.preprocessing.image import img_to_array
log.sucess('Keras imported')

from keras.models import load_model
from imutils import build_montages
import numpy as np
import argparse
import imutils
from imutils.video import VideoStream
import cv2
import httplib2
import time
from imutils import paths
import random
import datetime
import operator
warnings.resetwarnings()
import os
from constants.general import HAARCASCADE, EPOCH, PNG_PATH, FACE_IMAGES, HAPPY_MESSAGE, ALPHA

def watermark(image,mark_path,position="center",alpha=ALPHA):
	watermark = mark_path
	(wH, wW) = watermark.shape[:2]
	(B, G, R, A) = cv2.split(watermark)
	B = cv2.bitwise_and(B, B, mask=A)
	G = cv2.bitwise_and(G, G, mask=A)
	R = cv2.bitwise_and(R, R, mask=A)
	watermark = cv2.merge([B, G, R, A])
	(h, w) = image.shape[:2]
	image = np.dstack([image, np.ones((h, w), dtype="uint8") * 255])
 
	# construct an overlay that is the same size as the input
	# image, (using an extra dimension for the alpha transparency),
	# then add the watermark to the overlay in the bottom-right
	# corner
	overlay = np.zeros((h, w, 4), dtype="uint8")

	if position =="right_low" :
		overlay[h - wH - 10:h - 10, w - wW - 10:w - 10] = watermark
	if position == "center" :
		overlay[int(h/2) - int(wH/2) :int(h/2)+int(wH/2) , int(w/2) - int(wW/2) :int(w/2)+int(wW/2)] = watermark

 
	# blend the two images together using transparent overlays
	output = image.copy()
	cv2.addWeighted(overlay, alpha, output, 1.0, 0, output)
 
	# write the output image to disk
	return output

def build_montage():
	imagePaths = list(paths.list_images(FACE_IMAGES))
	# ATTENTION CHANGE HERE CYBER :) intead of shuffle order more recents
	random.shuffle(imagePaths)
	imagePaths = imagePaths[:70]

	# initialize the list of images
	images = []
	 
	# loop over the list of image paths
	for imagePath in imagePaths:
		# load the image and update the list of images
		image = cv2.imread(imagePath)
		images.append(image)
	 
	# construct the montages for the images
	montages = build_montages(images, (250, 250), (10, 5))
	# loop over the montages and display each of them
	return montages[0]

def main():
	log.info('Checking Camera Conected')
	#camera = VideoStream(src="rtsp://admin:h123@192.168.0.11/cam/realmonitor?channel=4&subtype=0", usePiCamera=False).start()
	log.info('Starting VideoStream')
	camera = VideoStream(src=0, usePiCamera=False).start()
	log.sucess('Video Stream started')

	# load the face detector cascade, emotion detection CNN, then define
	# the list of emotion labels
	log.info('Loading Face Detector Cascade')
	detector = cv2.CascadeClassifier(HAARCASCADE)
	log.sucess('Face Detector Cascade Loaded').info('Loading Model')
	model = load_model(EPOCH)
	log.sucess('Model Loaded')
	EMOTIONS = ["angry", "scared", "happy", "sad", "surprised","neutral"]
	error_detected = ""
	#camera = VideoStream(src="rtsp://admin:admin@cyberlabsrio.ddns.net/cam/realmonitor?channel=4&subtype=0", usePiCamera=False).start()

	# # if a video path was not supplied, grab the reference to the webcam
	# if not args.get("video", False):
	# 	camera = cv2.VideoCapture(0)

	# # otherwise, load the video
	# else:
	# 	camera = cv2.VideoCapture(args["video"])

	# keep looping
	cv2.namedWindow('Montage')
	cv2.setWindowProperty('Montage', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
	canvas = np.zeros((220, 300, 3), dtype="uint8")
	start_time = time.time()
	log.info('Building Montage')
	montage = build_montage()
	log.sucess('Montage Built')
	montage_copy = montage.copy()
	emotionPath = "{}/{}.png".format(PNG_PATH, "sunglass")
	popup.PopUp('Smile Cam', 'Press [q] to close the application.')
	while True:
		# grab the current frame
		# (grabbed, frame) = camera.read()
		frame = camera.read()
		# if we are viewing a video and we did not grab a
		# frame, then we have reached the end of the video
		#if args.get("video") and not grabbed:
		#	break

		# resize the frame and convert it to grayscale
		# frame = imutils.resize(frame, width=300)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# initialize the canvas for the visualization, then clone
		# the frame so we can draw on it
		frameClone = frame.copy()

		# detect faces in the input frame, then clone the frame so that
		# we can draw on it
		rects = detector.detectMultiScale(gray, scaleFactor=1.3, 
			minNeighbors=5, minSize=(30, 30),
			flags=cv2.CASCADE_SCALE_IMAGE)

		# ensure at least one face was found before continuing
		if len(rects) > 0:
			canvas = np.zeros((220, 300, 3), dtype="uint8")
			
			# determine the largest face area
			rect = sorted(rects, reverse=True,
				key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
			(fX, fY, fW, fH) = rect
		
			# extract the face ROI from the image, then pre-process
			# it for the network
			
			roi = gray[fY:fY + fH, fX:fX + fW]
			roi = cv2.resize(roi, (48, 48))
			roi = roi.astype("float") / 255.0
			roi = img_to_array(roi)
			roi = np.expand_dims(roi, axis=0)
			xfY = fY - 50
			xfH = fH + 150 
			xfX = fX - 50 
			xfW = fW + 150 
			if xfY + xfH > frame.shape[0] : 
				Ybotton = frame.shape[0]-10
			else :
				Ybotton =xfY + xfH 
			if xfX + xfW > frame.shape[1] :
				Xmax = frame.shape[1] -10 
			else :
				Xmax = xfX + xfW
			if xfY < 0 : 
				xfY = 0
			if xfX < 0 :
				xfX = 0 
			
			# make a prediction on the ROI, then lookup the class
			# label
			preds = model.predict(roi)[0]
			label = EMOTIONS[preds.argmax()]
			elapse = (time.time() - start_time)
			

			# loop over the labels + probabilities and draw them
			enum = enumerate(zip(EMOTIONS, preds))
			
			for (i, (emotion, prob)) in enum:
				if emotion == "happy":
					if  elapse > 5 and prob*100> 97:
						face_frame = frame[xfY:Ybotton, xfX:Xmax]
						# cv2.imshow(str(start_time),face_frame) 
						outputPath = "{}/{}.jpg".format(FACE_IMAGES, start_time)
						cv2.imwrite(outputPath, face_frame)
						print(HAPPY_MESSAGE)
						start_time = time.time()
						montage = build_montage()
						montage_copy = montage.copy()
					# construct the label text
				if prob *100 < 90 :
					color = (0, 0, 255)
				else :
					color = (0, 255, 0)

				if prob*100 > 51:
					emotionPath = "{}/{}.png".format(PNG_PATH, emotion)
					alpha = prob
				

				# construct the label text
				text = "{}: {:.2f}%".format(emotion, prob * 100)
				
				# draw the label + probability bar on the canvas
				w = int(prob * 300)
				cv2.rectangle(canvas, (5, (i * 35) + 5),
					(w, (i * 35) + 35), color, -1)
				cv2.putText(canvas, text, (10, (i * 35) + 23),
					cv2.FONT_HERSHEY_SIMPLEX, 0.45,
					(255, 255, 255), 2)
				cv2.rectangle(montage, (0, (i * 35) + 5),
					(w, (i * 35) + 35), color, 3)
				cv2.putText(montage, text, (10, (i * 35) + 23),
					cv2.FONT_HERSHEY_SIMPLEX, 0.45,
					(255, 255, 255), 2)

			# # draw the label on the frame
			# cv2.putText(frameClone, label, (fX, fY - 10),
			# 	cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
			# cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH),
			# 	(0, 0, 255), 2)

		# show our classifications + probabilities
		# cv2.imshow("Face", imutils.resize(frameClone, width=1200))
		# cv2.imshow("Probabilities", canvas)
		frame_montage =  watermark(montage,cv2.imread(emotionPath, cv2.IMREAD_UNCHANGED),alpha=0.9)

		cv2.imshow("Montage",frame_montage)
		montage = montage_copy.copy()
		# if the 'q' key is pressed, stop the loop
		if cv2.waitKey(1) & 0xFF == ord("q"):
			break

	# cleanup the camera and close any open windows

	camera.stop()
	cv2.destroyAllWindows()

if __name__ == "__main__":
	haar_found = check.canLocateFile(HAARCASCADE)
	epoch_found = check.canLocateFile(EPOCH)
	outputFound = check.canLocateDir(FACE_IMAGES, True)
	camera = check.isCameraConected(True)
	if(haar_found and epoch_found and outputFound and camera):
		main()
	else:
		os.system('pause')