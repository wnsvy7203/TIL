// Bronze 2. Prime Number

#include <iostream>
#include <vector>
#include <numeric>
#include <cmath>
#include <algorithm>

using namespace std;

int main()
{
    int M, N;

    cin >> M >> N;

    vector<int> prime;

    int sum(0);

    for (int i = M; i <= N; i++)
    {
        bool check = true;

        if (i == 1)
        {
            check = false;
        }

        for (int j = 2; j <= sqrt(i); j++)
        {
            if (i % j == 0)
            {
                check = false;
                break;
            }
        }

        if (check == true)
        {
            prime.push_back(i);
            sum += i;
        }
    }    

    if (prime.empty())
    {
        cout << -1;
    }
    else
    {

        cout << accumulate(prime.begin(), prime.end(), 0) << '\n' << *min_element(prime.begin(), prime.end());
    }
}