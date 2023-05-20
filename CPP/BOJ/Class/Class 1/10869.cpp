// Bronze 5
// 사칙연산

#include <iostream>

using namespace std;

int main()
{
    int N, X;
    int arr[10005];

    cin >> N >> X;
    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];
    }

    for (int i = 0; i < N; i++)
    {
        if (arr[i] < X)
        {
            cout << arr[i] << " ";
        }
    }
}

// 420ms
// int main()
// {
//     int N, X;
//     int res;

//     cin >> N >> X;
//     for (int i = 0; i < N; i++)
//     {
//         cin >> res;

//         if (res < X)
//         {
//             cout << res << " ";
//         }
//     }
// }