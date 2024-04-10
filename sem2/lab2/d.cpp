#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("nfc.in", "r", stdin);
    freopen("nfc.out", "w", stdout);

    long long n, m;
    char s;
    cin >> n >> s;

    unordered_map<char, unordered_set<char>> neterm;
    unordered_set<string> rules;
    neterm[s];

    for (long long i = 0; i < n; ++i) {
        string a, arrow, b;
        cin >> a >> arrow >> b;
        neterm[a[0]];
        if (b.size() == 1) {
            neterm[a[0]].insert(b[0]);
        } else {
            rules.insert({a[0], b[0], b[1]});
            neterm[b[0]];
            neterm[b[1]];
        }
    }
    string word;
    cin >> word;
    m = word.size();

    unordered_map<char, vector<vector<long long>>> cnt;
    for (const auto & c : neterm) {
        cnt[c.first].resize(m);
        for (long long j = 0; j < m; ++j) {
            cnt[c.first][j].resize(m);
        }
    }
    for (const auto & c : neterm) {
        for (long long pos = 0; pos < m; ++pos) {
            cnt[c.first][pos][pos] = c.second.count(word[pos]);
        }
    }
    for (long long length = 1; length < m; ++length) {
        for (long long pos = length - 1; pos >= 0; --pos) {
            for (const auto & rule : rules) {
                for (long long i = pos; i < length; ++i) {
                    cnt[rule[0]][length][pos] += cnt[rule[1]][i][pos] * cnt[rule[2]][length][i + 1];
                    cnt[rule[0]][length][pos] %= 1000000007;
                }
            }
        }
    }

    cout << cnt[s][m - 1][0] << endl;
}
