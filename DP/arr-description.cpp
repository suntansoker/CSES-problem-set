#include <iostream>
#include <vector>

const int MOD = 1000000007;

int main() {
    int n, m;
    std::cin >> n >> m;

    std::vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
    }

    std::vector<std::vector<int>> dp(n + 1, std::vector<int>(m + 1, 0));

    // Base case
    for (int i = 1; i <= m; ++i) {
        if (arr[0] == 0 || arr[0] == i) {
            dp[1][i] = 1;
        }
    }

    for (int i = 2; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (arr[i - 1] != 0 && arr[i - 1] != j) {
                dp[i][j] = 0;
                continue;
            }

            for (int k = j - 1; k < std::min(m + 1, j + 2); ++k) {
                dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD;
            }
        }
    }

    int ans = 0;
    for (int i = 1; i <= m; ++i) {
        ans = (ans + dp[n][i]) % MOD;
    }

    std::cout << ans << std::endl;

    return 0;
}
