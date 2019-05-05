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

Using python 3.6.7. install.sh installs the necessary libraries. Make sure you have pip3 available. Installs numpy, opencv-python, opencv-contrib-python, and scipy. Specific versions of opencv and opencv-contrib were used to run this due to them having SIFT and SURF descriptor support, which has been removed for more recent versions.

I have implemented a python script that opens the images with opencv, first calculates the RGB pixel diferences and writes the difference image to "task2/outputs/diff.png". Then, the script detects the SIFT descriptors using opencv libraries, finds a matching of the descriptors and prints the image matching to "task2/outputs/matchedImSIFT.png". Lastly, the script detects the SURF descriptors using opencv libraries, finds a matching of the descriptors and prints the image matching to "task2/outputs/matchedImSIFT.png". The matching was done using opencv's implementation of 2 nearest neighbors.

The results for the SIFT were better than for the SURF descriptor matching. However, the marching was still relatively poor due to very similar repeating features appearing in the image.

## Sources:
stackoverflow
[https"//www.pyimagesearch.com/2015/07/16/where-did-sift-and-surf-go-in-opencv-3/]
[https://docs.opencv.org/3.1.0/da/df5/tutorial_py_sift_intro.html]
[https://docs.opencv.org/3.4/dc/dc3/tutorial_py_matcher.html]


