#include <iostream>

using namespace std;

int main()
{
    int arr[10];

    for (int i = 0; i < 9; i++)
    {
        cin >> arr[i];
    }
    
    int num = arr[0];
    int order = 1;

    for (int i = 1; i < 9; i++)
    {
        if (num < arr[i])
        {
            num = arr[i];
            order = i + 1;
        }
    }

    cout << num << "\n" << order;
}