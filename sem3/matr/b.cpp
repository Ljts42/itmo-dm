#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("destroy.in", "r", stdin);
    freopen("destroy.out", "w", stdout);

    long long n, m, s;
    cin >> n >> m >> s;
    vector<vector<tuple<long long, long long, long long>>> g(n + 1);
    map<long long, long long> d;
    for (long long i = 1; i <= m; ++i) {
        long long a, b, c;
        cin >> a >> b >> c;
        g[a].push_back({c, b, i});
        g[b].push_back({c, a, i});
        d[i] = c;
    }
    set<long long> v;
    v.insert(n);
    priority_queue<tuple<long long, long long, long long>> q;
    for (auto & i : g[n]) {
        q.push(i);
    }
    tuple<long long, long long, long long> t = {0, 0, 0};
    while (v.size() < n) {
        while (!q.empty()) {
            t = q.top();
            q.pop();
            if (v.count(get<1>(t)) == 0) {
                break;
            }
        }
        v.insert(get<1>(t));
        for (auto & i : g[get<1>(t)]) {
            q.push(i);
        }
        d.erase(get<2>(t));
    }
    set<pair<long long, long long>> p;
    for (auto & i : d) {
        p.insert({i.second, i.first});
    }
    vector<long long> r;
    for (auto e = p.begin(); e != p.end() && s >= e->first; ++e) {
        s -= e->first;
        r.push_back(e->second);
    }
    sort(r.begin(), r.end());
    cout << r.size() << '\n';
    for (long long i = 0; i < r.size(); ++i) {
        cout << r[i] << ' ';
    }
}
