// Silver 4. Symmetric Difference

#include <iostream>
#include <set>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N, M;
    set<int> A;
    set<int> B;

    cin >> N >> M;

    for (int i = 0; i < N; i++)
    {
        int num;
        cin >> num;

        A.insert(num);
    }

    for (int i = 0; i < M; i++)
    {
        int num;
        cin >> num;

        B.insert(num);
    }

    int cnt = 0;

    for (auto num : A)
    {
        if (B.find(num) != B.end())
            cnt++;
    }

    cout << A.size() + B.size() - 2 * cnt;
}