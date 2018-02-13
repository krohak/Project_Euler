#include <iostream>
#include <string>
#include <assert.h>
#include <list>
#include <vector>
#include <queue>

# define INF 0x3f3f3f3f


using namespace std;

typedef pair<int, int> int_pair;

class Graph{

private:
    int V;
    list< pair<int, int> > *edges;

public:
    Graph(int V);
    void addEdge(int u, int v, int w);
    vector <int> shortestPath(int s);
    vector <int>* query();
};

Graph::Graph(int V)
{
    this->V = V;
    edges = new list<int_pair> [V];
}

void Graph::addEdge(int u, int v, int w)
{
    edges[u].push_back(make_pair(v, w));
    edges[v].push_back(make_pair(u, w));
}


vector<int> Graph::shortestPath(int src)
{

    priority_queue< int_pair, vector <int_pair> , greater<int_pair> > pq;

    vector<int> dist;
    dist=vector<int>(V, INF);

    pq.push(make_pair(0, src));
    dist[src] = 0;


    while (!pq.empty())
    {

        int u = pq.top().second;
        pq.pop();

        list< pair<int, int> >::iterator i;
        for (i = edges[u].begin(); i != edges[u].end(); ++i)
        {

            int v = (*i).first;
            int weight = (*i).second;


            if (dist[v] > dist[u] + weight)
            {

                dist[v] = dist[u] + weight;
                pq.push(make_pair(dist[v], v));
            }
        }
    }
    return dist;
}

vector <int>* Graph::query(){

  for(int i = 0; i < V; i++){ //initialize all v to v dist to 0
    addEdge(i, i, 0);
  }

  vector<int> *dist2;
  dist2 = new vector<int> [V];


  for(int u=0; u<V; u++){ // add distance data to vector



      dist2[u]=vector <int>(V,INF);

    list< pair<int, int> >::iterator i;

    for (i = edges[u].begin(); i != edges[u].end(); ++i)
    {
        int v = (*i).first;
        int weight = (*i).second;

        dist2[u][v]=weight;
    }


  }



for (int k=0; k<V; k++){
  for (int i=0; i<V; i++){

    for (int j=0; j<V; j++){

      if(dist2[i][j]>dist2[i][k] + dist2[k][j]){
          dist2[i][j]=dist2[i][k] + dist2[k][j];
      }

    }

  }
}

return dist2;
}

void NearestDriver(){
    int n, m;

    cin >> n >> m;

    Graph g(n);

    for(int i = 0; i < m; i++){
        int a, b, w;
        cin >> a >> b >> w;

        g.addEdge(a, b, w);
    }

    int u;
    cin >> u;


    vector<int> dist2;
    dist2=g.shortestPath(u);


    int bestv = -1;
    int l;
    int min=INF;
    cin >> l;
    for(int i = 0; i < l; i++){
        // scan over every car to get the final answer
        int c;
        cin >> c;
        if(c<dist2.size()){
          if (dist2[c]<min){
            min=dist2[c];
            bestv=c;
          }
        }
    }

    if(bestv == -1)
        cout << "NO" << endl;
    else
        cout << bestv << endl;

}


void QueryPrice(){
    int n, m;

    cin >> n >> m;

    Graph g(n);

    for(int i = 0; i < m; i++){
        int a, b, w;
        cin >> a >> b >> w;

        g.addEdge(a, b, w);
    }

    vector<int> *dist2;
    dist2=g.query();

    int l;
    cin >> l;
    for(int i = 0; i < l; i++){
        // scan over every query
        int c1,c2;
        cin >> c1 >> c2;
        if(c1<n && c2<n){
          if (dist2[c1][c2]<INF){
            cout << dist2[c1][c2] <<endl;
          }
        else {cout << "NO" <<endl;}
        }
    }

}

void Diameter(){
    int n, m;

    cin >> n >> m;

    Graph g(n);

    for(int i = 0; i < m; i++){
        int a, b, w;
        cin >> a >> b >> w;

        g.addEdge(a, b, w);
    }

    vector<int> *dist2;
    dist2=g.query();

    int max=0;

    for (int i=0; i<n; i++){
      for (int j=0; j<n; j++){

        if(max<dist2[i][j]){max=dist2[i][j];}
      }

    }

    if(max==INF){cout<<"INF"<<endl;}
    else{cout<<max<<endl;}


}

void DiameterApproximation(){
    int n, m;
    cin >> n >> m;

    Graph g(n);

    for(int i = 0; i < m; i++){
        int a, b, w;
        cin >> a >> b >> w;

        g.addEdge(a, b, w);
    }

    vector<int> dist1;
    dist1=g.shortestPath(1);

    int max1=0;
    int p1=0;
    for (int i=0; i<n; i++){
      if(max1<dist1[i]){
          max1=dist1[i];
          p1=i;
        }
    }
    if(max1==INF){cout<<"INF"<<endl; return;}

    vector<int> dist2;
    dist2=g.shortestPath(p1);

    int max2=0;
    for (int i=0; i<n; i++){
      if(max2<dist2[i]){
          max2=dist2[i];
        }
    }

    if(max2==INF){cout<<"INF"<<endl; return;}
    else{cout<<max2<<endl; return;}

}

int main(){

   string section;
    cin >> section;

    if(section == "NearestDriver")
        NearestDriver();
    else if(section == "QueryPrice")
        QueryPrice();
    else if(section == "Diameter")
        Diameter();
    else if(section == "DiameterApproximation")
        DiameterApproximation();
    else{
        cout << "wrong input file!" << endl;
        assert(0);
    }

    return 0;
}
