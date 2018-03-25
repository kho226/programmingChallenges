//CPP program to detect cycles in a graph

#include <iostream>
#include <list>

using namespace std;

class Graph{
    private:
        int V;
        list<int> *adj;
        void dfs_util(int v, bool visited[]);
        bool cycle_util(bool visited[], int v, bool *rs);
    public:
        Graph(int i = 0){v =i;}
        void dfs(int v = 0);
        void add_edge(int v, int w);
        bool is_cycle(int v);
};


bool Graph::cycle_util(bool visited[], int v, bool *rs){
    if (visited[v] == false){
        visited[v] = true;
        rs[v] = true;

        list<int>::iterator i;
        for (i = adj[v].begin(); i != adj[v].end(); i++){
            if (! visited[*i] && cycle_util(visited, *i, rs)){
                return true;
            }
            else if (rs[*i]){
                return true;
            }
        }
    }
    rs[v] = false;
    return false;
}


bool Graph::is_cycle(int v){

    bool *visited = new bool[V];
    bool *rs = new bool[V];

    for (int i = 0; i < V; i++){
        visited[i] = true;
        rs[i] = true;
    }

    //exhuastive dfs
    for (int i = 0; i < V; i++){
        if (cycle_util(visited, i, rs)){
            return true;
        }
    }
    return false;
}