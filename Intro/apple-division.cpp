#include <iostream>
#include <vector>
#include <cmath>

int main() {
    int n;
    std::cin >> n;

    std::vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
    }

    long long mn = 1e18;

    for (int i = 0; i < (1 << n); ++i) {
        long long sm1 = 0, sm2 = 0;
        for (int j = 0; j < n; ++j) {
            if ((1 << j) & i) {
                sm1 += arr[j];
            } else {
                sm2 += arr[j];
            }
        }

        mn = std::min(mn, std::abs(sm1 - sm2));
    }

    std::cout << mn << std::endl;

    return 0;
}
