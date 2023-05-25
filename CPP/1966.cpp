// Silver 3. Printer Queue

#include <iostream>
#include <vector>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int T;

    cin >> T;

    while (T--)
    {
        int N, M;

        cin >> N >> M;

        queue<vector<int>> doc;

        for (int i = 0; i < N; i++)
        {
            int add;
            cin >> add;

            vector<int> num(2, 0);
            num[0] = i;
            num[1] = add;

            doc.push(num);
        }

        int max = 9;

        int cnt = 1;

        while (1)
        {
            if (doc.front()[0] == max)
                doc.pop();
            else
            {
                vector<int> front = doc.front();
                doc.pop();
                doc.push(front);
            }

            max--;
        }
        


    }
}