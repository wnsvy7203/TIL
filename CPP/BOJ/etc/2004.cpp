// Silver 2. Combination 0's count

#include <iostream>
#include <vector>

using namespace std;

int N, M;

pair<unsigned, unsigned> func(int n)
{
    unsigned two = 0;
    unsigned five = 0;

    for (long long i = 2; i <= n; i *= 2)
        two += n / i;
    
    for (long long i = 5; i <= n; i *= 5)
        five += n / i;
    
    return make_pair(two, five);
}

int main()
{
    cin >> N >> M;

    pair<unsigned, unsigned> res1 = func(N);
    pair<unsigned, unsigned> res2 = func(M);
    pair<unsigned, unsigned> res3 = func(N-M);

    cout << min(res1.first - res2.first - res3.first, res1.second - res2.second - res3.second);
}