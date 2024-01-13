#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;

    std::vector<int> arr(n);
    int sm = 0;

    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
        sm += arr[i];
    }

    std::vector<int> dp(sm + 1, 0);
    dp[0] = 1;

    for (int j : arr) {
        for (int i = sm; i > 0; --i) {
            if (i - j < 0) {
                break;
            }
            if (dp[i] == 1) {
                continue;
            }
            if (dp[i - j] == 1) {
                dp[i] = 1;
            }
        }
    }

    std::vector<int> ans;
    for (int i = 1; i <= sm; ++i) {
        if (dp[i] == 1) {
            ans.push_back(i);
        }
    }

    std::cout << ans.size() << std::endl;
    
    for (int x : ans) {
        std::cout << x << ' ';
    }

    return 0;
}
