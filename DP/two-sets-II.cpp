#include <iostream>
#include <vector>

const long long MOD = 1000000007;

long long n;
long long sm;

std::vector<std::vector<long long>> dp;

long long findWays(long long idx, long long left) {
    if (left < 0) {
        return 0;
    }
    if (idx == 0) {
        return (left == 0) ? 1 : 0;
    }
    if (dp[idx][left] != -1) {
        return dp[idx][left];
    }

    long long take = findWays(idx - 1, left - idx);
    long long notTake = findWays(idx - 1, left);

    dp[idx][left] = (take + notTake) % MOD;
    return dp[idx][left];
}

int main() {
    std::cin >> n;

    sm = (n * (n + 1)) / 2;

    if (sm % 2 != 0) {
        std::cout << 0 << std::endl;
    } else {
        sm /= 2;
        dp.assign(n + 1, std::vector<long long>(sm + 1, -1));

        long long ways = (findWays(n, sm) * 500000004) % MOD;
        std::cout << ways << std::endl;
    }

    return 0;
}
