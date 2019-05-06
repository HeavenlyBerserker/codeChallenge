# codeChallenge

This github repository contains my work for the code challenge. Shout out to Shireen Elhabian.

## Required Task 1

This is the github repository created.

## Required Task 2

I have implemented my CircularArray class in C++ contained in the files "/task2/CircularArray.cpp" and "/task2/CircularArray.h". One can run all through the shell file "/task2/run.sh", which compiles the code into an executable "circular", and then runs circular. 

### Double Linked List Implementation

I have decided to create a double linked list, a data structure that can be rotated very efficiently due to the way it is stored in memory. The following operations/methods were implemented:

* void append(int num): constant time, appends number num to list
* void append(vector <int> v): linear time in the size of the vector, appends every number in vector v.
* node* getith(int i): at most n/2 time per operation. Returns the ith node of the linked list. It works with backwards indexing and >size indexing.
* void rotate(int steps): linear in number of steps, at most n/2. Uses getith(steps) and sets the returned node to be the new head.
* bool delith(int i): at most n/2 time. Uses getith to get the node, then disconnects and deletes it.

## Required Task 3

Note: I thought we had to find the differences between the 2D_registration images, so in addition to doing differences, I tried to do SIFT and SURF descriptor matching. I included the results to both pairs of images. See outputs "task3/outputs" directory to see what I mean. Run "task3/task3-simple.py" to do the basics. If you want to see the SIFT and SURF matching tasks, run "task3/task3.py".

Using python 3.6.7. install.sh installs the necessary libraries. Make sure you have pip3 available. Installs numpy, opencv-python, and opencv-contrib-python. Specific versions of opencv and opencv-contrib were used to run this due to them having SIFT and SURF descriptor support, which has been removed for more recent versions.

I have implemented a python script that opens the images with opencv, first calculates the RGB pixel diferences and writes the difference image to "task2/outputs/diff.png". Then, the script detects the SIFT descriptors using opencv libraries, finds a matching of the descriptors and prints the image matching to "task2/outputs/matchedImSIFT.png". Lastly, the script detects the SURF descriptors using opencv libraries, finds a matching of the descriptors and prints the image matching to "task2/outputs/matchedImSIFT.png". The matching was done using opencv's implementation of 2 nearest neighbors.

The results for the SIFT were better than for the SURF descriptor matching. However, the marching was still relatively poor due to very similar repeating features appearing in the image.

## Bonus Task 1

The code is in "bonusTask1/main.py". Can pass an argument file name where input is stored. First line input contains projects, second line dependencies. "bonusTask1/run.sh" runs both default inputs in the directory.

I implemented the algorithm to repeat the following procedure:

* while (still unsafisfied dependencies)
	* for dependency d
		* if(d is not satisfied) swap the elements
	* if(no changes have been made) exit, no solution
* return solution

## Bonus Task 2

Make sure opencv is installed. python3 main.py to run the program.

The program computes the translation matrix for a bunch of 2D and 3D coordinates. I had some trouble warping images without them going out of bounds. I am certain that my 2D and 3D work perfectly, however, due to my moving the images to avoid warping images out of bounds, I lost a bit of precision since I solved after translation. I assumed we were not allowed to use the built in opencv translation matrix solver, so I wrote the code, but I used the numpy linear system of equation solver. The original and transformed values are not perfect, but are very close. The 2D values suffered a lot due to pre-translation, but if you are happy with an incomplete image, it still stitches perfectly.

The output image is in the output folder. 

## Bonus Task 3

The link to the linux Qt 4.8 source was broken. Was able to find it at [https://download.qt.io/archive/qt/4.8/4.8.7/]. Was able to build SCIRun, but added it to .gitignore because it was too heavy. Was not able to use the shell script to build, but was able to use the "cd bin" and "cmake ../Superbuild" commands.

## Sources:
* [https://stackoverflow.com]
* [https://www.codementor.io/codementorteam/a-comprehensive-guide-to-implementation-of-singly-linked-list-using-c_plus_plus-ondlm5azr]
* [https://www.pyimagesearch.com/2015/07/16/where-did-sift-and-surf-go-in-opencv-3/]
* [https://docs.opencv.org/3.1.0/da/df5/tutorial_py_sift_intro.html]
* [https://docs.opencv.org/3.4/dc/dc3/tutorial_py_matcher.html]


