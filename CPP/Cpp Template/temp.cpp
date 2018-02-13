#include <iostream>
#include <string>


using namespace std;


template <class T>
class Node {
public:
T data;
Node<T>* next;
};


template <class T>
class LinkedList {
public:
Node<T>* head;
LinkedList();
void insert_front( T data );
T front();
};


template <class T>
LinkedList<T>::LinkedList(){
								head = NULL;
}

template <class T>
void LinkedList<T>::insert_front( T data ){
								Node<T>* n = new Node<T>;
								(*n).data = data;
								(*n).next = head;
								head = n;
}

template <class T>
T LinkedList<T>::front(){
								return (*head).data;
}

struct Record {
string name;
int number;
};

int main(){

					LinkedList <int> list;
					list.insert_front(1);
					list.insert_front(2);
					cout << list.front() << endl;


					LinkedList <string> list2;
					list2.insert_front("Kit");
					list2.insert_front("Ben");
					cout << list2.front() << endl;


					LinkedList <Record> list3;
					Record r;
					r.name = "Kit"; r.number = 91111111;
					list3.insert_front(r);
					r.name = "Ben"; r.number = 92222222;
					list3.insert_front(r);
					cout << list3.front().number << endl;
					return 0;
}
