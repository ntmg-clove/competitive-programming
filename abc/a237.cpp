#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (n); i++)
#define rep2(i, x, n) for (int i = x; i < (n); i++)
#define ALL(n) begin(n), end(n)
using ll = long long;
using ull = unsigned long long;
int main()
{
    ll N;
    cin >> N;
    ll t = (ll)1 << 31;

    string ans = "No";
    if (-t <= N && N < t)
    {
        ans = "Yes";
    }

    cout << ans << endl;
    return 0;
}