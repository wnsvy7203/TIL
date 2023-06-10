// Silver 5. Someone Who in the Office
// 80ms

#include <iostream>
#include <set>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;

    cin >> n;

    set<string, greater<string>> office;

    for (int i = 0; i < n; i++)
    {
        string name, status;
        cin >> name >> status;

        if (status == "enter")
            office.insert(name);
        else
            office.erase(name);
    }

    for (auto name : office)
        cout << name << '\n';
}