#include <bits/stdc++.h>
using namespace std;
using ull = unsigned long long;
using ll = long long;
int MOD = 360;

int main()
{
    int N;
    cin >> N;

    vector<int> vec(N);
    for (int i = 0; i < N; i++)
    {
        cin >> vec.at(i);
    }

    int now = 0;
    vector<int> cuts(0);
    cuts.push_back(0);
    for (int i = 0; i < N; i++)
    {
        now += vec[i];
        now %= MOD;
        cuts.push_back(now);
    }
    cuts.push_back(MOD);

    sort(cuts.begin(), cuts.end());

    int ans = 0;

    for (int i = 1; i < cuts.size(); i++)
    {
        ans = max(ans, cuts[i] - cuts[i - 1]);
    }
    cout << ans << endl;

    return 0;
}
