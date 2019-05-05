#include <iostream>
#include "CircularArray.h"
#include <vector>

using namespace std;

void traverseTimes(const CircularArray &ca, int times);
void traverseTimesBackwards(const CircularArray &ca, int times);


//-----------------------
//Main
//-----------------------
int main(){
	cout << "------------------------\n";
	cout << "Required Task 1\n";
	cout << "------------------------\n";
	cout << "A double linked list is implemented here. The value type is int, but can be changed to a template type.\n";
	//Instance of CircularArray
	CircularArray ca;

	//Appending values 0-4 one by one
	cout << "The double linked list is first populated with values 0-4 one by one. Constant time since we are manipulating a constant amount of links.\n";
	ca.append(0);
	ca.append(1);
	ca.append(2);
	ca.append(3);
	ca.append(4);

	//Since it's a double linked list, it can be traversed forwards and backwards in linear time
	cout << "Since it's a double linked list, it can be traversed forwards and backwards in linear time.\n";
	traverseTimes(ca,1);
	traverseTimesBackwards(ca,1);

	//Appending values 5-10 through vector append
	cout << "The method is overloaded to allow adding a vector full of values in. Values 5-10 are added.\n";
	vector<int> addvec;
	int upper = 10;
	for (int i = 5; i <= upper; i++) 
        addvec.push_back(i);
	ca.append(addvec); 
	
	//Printing
	traverseTimes(ca,1);

	//Getting node at index 5
	cout << "We can get a node at any index in <= n/2 time. Getting node 5, values is\n"; 
	node*n = ca.getith(1);
	cout << n->data << "\n";

	//Rotating once
	cout << "Rotations are done by just changing the head, which can be done in constant time. Rotating backwards (-1).\n";	
	ca.rotate(-1);

	//Printing
	traverseTimes(ca,1);

	//Rotating 5 steps
	cout << "Rotating any amount of steps is a constant time operation too, rotating 5 steps.\n";	
	ca.rotate(5);

	//Printing
	traverseTimes(ca,1);

	//Delete element number 6
	cout << "Deletion takes linear time because we need iterate to the index. If we know the node we want to delete, it is a lot easier. Poping an element, for instance, takes constant time. We delete element number 6 here.\n";	
	ca.delith(5);

	//Printing
	traverseTimes(ca,1);
	traverseTimesBackwards(ca,1);

	return 0;
}

//Traverses link list ca times times following next pointers
void traverseTimes(const CircularArray &ca, int times){
	if(times == 1){
		cout << "Traversing once forwards: [";
	}
	else
		cout << "Traversing "<< times << " times forwards.\n[";
	node *n = ca.head;
	for(int i = 0; i < ca.size*times; i++){
		if(i != ca.size*times-1)
			cout << n->data << ", ";
		else
			cout << n->data << "]\n";
		n = n->next;
	}
}

//Traverses link list ca times times following last pointers
void traverseTimesBackwards(const CircularArray &ca, int times){
	if(times == 1){
		cout << "Traversing once backwards: [";
	}
	else
		cout << "Traversing "<< times << " times backwards.\n[";
	node *n = ca.head;
	for(int i = 0; i < ca.size*times; i++){
		if(i != ca.size*times-1)
			cout << n->data << ", ";
		else
			cout << n->data << "]\n";
		n = n->last;
	}
}
