#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <vector>
#include <queue>

using namespace std;

//classes

class Node{

public:
  Node();
  Node(int,string);
  int id;
  string name;
};

Node::Node(int id1, string name1){
  id=id1; name=name1;
}

class Graph{

public:
  void InsertNode(Node x);
  void InsertEdge(int x, int y);
  void CommonNeighbor(int x, int y);
  void ShortestPath(int source, int destination);
  void printAllNodes();
  void printAllEdges();
//const map <int, string> &graph
private:
  map <int, string> nodes;
  typedef vector <int> edg;
  vector <edg> edges;

};

void Graph::InsertNode(Node x){ //add id exists
  if(nodes.count(x.id)==1){cout<< "ID exists.\n";}
  else{nodes[x.id]=x.name;}
}

void Graph::printAllNodes(){
  map<int,string>::iterator itr;
  for (itr=nodes.begin(); itr!=nodes.end(); itr++){

      cout<< (*itr).first << " " << (*itr).second << endl;
  }
}

void Graph::InsertEdge(int x, int y){
  if (nodes.count(x) == 0 || nodes.count(y)==0){
      cout<< "No such node." << endl;
      return;
    }

  int flag=0;
  vector<edg>::iterator itr;
  vector<int>::iterator itr2;

  for (itr=edges.begin();itr!=edges.end();itr++){

    itr2=(*itr).begin();
    if ((*itr2) == x){flag=1; break;}
    }

  if (flag==1){//node vector exists
   for (itr2; itr2!=(*itr).end(); itr2++){ //check if node exists in node vector
        if((*itr2) == y){flag=3; break;}
      }
    //sort(itr2,(*itr).end());
    //if(binary_search(itr2,(*itr).end(),y)){flag=3;}
    if (flag!=3){
      (*itr).push_back(y); //if doesnt exist already, push_back
    }
    }

  if (flag==0){//node vector doesnt exist

    vector<int> v1;
    v1.push_back(x); v1.push_back(y);
    edges.push_back(v1);
    }
}

void Graph::printAllEdges(){
  vector<edg>::iterator itr;
  vector<int>::iterator itr2;

  for (itr=edges.begin();itr!=edges.end();itr++){
    for (itr2=(*itr).begin();itr2!=(*itr).end();itr2++){

      cout << *itr2 << " ";
    }

    cout << endl;
  }
}

void Graph::CommonNeighbor(int x, int y){

  if (nodes.count(x) == 0 || nodes.count(y)==0){ //"no such node"
    cout<< "No such node." << endl;
    return;
  }

  vector<edg>::iterator itr_main;
  vector<int>::iterator itr1;
  vector<int>::iterator itr1_end;
  vector<int>::iterator itr2;
  vector<int>::iterator itr2_end;

  vector<int> v(100);
  vector<int>::iterator itr_v;

  for (itr_main=edges.begin();itr_main!=edges.end();itr_main++){
    //cout <<"hello";
    //itr1=(*itr_main).begin();
    //itr1_end=(*itr_main).end();
    if ((*((*itr_main).begin())) == x){
      itr1=(*itr_main).begin();
      itr1_end=(*itr_main).end();
      }
    }

  for (itr_main=edges.begin();itr_main!=edges.end();itr_main++){
    //cout<<"hel";
    if ((*((*itr_main).begin())) == y){
      itr2=(*itr_main).begin();
      itr2_end=(*itr_main).end();
      }
    }

  sort(itr1+1,itr1_end);
  sort(itr2+1,itr2_end);
  itr_v=set_intersection(itr1+1,itr1_end,itr2+1,itr2_end,v.begin());
  v.resize(itr_v-v.begin());

  if(v.size()==0){cout<< "No common neighbor.\n"; return;}


  for (itr_v=v.begin(); itr_v!=v.end(); itr_v++){    //no common neighbor, output name of nodes using BS
    map<int,string>::iterator map_itr;
    map_itr = nodes.lower_bound(*itr_v);
    cout << (*map_itr).first << " " << (*map_itr).second << endl;
  }

}

void print_bfs(map <int,string> nodes, map <int,int> previous,int source){

  if (source==-1){return;}

  source=previous[source];
  print_bfs(nodes,previous,source);
  if(source!=-1){cout << source << " " << nodes[source]<< endl;}

}

void Graph::ShortestPath(int source, int destination){
  queue<int> q;
  map<int,int> previous;
  map<int,bool> visited;

  map<int,string>::iterator itr;
  for (itr=nodes.begin(); itr!=nodes.end(); itr++){
      previous[(*itr).first]=-1;
      visited[(*itr).first]=0;
    }
  q.push(source);
  visited[source]=1;
  bool foundDestination=0;

  while(!q.empty() && !foundDestination){

    int current = q.front();
    q.pop();

  //  if(!visited[current]){
      //visited[current]=1; //cout << current << endl;
      if(current==destination){foundDestination=1; break;}

      //for each neighbor j of current
      vector<edg>::iterator itr;
      vector<int>::iterator itr2;

      for (itr=edges.begin();itr!=edges.end();itr++){
        if ((*((*itr).begin())) == current){
          for (itr2=(*itr).begin()+1;itr2!=(*itr).end();itr2++){ //all neighbors

            //cout << *itr2 << " ";
            if(!visited[*itr2]){
                q.push(*itr2);
                visited[*itr2]=1;
                previous[*itr2]=current;

            }
          }
        }
      }
    //}
  }

  if(!foundDestination){cout<<"No path found.\n"; return;}

  print_bfs(nodes,previous,destination);
  cout << destination << " " << nodes[destination] << endl;
}

int main(){

  Graph g;
  string command;
  int id1, id2;
  string name;

  while (cin>>command){

    if (command=="InsertNode"){
      cin >> id1 >> name;
      Node n(id1,name);
      g.InsertNode(n);
    }
    if (command=="InsertEdge"){
      cin >> id1 >> id2;
      g.InsertEdge(id1,id2);
    }
    else if (command=="CommonNeighbor"){
      cin >> id1 >> id2;
      g.CommonNeighbor(id1, id2);
    }
    else if (command=="ShortestPath"){
      cin >> id1 >> id2;
      g.ShortestPath(id1, id2);
    }
    else if (command=="Exit"){
      return 0;
    }


  }


}
