#include <bits/stdc++.h>

using namespace std;


#define NIL -1
using namespace std;

class Graph
{
    int V;
    list<int> *adj;
    void APUtil(int v, bool visited[], int disc[], int low[],
                int parent[], int &ap);
public:
    Graph(int V);
    void addEdge(int v, int w);
    int AP();

};

void Graph::APUtil(int v, bool visited[], int disc[], int low[], int parent[], int &ap) {

    static int time=0;
    visited[v] = true;
    disc[v] = low[v] = ++time;

    int children = 0;

    for(int edge : adj[v]){

        if (visited[edge]==false){
            children++;
            parent[edge] = v;
            APUtil(edge,visited,disc,low,parent,ap);
            low[v] = min(low[edge],low[v]);

            if (parent[v] == NIL && children > 1 ){
                ap++;
            }
            if (parent[v] != NIL && low[edge] >= disc[v] ){
                ap++;
            }
        }
        else if (edge != parent[v] ){
            low[v] = min(low[v],disc[edge]);
        }


    }


}
Graph::Graph(int V)
{
    this->V = V;
    adj = new list<int>[V];
}

void Graph::addEdge(int v, int w)
{
    adj[v].push_back(w);
    adj[w].push_back(v);
}

int Graph::AP() {

    int low[V];
    int parent[V];
    int disc[V];
    for(int i=0;i<V;i++){
        low[i] =0;
        parent[i] = NIL;
        disc[i]= 0;
    }

    bool visited[V];
    int ap=0;

    for(int i=1;i<V;i++){
        if (visited[i]==false){
            APUtil(i,visited,disc,low,parent,ap);
        }
    }


    return ap;


}

int main() {

    while(true){
        int n,m;
        cin >> n >> m;
        if (n ==0 && m == 0){
            break;
        }
        Graph g(n+1);
        int from,to;
        for(int i=0;i<m;i++){
            cin >> from >> to;
            g.addEdge(from,to);
        }
        cout << g.AP()<<endl;





    }

}