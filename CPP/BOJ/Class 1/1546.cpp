// Bronze 1. Average

#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int N;

    cin >> N;

    double sub[1005];

    for (int i = 0; i < N; i++)
    {
        cin >> sub[i];
    }

    double* max = max_element(sub, sub+N);
    double val = *max;

    for (int i = 0; i < N; i++)
    {
        sub[i] = sub[i] / val * 100;
    }

    double sum = 0;

    for (int i = 0; i < N; i++)
    {
        sum += sub[i];
    }

    cout << sum / N;
}