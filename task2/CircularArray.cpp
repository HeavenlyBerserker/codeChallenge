#include "CircularArray.h"
#include <cstddef>
#include <vector>

using namespace std;

CircularArray::CircularArray(){
	head = NULL;
	size = 0;
}

void CircularArray::append(int num){
	node *n = new node;
	n->data = num;

	if(head == NULL){
		head = n;
		n->last = n;
		n->next = n;
		n = NULL;
	}
	else{
		n->last = head->last;
		n->next = head;

		head->last->next = n;		
		head->last = n;
	}

	size++;
}

void CircularArray::del(node * n){
	n->last->next = n->next;
	n->next->last = n->last;
	n = NULL;
	delete n;
	size--;
}

bool CircularArray::delith(int i){
	if(size == 0){
		return false;
	}
	node * n = getith(i);
	del(n);
	return true;
}

void CircularArray::append(vector <int> v){
	for(size_t i = 0; i < v.size(); i++){
		append(v[i]);
	}
}

node* CircularArray::getith(int i){
	if(i < 0) i += size;
	if(i % size > size/2){
		node *n = head;
		for(int j = 0; j < size - (i%size); j++){
			n = n->last;
		}
		return n;
	}
	else{
		node *n = head;
		for(int j = 0; j < i; j++){
			n = n->next;
		}
		return n;
	}
}

void CircularArray::rotate(int steps){
	head = getith(steps);
}
