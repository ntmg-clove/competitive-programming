#include <bits/stdc++.h>
using namespace std;
using ull = unsigned long long;
using ll = long long;

int main()
{
    int n;
    bool tmp;
    string ans;
    cin >> n;

    if (n < 10)
    {
        tmp = pow(2, n) > pow(n, 2);
    }
    else
    {
        tmp = true;
    }

    ans = tmp ? "Yes" : "No";

    cout << ans << endl;
    return 0;
}
