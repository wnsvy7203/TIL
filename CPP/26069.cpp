// Silver 4. Friendly ChongChong

#include <iostream>
#include <set>

using namespace std;

int main()
{
    int N;

    cin >> N;

    set<string> dance;

    int idx = 0;

    for (int i = 0; i < N; i++)
    {
        string A, B;

        cin >> A >> B;

        if (A == "ChongChong" || B == "ChongChong")
            idx = i;
            dance.insert(A, B);
        
        if (i > idx)
        {
            
        }
    }

    cout << dance.size();
}