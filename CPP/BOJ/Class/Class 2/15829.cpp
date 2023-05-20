// Bronze 2. Hashing

#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
    int M = 1234567891;

    unsigned long long int sum = 0;

    int L;
    
    string str;

    cin >> L >> str;

    long long int r = 1;
    for (int i = 0; i < L; i++)
    {        
        sum += ((str[i] - 96) * r) % M;

        r *= 31;

        if (r > M)
        {
            r %= M;
        }
    }

    if (sum > M)
    {
        sum %= M;
    }
    cout << sum;
}
