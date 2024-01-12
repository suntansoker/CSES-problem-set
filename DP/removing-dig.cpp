#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n;
    std::cin >> n;

    const int INF = 1e8;
    std::vector<int> dp(n + 1, INF);
    dp[0] = 0;

    for (int i = 1; i <= n; ++i) {
        for (char j : std::to_string(i)) {
            dp[i] = std::min(1 + dp[i - (j - '0')], dp[i]);
        }
    }

    std::cout << dp[n] << std::endl;

    return 0;
}
