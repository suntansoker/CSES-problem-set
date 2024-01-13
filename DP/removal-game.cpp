#include <iostream>
#include <vector>
#include <numeric>

int n;
std::vector<long long> arr;
std::vector<std::vector<long long>> dp;

long long findMaxScore(int left, int right) {
    if (left > right) {
        return 0;
    }
    if (left == right) {
        return arr[left];
    }
    if (dp[left][right] != -1) {
        return dp[left][right];
    }
    long long ifLeft = arr[left] - findMaxScore(left + 1, right);
    long long ifRight = arr[right] - findMaxScore(left, right - 1);
    dp[left][right] = std::max(ifLeft, ifRight);
    return dp[left][right];
}

int main() {
    std::cin >> n;
    arr.resize(n);
    dp.assign(n, std::vector<long long>(n, -1));

    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
    }

    long long maxScore = (std::accumulate(arr.begin(), arr.end(), 0LL) + findMaxScore(0, n - 1)) / 2;
    std::cout << maxScore << std::endl;

    return 0;
}
