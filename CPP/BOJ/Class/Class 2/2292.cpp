// Bronze 2. Honeycomb

#include <iostream>

using namespace std;

int N;

int main()
{
    cin >> N;

    if (N == 1)
    {
        cout << 1;
    }
    else
    {
        for (int i = 1; i <= N; i++)
        {
            if (3*i*i - 3*i + 2 <= N && N < 3*i*i + 3*i + 2)
            {
                cout << i+1;
                break;
            }
        }
    }
}