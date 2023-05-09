// Bronze 3. Escape from Rectangle

#include <iostream>
#include <algorithm>

using namespace std;

int x, y, w, h;

int main()
{
    cin >> x >> y >> w >> h;

    int arr[4] = { x, y, w-x, h-y };

    int *min = min_element(arr, arr+4);

    cout << *min;
}