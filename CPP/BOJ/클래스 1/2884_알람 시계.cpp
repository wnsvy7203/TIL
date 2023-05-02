#include <iostream>

using namespace std;

int main()
{
    int H, M;

    cin >> H >> M;

    int time = H * 60 + M - 45;

    if (time < 0)
    {
        time += 1440;
    }

    cout << time / 60 << " " << time % 60;
}