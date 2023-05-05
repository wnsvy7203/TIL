// Bronze 3. Oven Watch

#include <iostream>

using namespace std;

int main()
{
    int H, M;
    int time;

    cin >> H >> M >> time;

    int temp = H * 60 + M + time;

    if (temp >= 1440)
    {
        temp -= 1440;
    }

    cout << temp / 60 << " " << temp % 60;
}