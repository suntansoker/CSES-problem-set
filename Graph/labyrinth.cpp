#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<char>> mat(n, vector<char>(m));
    int startRow = -1, startCol = -1, endRow = -1, endCol = -1;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> mat[i][j];
            if (mat[i][j] == 'A') {
                startRow = i;
                startCol = j;
            } 
            else if (mat[i][j] == 'B') {
                endRow = i;
                endCol = j;
            }
            
        }
    }

    int a[4] = {0, -1, 0, 1};
    int b[4] = {-1, 0, 1, 0};

    queue<vector<int>> q;
    q.push({0, -2, startRow, startCol});

    vector<vector<int>> vis(n, vector<int>(m, 0));
    vector<vector<int>> prev(n, vector<int>(m, -1));

    prev[startRow][startCol] = -2;
    int minDist = 100000000;

    while (!q.empty()) {
        vector<int> front = q.front();
        q.pop();

        // int dist = front[0];
        int x = front[2];
        int y = front[3];

        vis[x][y] = 1;
        prev[x][y] = front[1];

        if (x == endRow && y == endCol) {
            minDist = front[0];
            break;
        }

        for (int i = 0; i < 4; ++i) {
            int pos_x = x + a[i];
            int pos_y = y + b[i];

            if (0 <= pos_x && pos_x < n && 0 <= pos_y && pos_y < m && vis[pos_x][pos_y] == 0 && mat[pos_x][pos_y] != '#') {
                q.push({front[0] + 1, i, pos_x, pos_y});
                vis[pos_x][pos_y] = 1;  // Mark visited to avoid revisiting
            }
        }
    }

    string ans = "";

    if (prev[endRow][endCol] != -1) {
        do {
            int val = prev[endRow][endCol];
            if (val == 0) {
                ans = 'L' + ans;
                endCol += 1;
            } else if (val == 1) {
                ans = 'U' + ans;
                endRow += 1;
            } else if (val == 2) {
                ans = 'R' + ans;
                endCol -= 1;
            } else if (val == 3) {
                ans = 'D' + ans;
                endRow -= 1;
            } else {
                break;
            }
        } while(prev[endRow][endCol] != -2);

        cout << "YES" << endl;
        cout << minDist << endl;
        cout << ans << endl;
    } else {
        cout << "NO" << endl;
    }

    return 0;
}