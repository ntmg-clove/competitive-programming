#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ull = unsigned long long;
int main()
{
    string S;
    cin >> S;
    int a, b;
    cin >> a >> b;
    a--;
    b--;

    int l = S.length();
    // cout << S.length() << endl;
    vector<char> vec(l);

    for (int i = 0; i < l; i++)
    {
        if (i == a)
        {
            vec.at(i) = S[b];
        }
        else if (i == b)
        {
            vec.at(i) = S[a];
        }
        else
        {
            vec.at(i) = S[i];
        }
    }

    for (int i = 0; i < l; i++)
    {
        cout << vec.at(i);
    }
    cout << endl;

    return 0;
}