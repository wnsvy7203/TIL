// Silver 4. Friendly ChongChong

#include <iostream>
#include <set>

using namespace std;

int main()
{
    int N;

    cin >> N;

    set<string> dance;

    dance.insert("ChongChong");

    int idx = 0;

    for (int i = 0; i < N; i++)
    {
        string A, B;

        cin >> A >> B;

        if (dance.find(A) != dance.end())
        {
            dance.insert(B);
        }
        else if (dance.find(B) != dance.end())
        {
            dance.insert(A);
        }
    }

    cout << dance.size();
}