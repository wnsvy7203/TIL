// Silver 4. Greeting Bright Gomgom
// 96ms

#include <iostream>
#include <string>
#include <set>

using namespace std;

int main()
{
    int N;

    cin >> N;

    int cnt = 0;

    set<string> gomgom;

    for (int i = 0; i < N; i++)
    {
        string str;

        cin >> str;

        if (str == "ENTER")
        {
            cnt += gomgom.size();
            gomgom.clear();
        }
        else
        {
            gomgom.insert(str);
        }
    }
    
    cnt += gomgom.size();

    cout << cnt;
}