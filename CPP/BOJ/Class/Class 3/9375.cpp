// Silver 3. Fasion Leader Shin

#include <iostream>
#include <map>


using namespace std;

int T;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> T;

    while (T--)
    {
        int n;
        map<string, int> clothes;

        cin >> n;

        for (int i = 0; i < n; i++)
        {
            string name, type;

            cin >> name >> type;

            if (clothes.find(type) == clothes.end())
                clothes.insert({type, 1});
            else
                clothes[type]++;
        }

        int cnt = 1;

        for (auto i : clothes)
            cnt *= i.second+1;

        cout << cnt-1 << '\n';
    }
}