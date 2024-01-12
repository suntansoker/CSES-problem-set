#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n, x;
    std::cin >> n >> x;

    std::vector<int> price(n);
    std::vector<int> pages(n);

    for (int i = 0; i < n; ++i) {
        std::cin >> price[i];
    }

    for (int i = 0; i < n; ++i) {
        std::cin >> pages[i];
    }

    std::vector<std::vector<int>> dp(n + 1, std::vector<int>(x + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= x; ++j) {
            dp[i][j] = dp[i - 1][j];
            if (j - price[i - 1] >= 0) {
                dp[i][j] = std::max(dp[i][j], pages[i - 1] + dp[i - 1][j - price[i - 1]]);
            }
        }
    }

    std::cout << dp[n][x] << std::endl;

    return 0;
}
