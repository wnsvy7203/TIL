// Silver 3. Printer Queue

#include <iostream>
#include <vector>
#include <queue>
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

        queue<pair<int, int>> docx;
        vector<pair<int, int>> doc;

        for (int i = 0; i < N; i++)
        {
            int add;
            cin >> add;

            pair<int, int> num;
            num.first = add;
            num.second = i;

            docx.push(num);
            doc.push_back(num);
        }

        sort(doc.begin(), doc.end(), greater<>());

        int cnt = 0;

        while (1)
        {
            if (doc[0].first == docx.front().first)
            {
                cnt++;
                if (docx.front().second == M)
                {
                    cout << cnt << '\n';
                    break;
                }
                else
                    docx.pop();
            }
            else
            {
                pair<int, int> temp;

                temp = docx.front();

                docx.pop();
                docx.push(temp);
            }
        }
    }
}