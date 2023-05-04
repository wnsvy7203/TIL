// Bronze 2. 숫자의 개수

#include <iostream>
#include <string>

using namespace std;

int main()
{
    int A, B, C;

    int nums[10] = {};

    string str;

    cin >> A >> B >> C;

    str = to_string(A*B*C);

    for (int i = 0; i < str.length(); i++)
    {
        nums[str[i]-48]++;
    }

    for (int i = 0; i < 10; i++)
    {
        cout << nums[i] << "\n";
    }
}