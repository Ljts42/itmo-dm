#include <iostream>
 
using namespace std;
 
int d = 0;
int n;
 
int r(int k, int v, int h, int s1[100][100], int s2[100][100], int m)
{
    d = (h > d) ? h : d;
    if (s1[k][0] == 0)
    {
        return (v >> (m - s1[k][1])) % 2;
    }
    else
    {
        int q = 0;
        for (int i = 1; i <= s1[k][0]; i++)
        {
            q = (q << 1) + r(s1[k][i] - 1, v, h + 1, s1, s2, m);
        }
        return s2[k][q];
    }
}
 
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
 
    int m = 0;
    cin >> n;
    int s1[100][100];
    int s2[100][100];
    for (int i = 0; i < n; i++)
    {
        int a;
        cin >> a;
        if (a == 0)
        {
            s1[i][0] = 0;
            s1[i][1] = ++m;
        }
        else
        {
            s1[i][0] = a;
            for (int j = 1; j <= a; j++)
            {
                cin >> s1[i][j];
            }
            for (int j = 0; j < (1 << a); j++)
            {
                cin >> s2[i][j];
            }
        }
    }
 
    int res[1 << m];
    for (int i = 0; i < (1 << m); i++)
    {
        res[i] = r(n - 1, i, 0, s1, s2, m);
    }
 
    cout << d << '\n';
    for (int i : res)
    {
        cout << i;
    }
    cout << '\n';
}