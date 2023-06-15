// Silver 4. Algorithm Class - Merge Sort 1

#include <iostream>
#include <vector>

using namespace std;

int N, K;
int cnt;
bool flag = 0;
int A[500001] = {0, };
int temp[500001] = {0, };

void merge(int A[], int p, int q, int r)
{
    int i = p;
    int j = q+1;
    int t = 1;

    while (i <= q && j <= r)
    {
        if (A[i] <= A[j])
            temp[t++] = A[i++];
        else
            temp[t++] = A[j++];
    }
    while (i <= q)
        temp[t++] = A[i++];
    while (j <= r)
        temp[t++] = A[j++];
    
    i = p;
    t = 1;

    while (i <= r)
    {
        A[i++] = temp[t++];
        cnt++;

        if (cnt == K)
        {
            cout << A[i-1];
            flag = 1;
            return;
        }
    }
}

void merge_sort(int A[], int p, int r)
{
    if (p < r)
    {
        int q = (p+r) / 2;
        merge_sort(A, p, q);
        merge_sort(A, q+1, r);
        merge(A, p, q, r);
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> K;

    for (int i = 0; i < N; i++)
        cin >> A[i];

    merge_sort(A, 0, N-1);
    if (!flag)
        cout << -1;
}