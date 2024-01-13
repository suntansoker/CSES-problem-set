#include <iostream>
#include <vector>

const int MOD = 1000000007;

int main() {

    std::vector<std::vector<int>> dp(1e6 + 1, std::vector<int>(2, 0));
    dp[1][0] = 1;
    dp[1][1] = 1;

    for (int i = 2; i <= 1e6; ++i) {
        dp[i][0] = (2LL * dp[i - 1][0] + dp[i - 1][1]) % MOD;
        dp[i][1] = (4LL * dp[i - 1][1] + dp[i - 1][0]) % MOD;
    }

    int t;

    std::cin >> t;

    while (t > 0) {
        int n;
        std::cin >> n;

        std::cout << (dp[n][0] + dp[n][1]) % MOD << std::endl;

        t -= 1;
    }

    return 0;
}
