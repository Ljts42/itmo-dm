#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("schedule.in", "r", stdin);
    freopen("schedule.out", "w", stdout);

    long long n;
    cin >> n;
    vector<pair<long long, long long>> s;
    set<long long> z;
    for (long long i = 1; i <= n; ++i) {
        long long d, w;
        cin >> d >> w;
        s.push_back(make_pair(d, w));
        z.insert(i);
    }
    sort(s.begin(), s.end(), [](const pair<long long, long long> & lhs, const pair<long long, long long> & rhs) { return lhs.second > rhs.second || (lhs.second == rhs.second && lhs.first > lhs.first); });
    long long p = 0;
    for (long long i = 0; i < n; ++i) {
        auto j = z.upper_bound(s[i].first);
        if (j == z.end()) {
            continue;
        } else if (j == z.begin()) {
            p += s[i].second;
        } else {
            --j;
            z.erase(j);
        }
    }
    cout << p;
}
