import numpy as np
import cv2

def main():
	w0 = cv2.imread("inputs/w0.png")
	w0 = cv2.cvtColor(w0, cv2.COLOR_BGR2RGB) 
	w1 = cv2.imread("inputs/w1.png")
	w1 = cv2.cvtColor(w1, cv2.COLOR_BGR2RGB) 

	#Getting image difference
	diff = abs(w0 - w1)	
	cv2.imwrite('outputs/diff.png', diff)
	print("Difference written.")
	
	#Getting SIFT descriptors for both images
	detector = cv2.xfeatures2d.SIFT_create()
	kps0, des0 = detector.detectAndCompute(w0,None)
	kps1, des1 = detector.detectAndCompute(w1,None)

	#Write SIFT images
	w0_s = w0
	w1_s = w1
	cv2.drawKeypoints(w0, kps0, w0_s)
	cv2.drawKeypoints(w1, kps1, w1_s)
	
	cv2.imwrite('outputs/w0_sift.png', w0_s)
	cv2.imwrite('outputs/w1_sift.png', w1_s)

	#Matching SIFT
	matcher = cv2.BFMatcher()
	
	matches = matcher.knnMatch(des0,des1,k=2)

	good = []
	for m,n in matches:
		if(m.distance < 0.5*n.distance):
			good.append([m])
	
	matchedIm = cv2.drawMatchesKnn(w0,kps0,w1,kps1,good,None,flags = cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

	cv2.imwrite("outputs/matchedImSIFT.png", matchedIm)
	print("SIFT matching written.")

	#Getting SURF descriptors for both images
	detector = cv2.xfeatures2d.SURF_create()
	kps0, des0 = detector.detectAndCompute(w0,None)
	kps1, des1 = detector.detectAndCompute(w1,None)

	#Write SURF images
	w0_s = w0
	w1_s = w1
	cv2.drawKeypoints(w0, kps0, w0_s)
	cv2.drawKeypoints(w1, kps1, w1_s)
	
	cv2.imwrite('outputs/w0_surf.png', w0_s)
	cv2.imwrite('outputs/w1_surf.png', w1_s)

	#Matching SURF
	matcher = cv2.BFMatcher()
	
	matches = matcher.knnMatch(des0,des1,k=2)

	good = []
	for m,n in matches:
		if(m.distance < 0.6*n.distance):
			good.append([m])
	
	matchedIm = cv2.drawMatchesKnn(w0,kps0,w1,kps1,good,None,flags = cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

	cv2.imwrite("outputs/matchedImSURF.png", matchedIm)
	print("SURF matching written.")
	

def printKeypoints(kps):
	for p in kps:
		printKey(p)

def printKey(keypoint):
	print("[" + str(keypoint.pt[0]) + ", " + str(keypoint.pt[1]) + ", " +str(keypoint.size) + ", " + str(keypoint.angle) + "]")

main()
