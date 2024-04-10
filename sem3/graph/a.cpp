#include <iostream>
#include <deque>
#include <algorithm>

using namespace std;

int main() {
    size_t n;
    cin >> n;

    bool g[n][n];
    deque<size_t> q;
    g[0][0] = 0;
    q.push_back(0);
    for (size_t i = 1; i < n; ++i) {
        g[i][i] = 0;
        q.push_back(i);

        string c;
        cin >> c;
        for (size_t j = 0; j < i; ++j) {
            g[i][j] = (c[j] == '1');
            g[j][i] = (c[j] == '1');
        }
    }

    for (size_t k = 0; k < n * n; ++k) {
        if (!g[*q.begin()][*next(q.begin())]) {
            auto i = next(q.begin(), 2);
            while (!g[*q.begin()][*i] || !g[*next(q.begin())][*next(i)]) {
                ++i;
            }
            reverse(next(q.begin()), next(i));
        }
        q.push_back(q.front());
        q.pop_front();
    }

    for (size_t i : q) {
        cout << i + 1 << ' ';
    }
}
