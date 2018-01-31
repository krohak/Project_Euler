#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;


class Node{

    public:
           char c;
           Node *left_child;
           Node *right_sibling;
           Node();
};

class Tree{

    public:
        Node *head;
        Tree();
        void add(string name);
        int find(string name);
        void print_children();
};

Node::Node(){


    left_child = NULL;
    right_sibling = NULL;


}

Tree::Tree(){


    head = new Node;


}

void Tree::add(string name){

  /*

  1. Check name[cur_c] in all non-null siblings of the first child of head
    - if not found (node->c != name[cur_c] && node->right == NULL), make a sibling node of first left_child
    - if found (node->c == name[cur_c]):
      - if no child, add name[cur_c:] to child list
      - else, go to child node and search for name[cur_c+1]
  */

    Node* node = new Node;
    node = head;

    int cur_c = 0;

    if (node->left_child != NULL){

      node=node->left_child;

      while(node != NULL){

        if(node->c != name[cur_c] && node->right_sibling == NULL){   //node->left_child null or not null [end of list]
          Node* node2 = new Node;
          node2->c = name[cur_c];
          node->right_sibling = node2;
          node = node->right_sibling;
          cur_c++;
        //  cout << "hi2";
          break;
        }

        else if(node->c == name[cur_c] && node->left_child == NULL){  //either node->right_sibling is null or not [end of list or not]
          cur_c++;
        //  cout <<"hi3";
          break;
        }

        else if(node->c == name[cur_c]){
          node = node->left_child;
        //  cout <<"hi3";
          cur_c++;

          if(node->right_sibling == NULL){
            break;
          }

        }

        //cout << "hi1";
        node=node->right_sibling;

      }
    }


    for(int i=cur_c; i<name.length(); i++){

        Node* node2 = new Node;
        node2->c = name[i];
        //cout << node->c;
        node->left_child = node2;
        node = node->left_child;
    }

    return;

}

void Tree::print_children(){

  Node* node1 = new Node;
  node1 = head->left_child;
  node1 = node1 -> right_sibling;
  cout << node1->c;
  //cout << "yas";

/*if (node1->left_child == NULL && node-> right_sibling != NULL){
    cout << node1->c;
    print_children(node1->right_sibling);
    return;
  }*/

if(node1 !=NULL){

/* while(node1->right_sibling!=NULL){

    //cout << "hello";
    node1 = node1->right_sibling;
    cout << node1->c;

  }*/

  while(node1->left_child!=NULL){

    //cout << "hello";
    node1 = node1->left_child;
    cout << node1->c;


  }
}
  return;
}

int Tree::find(string name){

  /*
  1. Find the name in tree by iterating through the right siblings and going to the left child whenever we match a character in name
  2. if left_child of the last character match is null, return 0
  3. if not null,go to the left_child of the last character match
  4. count the number of siblings [including the first] and return it
  */

//!! modify code to work with nth character

  Node* node = new Node;
  node = head;

  int cur_c = 0;
  int num = 0;
  //char last = name[name.length()-1]

  if (node->left_child != NULL){

    node=node->left_child;

    while(node != NULL){

      if(node->c != name[cur_c]){
        //cout<< "hi";

        node = node -> right_sibling;

        if (node->right_sibling == NULL){
        return 0;
       }

      }

      else if(node->c == name[cur_c]){

                if( node->left_child == NULL){  //either node->right_sibling is null or not [end of list or not]

                  cur_c++;

                 if (cur_c != name.length()){ //found no occurance of string
                    //cout <<"hi";
                    return 0;
                  }

                num++;
                return num;  //found one occurance
                }

              else { //finding a char when child isnt nulll
                node = node->left_child;
                //num++;
                cur_c++;


                if (cur_c == name.length()){ //if whole string found

                  while(node->right_sibling!=NULL){

                      //cout << "hello";
                      node = node->right_sibling;
                      num++;
                      //cout << node1->c;

                    }
                    //cout <<"debug";
                    return num;  //counted all siblings
                }

                node=node->right_sibling;

              }
          }
    }
  }



}

int main(){
    int n;
    Tree T;
    Node nl;
    cin >> n;
    for(int a0 = 0; a0 < n; a0++){
        //string op;
        string contact;
        cin >> contact;
        T.add(contact);
    }
    //T.print_children();
    cout << T.find("as");
    //cout << T.head;
    return 0;
}
