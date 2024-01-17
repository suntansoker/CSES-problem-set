#include <iostream>
#include <vector>
#include <queue>

int main() {
    int n, m;
    std::cin >> n >> m;

    std::vector<std::vector<char>> mat(n, std::vector<char>(m));

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            std::cin >> mat[i][j];
        }
    }

    int count = 0;
    std::vector<int> vis(n * m, 0);

    std::vector<int> a = {0, -1, 0, 1};
    std::vector<int> b = {-1, 0, 1, 0};

    auto bfs = [&](int start) {
        std::queue<int> q;
        q.push(start);

        while (!q.empty()) {
            int idx = q.front();
            q.pop();
            int i = idx / m;
            int j = idx % m;
            vis[idx] = 1;

            for (int k = 0; k < 4; ++k) {
                int new_x = i + a[k];
                int new_y = j + b[k];
                int new_idx = new_x * m + new_y;

                if (0 <= new_x && new_x < n && 0 <= new_y && new_y < m && !vis[new_idx] && mat[new_x][new_y] == '.') {
                    q.push(new_idx);
                    vis[new_idx] = 1;  // Mark visited to avoid revisiting
                }
            }
        }
    };

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            int idx = i * m + j;
            if (!vis[idx] && mat[i][j] == '.') {
                count++;
                bfs(idx);
            }
        }
    }

    std::cout << count << std::endl;

    return 0;
}
