#include <vector>

using namespace std;

struct node{
	int data;
	node *next;
	node *last;
};

class CircularArray{
	private:
	//Deletes the node passed to it. Private because we don't trust user with passing pointers.
	void del(node * n);
	
	public:
	//Head and size would be safer if private, but this simplifies implementation
	node *head;
	int size;
	
	//Constructor
	CircularArray();
	//Appends = prepends a number to the list
	void append(int num);
	//Appends a collection of numbers to the list
	void append(vector <int> v);
	//Gets the ith node
	node* getith(int i);
	//Rotates steps steps
	void rotate(int steps);
	//Deletes ith element.
	bool delith(int i);
};
