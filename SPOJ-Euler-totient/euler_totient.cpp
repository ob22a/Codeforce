#include <iostream>
#include <vector>
using namespace std;

int main() {
    const int MAX = 1000000;
    int T;
    cin >> T;

    vector<int> spf(MAX + 1, 0);
    vector<int> totient(MAX + 1, 0);
    totient[1] = 1;

    for (int i = 2; i <= MAX; ++i) {
        if (spf[i] == 0) {
            spf[i] = i;
            for (int j = i * 2; j <= MAX; j += i) {
                if (spf[j] == 0)
                    spf[j] = i;
            }
        }
    }

    for (int i = 2; i <= MAX; ++i) {
        int n = i;
        int sol = i;
        int prev = 0;
        while (n > 1) {
            int p = spf[n];
            if (p != prev) {
                sol -= sol / p;
                prev = p;
            }
            n /= p;
        }
        totient[i] = sol;
    }

    while (T--) {
        int n;
        cin >> n;
        cout << totient[n] << "\n";
    }
    return 0;
}
