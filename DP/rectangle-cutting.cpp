#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int a, b;
    std::cin >> a >> b;

    std::vector<std::vector<int>> dp(a + 1, std::vector<int>(b + 1, 1e9));

    for (int i = 1; i <= a; ++i) {
        for (int j = 1; j <= b; ++j) {
            if (i == j) {
                dp[i][j] = 0;
                continue;
            }
            for (int k = 1; k < i; ++k) {
                dp[i][j] = std::min(dp[i][j], 1 + dp[k][j] + dp[i - k][j]);
            }
            for (int k = 1; k < j; ++k) {
                dp[i][j] = std::min(dp[i][j], 1 + dp[i][k] + dp[i][j - k]);
            }
        }
    }

    std::cout << dp[a][b] << std::endl;

    return 0;
}
