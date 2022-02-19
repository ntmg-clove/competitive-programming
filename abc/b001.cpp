#include <bits/stdc++.h>
using namespace std;
using ull = unsigned long long;
using ll = long long;

int main()
{
    int m;
    string vv;
    cin >> m;

    if (m < 100)
    {
        vv = "00";
    }
    else if (100 <= m && m <= 5000)
    {
        vv = to_string(m / 100);
        if (vv.size() == 1)
        {
            vv = "0" + vv;
        }
    }
    else if (6000 <= m && m <= 30000)
    {
        vv = to_string(m / 1000 + 50);
    }
    else if (35000 <= m && m <= 70000)
    {
        vv = to_string((m / 1000 - 30) / 5 + 80);
    }
    else if (m > 70000)
    {
        vv = to_string(89);
    }

    cout << vv << endl;

    return 0;
}
