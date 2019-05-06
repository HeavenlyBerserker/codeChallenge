import numpy as np
import cv2

def main():
	w0 = cv2.imread("inputs/w2.png")
	w0 = cv2.cvtColor(w0, cv2.COLOR_BGR2RGB) 
	w1 = cv2.imread("inputs/w3.png")
	w1 = cv2.cvtColor(w1, cv2.COLOR_BGR2RGB) 

	#Getting image difference
	diff = abs(w0 - w1)	
	cv2.imwrite('outputs/diff23.png', diff)
	print("Difference written.")
	

def printKeypoints(kps):
	for p in kps:
		printKey(p)

def printKey(keypoint):
	print("[" + str(keypoint.pt[0]) + ", " + str(keypoint.pt[1]) + ", " +str(keypoint.size) + ", " + str(keypoint.angle) + "]")

main()
