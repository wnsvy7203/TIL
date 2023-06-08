// Silver 5. Sorting for Age
// 108ms

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
vector<pair<int, string>> user;

bool sort_by_age(pair<int, string> a, pair<int, string> b)
{
    return a.first < b.first;
}

int main()
{
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        int age;
        string name;

        cin >> age >> name;

        user.push_back(make_pair(age, name));
    }

    stable_sort(user.begin(), user.end(), sort_by_age);

    for (int i = 0; i < N; i++)
        cout << user[i].first << ' ' << user[i].second << '\n';
}