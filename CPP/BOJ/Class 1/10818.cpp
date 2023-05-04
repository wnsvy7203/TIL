// Bronze 5
// 최소, 최대

// 524ms

#include <iostream>
#include <algorithm>

using namespace std;

int N;
int arr[1000005];

int main()
{
    cin >> N;


    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];
    }

    sort(arr, arr+N);

    cout << arr[0] << " " << arr[N-1];
}