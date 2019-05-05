import numpy as np
import cv2
import scipy.misc

def main():
	print("Hello World")

	w0 = cv2.imread("w0.png")
	w0 = cv2.cvtColor(w0, cv2.COLOR_BGR2RGB) 
	w1 = cv2.imread("w1.png")
	w1 = cv2.cvtColor(w1, cv2.COLOR_BGR2RGB) 

	#Getting image difference
	diff = abs(w0 - w1)	
	scipy.misc.imsave('out.png', diff)

	#Getting SIFT descriptors
	sift0 = cv2.xfeatures2d.SIFT_create()
	sift0 = sift.detect(w0,None)
	sift1 = cv2.xfeatures2d.SIFT_create()
	sift1 = sift.detect(w1,None)

main()
