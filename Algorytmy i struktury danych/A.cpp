#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define ff first
#define ss second
using namespace std;

vector <pair <long long, long long> > v;
vector <long long> ans;
int n;
long long a, b, ans1;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cin >> n;
    for(int i = 0; i < n; i++)
    {
        cin >> a >> b;
        while(!(a % 2))
        {
            a /= 2;
            b *= 2;
        }
        v.pb(mp(a, b));
    }
    sort(v.begin(), v.end());
    ans.pb(v[0].ss);
    for(int i = 1; i < v.size(); i++)
    {
        if(v[i].ff == v[i - 1].ff)
            ans[ans.size() - 1] += v[i].ss;
        else
            ans.pb(v[i].ss);
    }
    for(auto it:ans)
    {
        ans1 += __builtin_popcountll(it);
    }
    cout << ans1 << endl;
}