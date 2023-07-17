// Gold 5. Hide and Seek 3

#include <iostream>
#include <deque>

using namespace std;

int N, K;
int visited[100001];

int bfs()
{
    deque<int> deq;
    deq.push_back(N);
    visited[N] = 1;

    while(!deq.empty())
    {
        int tmp = deq.front();
        deq.pop_front();

        if (tmp == K)
            return visited[K]-1;

        if (tmp*2 < 100001 && !visited[tmp*2])
        {
            deq.push_front(tmp*2);
            visited[tmp*2] = visited[tmp];
        }

        if (tmp-1 >= 0 && !visited[tmp-1])
        {
            deq.push_back(tmp-1);
            visited[tmp-1] = visited[tmp]+1;
        }

        if (tmp+1 < 100001 && !visited[tmp+1])
        {
            deq.push_back(tmp+1);
            visited[tmp+1] = visited[tmp]+1;
        }
    }
}

int main()
{
    cin >> N >> K;
    cout << bfs();
}