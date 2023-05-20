// Bronze 1. Must be Over Average

#include <iostream>

using namespace std;

int C;

int main()
{
    cin >> C;

    for (int c = 0; c < C; c++)
    {
        int N;

        cin >> N;

        int score[1005] = {};

        double sum = 0;
        for (int i = 0; i < N; i++)
        {
            cin >> score[i];
            sum += score[i];
        }

        int cnt = 0;

        for (int i = 0; i < N; i++)
        {
            if (score[i] > sum / N)
            {
                cnt++;
            }
        }

        cout.precision(3);

        cout << fixed << (double)cnt * 100 / N << "%" << "\n";
    }
}