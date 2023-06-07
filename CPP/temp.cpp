#include <iostream>
#include <string>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    string str;
    
    while (1)
    {
        getline(cin, str);
        
        if (str == "#")
            return 0;
        
        int cnt = 0;
        
        for (int i = 0; i < str.length(); i++)
        {
            switch(str[i])
            {
                case 'a':
                    cnt++;
                    break;
                case 'e':
                    cnt++;
                    break;
                case 'i':
                    cnt++;
                    break;
                case 'o':
                    cnt++;
                    break;
                case 'u':
                    cnt++;
                    break;
                case 'A':
                    cnt++;
                    break;
                case 'E':
                    cnt++;
                    break;
                case 'I':
                    cnt++;
                    break;
                case 'O':
                    cnt++;
                    break;
                case 'U':
                    cnt++;
                    break;
            }
        }
        
        cout << cnt << '\n';
    }
}