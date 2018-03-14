# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 13:26:15 2018

@author: sathy
"""

import cv2

camera_type = 'local'

def get_image():
    ret, image = cap.read()
    return image
cap = cv2.VideoCapture(0)

ref_img = get_image()
result = ref_img 		
#--------------Controls---------------------
print ("Controls:")
print ("K = Cropping (Draw box with mouse first, then press K)")
print ("S = save image to Image.jpg")
print ("Q = quit")

use_cropping = False

#---------------Cropping---------------------
refPt = []
setting_cropping = False
def click_and_crop(event, x, y, flags, param):
	global refPt, cropping
	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping specification is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		setting_cropping = True
	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		refPt.append((x, y))
		setting_cropping = False

		# draw a rectangle around the region of interest
		cv2.rectangle(result, refPt[0], refPt[1], (0, 255, 0), 2)
		cv2.imshow("frame", result)
cv2.namedWindow("frame")
cv2.setMouseCallback("frame", click_and_crop)  # register mouse events

while(True):  
	img = get_image()
	if (use_cropping) and (len(refPt)==2):
		cropped_img = img[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]	
		img = cropped_img	
	result = img # Display the resulting frame
	# if there's a cropping rectangle drawn, keep showing the rectangle
	if ((2==len(refPt)) and (not use_cropping)):
		cv2.rectangle(result, refPt[0], refPt[1], (0, 255, 0), 2)
	cv2.imshow("frame",result)   # show the image on the screen

	#---------------Keyboard controls--------------------
	key = cv2.waitKey(1) & 0xFF
    #----------------- quit--------------------------
	if key == ord('q'):   
		break
    #---------------- save image---------------------
	elif key == ord('s'):  
		cv2.imwrite( ".jpg", result );
    #---------------------cropping-------------------     
	elif (key == ord('k')) and (2==len(refPt)):  
		use_cropping = not use_cropping

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
