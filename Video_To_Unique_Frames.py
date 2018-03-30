#Author : Aditi Shah
#March 30, 2018
import sys
import os
import cv2
import numpy as np
import math
def mse(imageA, imageB):
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar" the two images are
	return err
def video_to_frames(input_loc,output_loc):
    try:
        os.mkdir(output_loc)
    except OSError:
        pass
    # Start capturing the feed
    cap = cv2.VideoCapture(input_loc)
    frameRate = cap.get(5) #frame rate
    prev=None
    count=0
    while cap.isOpened():
      count+=1
      frameId = cap.get(1) #current frame number
      ret, frame = cap.read()
      if (ret != True):
          break
      if (frameId % math.floor(frameRate) == 0):
        if prev is None:
          prev=frame
        imageA=prev
        imageB=frame
        prev=frame
        c=mse(imageA, imageB)
        if c>1:
          cv2.imwrite(output_loc + "/%#05d.jpg" % (count+1), frame)
    cap.release()
video_to_frames(sys.argv[1],sys.argv[2])