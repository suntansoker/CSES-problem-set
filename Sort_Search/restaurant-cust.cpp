#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n;
    std::cin >> n;

    std::vector<std::pair<int, int>> a;

    for (int i = 0; i < n; ++i) {
        int x, y;
        std::cin >> x >> y;
        a.push_back(std::make_pair(x, 1));
        a.push_back(std::make_pair(y, -1));
    }

    std::sort(a.begin(), a.end());

    int m = 0;
    int cur = 0;

    for (const auto& p : a) {
        cur += p.second;
        m = std::max(cur, m);
    }

    std::cout << m << std::endl;

    return 0;
}