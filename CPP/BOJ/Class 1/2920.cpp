// Bronze 2. À½°è

#include <iostream>

using namespace std;

int main()
{
    int nums[8];

    for (int i = 0; i < 8; i++)
    {
        cin >> nums[i];
    }

    bool ascend = true;
    bool descend = true;

    for (int i = 0; i < 8; i++)
    {
        if (nums[i] != i+1)
        {
            ascend = false;
        }

        if (nums[i] != 8-i)
        {
            descend = false;
        }
    }

    if (ascend == true)
    {
        cout << "ascending";
    }
    else if (descend == true)
    {
        cout << "descending";
    }
    else
    {
        cout << "mixed";
    }
}