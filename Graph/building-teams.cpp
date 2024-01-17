#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

bool isBipartite(int node, vector<int>& color, unordered_map<int, vector<int>>& adj, bool& result) {
    if (color[node] == -1) {
        color[node] = 1;
    }

    for (int it : adj[node]) {
        if (color[it] == -1) {
            color[it] = 3 - color[node];
            if(!isBipartite(it, color, adj, result)){
                cout << "IMPOSSIBLE" << endl;
                exit(0);
            }
        } else if (color[it] == color[node]) {
            result = false;
            return false;
        }
    }
    return true;
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> arr(m, vector<int>(2));
    unordered_map<int, vector<int>> adj;

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < 2; ++j) {
            cin >> arr[i][j];
            adj[arr[i][j]].push_back(arr[i][(j + 1) % 2]);
        }
    }

    vector<int> color(n + 1, -1);

    bool result = true;
    for (int i = 1; i <= n; ++i) {
        if (color[i] == -1) {
            if(!isBipartite(i, color, adj, result)){
                cout << "IMPOSSIBLE" << endl;
                exit(0);
            }
        }
    }

    
    for (int i = 1; i <= n; ++i) {
        cout << color[i] << ' ';
        
        cout << endl;
    }

    return 0;
}
