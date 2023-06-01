// Silver 5. Number of Factorial 0

#include <iostream>

using namespace std;

int main()
{
    int N;

    cin >> N;

    int res = 0;

    for (int i = N; i > 1; i--)
    {
        int temp = i;

        while (!(temp % 5))
        {
            res++;
            temp /= 5;
        }
    }
    
    cout << res;
}