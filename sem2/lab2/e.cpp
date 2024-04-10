#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("cf.in", "r", stdin);
    freopen("cf.out", "w", stdout);

    long long n, m;
    char s;
    cin >> n >> s;

    vector<pair<char, string>> not_small;
    vector<pair<char, string>> small;
    vector<char> epsilon;

    char inp[100];
    cin.getline(inp, 100);

    for (long long i = 0; i < n; i++) {
        memset(inp, 0, 100);

        cin.getline(inp, 100);
        char left_part = inp[0] - 'A';

        string right_part;
        bool is_small = true;
        for (long long j = 5; is_letter(inp[j]); j++) {
            if (is_big(inp[j]))
                is_small = false;
            right_part.push_back(inp[j]);
        }

        if (is_small) {
            small.push_back(pair<char, string>(left_part, right_part));
        } else if (right_part.size() == 0) {
            epsilon.push_back(left_part);
        } else {
            not_small.push_back(pair<char, string>(left_part, right_part));
        }
    }
    vector<vector<vector<bool>>> a(26);

    string word;
    cin >> word;
    m = word.size();
    
    for (long long i = 0; i < 26; i++) {
        a[i].resize(m + 1);
        for (long long j = 0; j < m; j++) {
            a[i][j].resize(m + 1);
        }
    }

    vector<vector<vector<vector<bool>>>> h(26);
    for (long long i = 0; i < 26; i++) {
        h[i].resize(m + 1);
        for (long long j = 0; j < m; j++) {
            h[i][j].resize(m + 1);
            for (long long k = 0; k < m; k++) {
                h[i][j][k].resize(100);
            }
        }
    }

    /* Initialize dp */
    for (long long i = 0; i < m; i++) {
        long long j = 0;
        for (auto str = small.begin(); str != small.end(); ++str, ++j) {
            if (str->second.size() == 1 && str->second[0] == word[i]) {
                a[str->first][i][i + 1] = true;
            }
            h[j][i][i][0] = true;
        }
        for (auto str = epsilon.begin(); str != epsilon.end(); ++str) {
            a[*str][i][i] = true;
        }
    }

    /* Count dp */
    for (long long len = 1; len < m; len++) {
        for (long long i = 0; i < m; i++) {
            long long j = i + len;
            for (long long str = 0; str < small.size(); ++str) {
                for (long long k = 1; k < small[str].second.size(); k++) {
                    for (long long r = i; r < j + 1; r++) {
                        h[str][i][j + 1][k] = h[str][i][j + 1][k] || (h[str][i][r][k - 1] && a[small[str].second[k]][r][j + 1]);
                    }
                }
            }
        }
    }

    for (long long i = 0; i < m; i++) {
        for (long long j = 0; j < m; j++) {
            for (long long str = 0; str < small.size(); ++str) {
                for (long long str_a = 0; str_a < small.size(); ++str_a) {
                    if (small[str_a].first == small[str].first) {
                        a[small[str_a].first][i][j] = a[small[str_a].first][i][j] || h[str_a][i][j][small[str_a].second.size()];
                    }
                }
            }
        }
    }

    if (a[s - 'A'][0][m - 1]) {
        cout << "yes" << endl;
    } else {
        cout << "no" << endl;
    }
}