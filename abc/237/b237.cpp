#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (n); i++)
using namespace std;
using ll = long long;
using ull = unsigned long long;
int main()
{
    int H, W;
    cin >> H >> W;

    vector<vector<int>> vec(H, vector<int>(W));
    vector<vector<int>> vec_t(W, vector<int>(H));

    rep(i, H) rep(j, W) cin >> vec.at(i).at(j);

    // 転置行列を作る
    rep(i, H)
    {
        rep(j, W)
        {
            vec_t.at(j).at(i) = vec.at(i).at(j);
        }
    }

    rep(i, W)
    {
        rep(j, H) cout << vec_t.at(i).at(j) << " ";
        cout << endl;
    }

    return 0;
}
