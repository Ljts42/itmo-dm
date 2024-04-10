#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("cycles.in", "r", stdin);
    freopen("cycles.out", "w", stdout);

    long long n, m;
    cin >> n >> m;
    vector<long long> w(n);
    for (long long i = 0; i < n; ++i) {
        cin >> w[i];
    }
    set<long long> s;
    for (long long i = 0; i < m; ++i) {
        long long a, b, c = 0;
        cin >> a;
        for (long long j = 0; j < a; ++j) {
            cin >> b;
            c |= 1 << (b - 1);
        }
        s.insert(c);
    }
    vector<long long> q(s.begin(), s.end());
    while (!q.empty()) {
        long long i = q.back();
        q.pop_back();
        for (long long j = 0; j < n; ++j) {
            long long k = i | (1 << j);
            if (s.count(k) == 0) {
                q.push_back(k);
                s.insert(k);
            }
        }
    }
    long long t = 0, r = 0;
    for (long long i = (1 << n) - 1; i >= 0; --i) {
        if (s.count(i) == 0) {
            long long z = 0, c = 0, j = 0;
            for (long long k = i; k > 0; k >>= 1, ++j) {
                if (k & 1) {
                    z += w[j];
                    ++c;
                }
            }
            if (c > t) {
                t = c;
                r = z;
            } else if (c == t) {
                r = max(r, z);
            }
        }
    }
    cout << r;
}
