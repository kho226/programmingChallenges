//CPP program to demonstrate basic depth first search

#include <iostream>
#include <list>

using namespace std;

class Graph{
    private:
        int V;
        list<int> *adj;
        void dfs_util(bool visited[], int i);
    public:
        Graph(int x = 0){V = x;}
        void dfs_iterative(int i = 0);
        void add_edge(int i, int w);
        void dfs_recursive(int i = 0);
};

//exhaustive 
void Graph::dfs_recursive(int i = 0){
    bool *visited = new bool[V];
    for (int i = 0; i < V; i++){
        visited[i] = false;
    }

    for (int i = 0; i < V; i++){
        if (visited[i] == false){
            dfs_util(visited, i);
        }
    }
}

void Graph::dfs_util(bool visited[], int v){
    visited[v] = true;

    list<int>::iterator i;

    for(i = adj[v].begin(); i != adj[v].end(); i++){
        if (!visited[*i]){
            dfs_util(visited,*i);
        }
    }
}

void Graph::add_edge(int i, int w){
    adj[w].push_back(i);
}


int main()
{
    // Create a graph given in the above diagram
    Graph g(4);
    g.add_edge(0, 1);
    g.add_edge(0, 2);
    g.add_edge(1, 2);
    g.add_edge(2, 0);
    g.add_edge(2, 3);
    g.add_edge(3, 3);
 
    cout << "Following is Depth First Traversal"
            " (starting from vertex 2) \n";
    g.dfs_recursive(2);
 
    return 0;
}