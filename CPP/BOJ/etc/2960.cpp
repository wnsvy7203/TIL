// Silver 4. Sieve of Eratosthenes

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N, K;

    cin >> N >> K;
    
    int cnt = 0;

    vector<int> visited(N+1, 0);

    for (int i = 2; i < N+1; i++)
    {
        if (visited[i])
            continue;
        else
        {
            for (int j = i; j <= N; j += i)
            {
                if (visited[j])
                    continue;
                else
                {
                    cnt++;
                    visited[j] = 1;
                    
                    if (cnt == K)
                    {
                        cout << j;
                        exit(0);
                    }
                }
            }
        }
    }
}