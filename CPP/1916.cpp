// Gold 5. Calculating the Least Cost

#include <iostream>
#include <vector>

using namespace std;

int N, M;
vector<pair<int, int>> dist[1001];

int main()
{
    cin >> N >> M;

    while (M--)
    {
        int u, v, w;

        cin >> u >> v >> w;

        dist[u].push_back(make_pair(v, w));
    }


}