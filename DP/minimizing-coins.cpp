#include <iostream>
#include <vector>

const int INF = 1e8;

int main() {
    int n, x;
    std::cin >> n >> x;

    std::vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
    }

    std::vector<int> dp(x + 1, INF);
    dp[0] = 0;

    for (int i = 1; i <= x; ++i) {
        for (int j : arr) {
            if (i - j >= 0) {
                dp[i] = std::min(dp[i], 1 + dp[i - j]);
            }
        }
    }

    if (dp[x] >= INF) {
        std::cout << -1 << std::endl;
    } else {
        std::cout << dp[x] << std::endl;
    }

    return 0;
}
