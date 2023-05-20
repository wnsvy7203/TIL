// Bronze 3. Fourth Dot

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> checkA;
    vector<int> checkB;

    for (int i = 0; i < 3; i++)
    {
        int A, B;

        cin >> A >> B;

        checkA.push_back(A);
        checkB.push_back(B);
    }

    int a(checkA[0]), b(checkB[0]);

    if (a == checkA[1] && a != checkA[2])
    {
        a = checkA[2];
    }
    else if (a != checkA[1] && a == checkA[2])
    {
        a = checkA[1];
    }

    if (b == checkB[1] && b != checkB[2])
    {
        b = checkB[2];
    }
    else if (b != checkB[1] && b == checkB[2])
    {
        b = checkB[1];
    }

    cout << a << " " << b;
}
