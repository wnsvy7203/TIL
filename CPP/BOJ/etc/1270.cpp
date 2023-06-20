// Silver 3. War - Hopscotch

#include <iostream>
#include <map>
#include <cmath>

using namespace std;

int n;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n;

    while (n--)
    {
        int Ti;

        cin >> Ti;

        map<int, int> T;

        long long int Nij;
        long long int ans;

        bool flag = 0;

        for (int i = 0; i < Ti; i++)
        {
            cin >> Nij;

            if (T.find(Nij) == T.end())
                T.insert({Nij, 1});
            else
                T[Nij]++;
            
            if (T[Nij] > Ti/2)
            {
                ans = Nij;
                flag = 1;
            }
        }

        if (flag) cout << ans << '\n';
        else cout << "SYJKGW" << '\n';
    }
}