#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::string str1, str2;
    std::cin >> str1 >> str2;

    int n = str1.length();
    int m = str2.length();

    std::vector<std::vector<int>> dp(n + 1, std::vector<int>(m + 1, 0));

    for (int j = 0; j <= m; ++j) {
        dp[0][j] = j;
    }

    for (int i = 0; i <= n; ++i) {
        dp[i][0] = i;
    }

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (str1[i - 1] != str2[j - 1]) {
                dp[i][j] = 1 + std::min({dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]});
            } else {
                dp[i][j] = dp[i - 1][j - 1];
            }
        }
    }

    std::cout << dp[n][m] << std::endl;

    return 0;
}
