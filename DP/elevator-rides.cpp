#include <iostream>
#include <vector>
#include <algorithm>

const int INF = 1e9;

int main() {
    int n, x;
    std::cin >> n >> x;

    std::vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
    }

    std::vector<std::vector<int>> dp(1 << n, std::vector<int>(2, INF));
    dp[0][0] = 1;
    dp[0][1] = 0;

    for (int mask = 1; mask < (1 << n); ++mask) {
        for (int i = 0; i < n; ++i) {
            if ((mask & (1 << i)) > 0) {
                int prev = mask ^ (1 << i);
                int numberofElevators = dp[prev][0];
                int totalCount = dp[prev][1];

                if (totalCount + arr[i] <= x) {
                    dp[mask] = std::min(dp[mask], std::vector<int>{numberofElevators, totalCount + arr[i]});
                } else {
                    dp[mask] = std::min(dp[mask], std::vector<int>{numberofElevators + 1, arr[i]});
                }
            }
        }
    }

    std::cout << dp[(1 << n) - 1][0] << std::endl;

    return 0;
}
