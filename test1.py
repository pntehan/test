import cv2 as cv
import os
import time

ascii_char = list(r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
char_len = len(ascii_char)
cap = cv.VideoCapture('F:/HYLiteResources/video/15215499037e9664374419bc63.mp4_last.mp4')

while True:
	hasFrame, frame = cap.read()
	if not hasFrame:
		break
	width = frame.shape[0]
	height = frame.shape[1]
	img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	img_resize = cv.resize(img_gray, (int(width/10), int(height/10)))
	text = ''
	for row in img_resize:
		for pixel in row:
			text += ascii_char[int(pixel/256*char_len)]
		text += '\n'
	os.system('cls')
	print(text)
	#time.sleep(0.1)	


