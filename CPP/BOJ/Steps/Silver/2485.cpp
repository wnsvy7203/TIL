// Silver 5. Colonnade
// 12ms

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int gcd(int a, int b)
{
    while (b)
    {
        int temp = a % b;
        a = b;
        b = temp;
    }

    return a;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N;

    cin >> N;

    vector<int> tree(100005, 0);
    vector<int> sub(100005, 0);

    for (int i = 0; i < N; i++)
    {
        cin >> tree[i];
    }

    sort(tree.begin(), tree.begin()+N);

    for (int i = 1; i < N; i++)
    {
        sub[i-1] = tree[i] - tree[i-1];
    }

    int g = gcd(sub[0], sub[1]);

    for (int i = 2; i < N-1; i++)
    {
        g = gcd(g, sub[i]);
    }

    int cnt = 0;

    for (int i = 0; i < N-1; i++)
    {
        cnt += sub[i] / g - 1;
    }

    cout << cnt;
}