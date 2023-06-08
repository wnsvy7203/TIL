// Bronze 2. »ó¼ö

#include <iostream>
#include <string>

using namespace std;

int main()
{
    string A, B;

    cin >> A >> B;

    string a, b;

    for (int i = 0; i < 3; i++)
    {
        a += A[2-i];
        b += B[2-i];
    }

    if (stoi(a) > stoi(b))
    {
        cout << a;
    }
    else
    {
        cout << b;
    }
}