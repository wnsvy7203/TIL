// Silver 5. Windows Closing

// 약수가 홀수 개 일 때만 열리네
// 제곱수

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N;

    cin >> N;

    int cnt = 0;

    for (int i = 1; i < sqrt(N)+1; i++)
    {
        if (pow(i, 2) <= N)
            cnt++;
    }

    cout << cnt;
}