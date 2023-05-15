// Bronze 1. Divisors' Sum

#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric>

using namespace std;

int main()
{
    int n;

    while (1)
    {
        cin >> n;

        if (n == -1)
        {
            return 0;
        }

        vector<int> div;

        for (int i = 1; i < n; i++)
        {
            if (n % i == 0)
            {
                div.push_back(i);
            }
        }

        if (n == accumulate(div.begin(), div.end(), 0))
        {
            cout << n << " = ";
            for (int i = 0; i < div.size(); i++)
            {
                cout << div[i];
                if (i != div.size() - 1)
                {
                    cout << " + ";
                }
            }
        }
        else
        {
            cout << n << " is NOT perfect.";
        }
        cout << '\n';
    }
}