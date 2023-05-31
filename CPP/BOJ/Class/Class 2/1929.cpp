// Silver 3. Finding Prime Numbers
// 20ms

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int M, N;

int main()
{
    vector<bool> prime(1000001, true);

    prime[0] = 0;
    prime[1] = 0;

    int cnt = 2;

    while (cnt <= 1000000)
    {
        if (prime[cnt])
            for (int i = 2 * cnt; i < 1000001; i += cnt)
                prime[i] = 0;
        
        cnt++;
    }

    cin >> M >> N;

    for (int i = M; i <= N; i++)
        if (prime[i])   cout << i << '\n';
}

// 436ms
// int main()
// {
//     cin >> M >> N;

//     for (int i = M; i <= N; i++)
//     {
//         bool flag = 1;

//         if (i == 1) flag = 0;
//         else if (i == 2) flag = 1;
//         else
//             for (int j = 2; j < sqrt(i)+1; j++)
//                 if (!(i % j))
//                 {
//                     flag = 0;
//                     break;
//                 }

//         if (flag)   cout << i << '\n';
//     }
// }