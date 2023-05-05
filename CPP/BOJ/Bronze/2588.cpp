// Bronze 3. Multiplication

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int N, M;
    
    cin >> N >> M;
    
    cout << N * (M % 10) << "\n";
    cout << N * (M % 100 / 10) << "\n";
    cout << N * (M / 100) << "\n";
    cout << N * M;
}