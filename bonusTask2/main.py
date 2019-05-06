import numpy as np
import cv2

def main():
	#Reading in correspondance points
	w0 = readF("inputs/2D/w0.txt")
	w1 = readF("inputs/2D/w1.txt")	

	#Pretranslating so the image can be stitched at the end
	
	xtr = 500.0
	ytr = 300.0
	for i in range(len(w0)):
		w0[i][0] += xtr
		w0[i][1] += ytr
		w1[i][0] += xtr
		w1[i][1] += ytr

	#Solving for transformation matrix T
	col1 = []
	for i in range(len(w0)):
		col1.append([1])
	w0 = np.append(w0,col1, axis = 1)
	
	col0 = []
	for i in range(len(w0)):
		col0.append([0])
	w0 = np.append(w0,col0, axis = 1)
	w0 = np.append(w0,col0, axis = 1)
	w0 = np.append(w0,col0, axis = 1)
		
	l = len(w0)
	for i in range(l):
		w0 = np.append(w0,[[0,0,0, w0[i][0], w0[i][1], w0[i][2]]], axis = 0)
		
	wpr = []
	l = len(w1)
	for i in range(l):
		wpr.append([w1[i][0]])
	for i in range(l):
		wpr.append([w1[i][1]])
	
	sol = np.linalg.lstsq(w0, wpr, rcond = -1)

	T = np.array([[sol[0][0][0],sol[0][1][0], sol[0][2][0]], [sol[0][3][0],sol[0][4][0], sol[0][5][0]]])

	print("2D transformation array:\n", T)

	#Getting images
	print("---------------------------------------")
	im0 = cv2.imread('inputs/2D/w0.png')
	im1 = cv2.imread('inputs/2D/w1.png')

	rows,cols,ch = im0.shape
	r1, c1,ch1 = im1.shape

	#Moving and padding
	T2 = np.array([[1.0,0.0,xtr],[0.0,1.0,ytr]])

	tempim0 = cv2.warpAffine(im0, T2, (2000, 1000))

	#Warping
	warped0 = cv2.warpAffine(tempim0, T, (2000, 1000))


	#Stitching
	for i in range(r1):
		for j in range(c1):
			warped0[i+int(ytr)][j+int(xtr)] = im1[i][j]

	cv2.imwrite("outputs/warped0.png", warped0)

	#Reading in 3D correspondance points
	w0 = readF("inputs/3D/w0.txt")
	w1 = readF("inputs/3D/w1.txt")

	l = len(w0)

	x = np.zeros((3*l, 12))

	for i in range(l):
		temp = [w0[i][0],w0[i][1],w0[i][2],1]
		x[3*i][0] = temp[0]
		x[3*i][1] = temp[1]
		x[3*i][2] = temp[2]
		x[3*i][3] = temp[3]
		x[3*i+1][4] = temp[0]
		x[3*i+1][5] = temp[1]
		x[3*i+1][6] = temp[2]
		x[3*i+1][7] = temp[3]
		x[3*i+2][8] = temp[0]
		x[3*i+2][9] = temp[1]
		x[3*i+2][10] = temp[2]
		x[3*i+2][11] = temp[3]
	
	xpr = np.array([])

	for line in w1:
		xpr = np.append(xpr, line)
	
	a = np.linalg.lstsq(x, xpr, rcond = -1)
	a = a[0]
	
	T3D = np.array([[a[0],a[1],a[2],a[3]],[a[4],a[5],a[6],a[7]],[a[8],a[9],a[10],a[11]],[0,0,0,1]])

	print("3D transformation array:\n", T3D)
	
	print("Original ............................. vs .......................... transformation")
	for i in range(l):
		print(w1[i], ".....", T3D.dot([w0[i][0],w0[i][1],w0[i][2],1]))
	

def readF(filename):
	return np.genfromtxt(filename, delimiter='')

main()
