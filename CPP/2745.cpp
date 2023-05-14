// Bronze 2. Arithmetic Conversion

#include <iostream>
#include <string>
#include <cmath>
#include <cctype>

using namespace std;

int main()
{
    string N;
    int B;
    
    cin >> N >> B;
    
    int sum = 0;
    
    for (int i = N.length()-1; i >= 0 ; i--)
    {
        if (isdigit(N[i]) == 0)
        {
            sum += ((N[i] - 55) * pow(B, i));
        }
        else
        {
            sum += ((N[i] - 48) * pow(B, i));
        }
    }
    
    cout << sum;
}