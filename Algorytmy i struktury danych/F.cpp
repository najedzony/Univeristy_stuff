#include <bits/stdc++.h>
#define ff first
#define ss second
using namespace std;

pair<int, pair<int, int> > t[1000005];
int n, m, a, b, c, ans = INT_MAX;
int repr[1000005];

int Find(int v)
{
    if(repr[v] == v)
        return v;
    repr[v] = Find(repr[v]);
    return repr[v];
}

void Union(int a, int b)
{
    int pom_a = Find(a);
    int pom_b = Find(b);
    repr[pom_a] = pom_b;
}

int main()
{
    cin >> n >> m;
    for(int i = 1; i <= m; i++)
    {
        cin >> t[i].ss.ff >> t[i].ss.ss >> t[i].ff;
        t[i].ff *= -1;
    }

    sort(t+1, t+m+1);
    
    for(int i = 1; i <= n; i++)
        repr[i] = i;

    for(int i = 1; i <= m; i++)
    {
        int pom1 = t[i].ss.ff;
        int pom2 = t[i].ss.ss;
        if(Find(pom1) != Find(pom2))
        {
            Union(pom1, pom2);
            ans = min(ans, t[i].ff * (-1));
        }
    }
    cout << ans << endl;
}