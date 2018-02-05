#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


struct node{
  int data;
  node *left;
  node *right;
};

typedef node node;

node * getNode(){
  node * head = new node;
  head-> data = 0;
  head->right = NULL;
  head->left = NULL;
  return head;
}





int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */

    int m;
    cin >> m;

    string line;
    getline( cin, line );

    node *head = getNode();
    //node *ref = head;

    istringstream is( line );
    int i;

    while( is >> i) {
      node *next = getNode();
      next->data=i;
      head->right = next;
      next->left = head;
      head = head->right;
    }

    while(m>1){
        head = head->left;
        m-=1;
    }

    cout << head->data;

    return 0;
}
