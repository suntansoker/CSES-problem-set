#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

#define ll long long

int main() {
    // read the input
    int n;
    std::cin >> n;
    std::vector<std::tuple<ll, ll, ll>> projects(n);

    for (int i = 0; i < n; ++i) {
        int start, end, reward;
        std::cin >> start >> end >> reward;
        projects[i]={end, start, reward};
    }

    std::sort(projects.begin(), projects.end());

    // compute the dp table and totalBestReward
    ll maxReward = 0;
    std::map<ll, ll> dp;  // {end: totalRewardSoFar}
    dp[0] = 0;

    for (const auto& project : projects) {
        ll end, start, reward;
        std::tie(end, start, reward) = project;

        auto it = dp.lower_bound(start);
        it--;
        ll totalReward = it->second + reward;
        maxReward = std::max(maxReward, totalReward);
        dp[end] = maxReward;
    }

    std::cout << maxReward << std::endl;

    return 0;
}
