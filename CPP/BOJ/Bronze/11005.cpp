// Bronze 1. Radix Conversion 2

#include <iostream>
#include <vector>

using namespace std;

int N, B = 0;

int main()
{
    cin >> N >> B;

    int n = N;

    vector<char> num;

    do
    {
        if (n % B >= 10)
        {
            num.push_back((n % B) + 55);
        }
        else
        {
            num.push_back((n % B) + 48);
        }

        n /= B;
    }
    while (n != 0);

    for (int i = num.size()-1; i >= 0; i--)
    {
        cout << num[i];
    }
}