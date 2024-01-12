#include <iostream>
#include <vector>

int main() {
    int n, x;
    std::cin >> n >> x;

    std::vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
    }

    std::vector<int> dp(x + 1, 0);
    dp[0] = 1;

    for (int i = 1; i <= x; ++i) {
        for (int j : arr) {
            if (i - j >= 0) {
                dp[i] = (dp[i] + dp[i - j]) % 1000000007;
            }
        }
    }

    std::cout << dp[x] << std::endl;

    return 0;
}
