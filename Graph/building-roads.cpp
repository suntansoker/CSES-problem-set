#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;

void bfs(vector<vector<int>>& adj, vector<int>& visited, int start) {
        queue<int> q;
        q.push(start);
        visited[start] = 1;

        while (!q.empty()) {
            int node = q.front();
            q.pop();

            for (int neighbor : adj[node]) {
                if (!visited[neighbor]) {
                    q.push(neighbor);
                    visited[neighbor] = 1;
                }
            }
        }
    }

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> adj(n + 1); // Adjacency list representation
    vector<int> visited(n + 1, 0);   // Visited array to keep track of visited nodes

    // Assuming the graph is given as edges
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> comps;
    queue<int> q;

    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            bfs(adj, visited, i);
            comps.push_back(i);
        }
    }

    if (comps.size() <= 1) {
        cout << 0 << endl;
    } else {
        cout << comps.size() - 1 << endl;
        for (int i = 1; i < comps.size(); ++i) {
            cout << comps[i] << ' ' << comps[i - 1] << endl;
        }
    }

    return 0;
}
