# codeChallenge

This github repository contains my work for the code challenge. Shout out to Shireen Elhabian.

## Required Task 1

This is the github repository created.

## Required Task 2

I have implemented my CircularArray class in C++ contained in the files "/task2/CircularArray.cpp" and "/task2/CircularArray.h". One can run all through the shell file "/task2/run.sh", which compiles the code into an executable "circular", and then runs circular. 

### Double Linked List Implementation

I have decided to create a double linked list, a data structure that can be rotated very efficiently due to the way it is stored in memory. The following operations/methods were implemented:

*void append(int num): constant time, appends number num to list
*void append(vector <int> v): linear time in the size of the vector, appends every number in vector v.
*node* getith(int i): <n/2 time per operation. Returns the ith node of the linked list. It works with backwards indexing and >size indexing.
*void rotate(int steps): linear in number of steps, <n/2. Uses getith(steps) and sets the returned node to be the new head.
*bool delith(int i): <n/2 time. Uses getith to get the node, then disconnects and deletes it.


