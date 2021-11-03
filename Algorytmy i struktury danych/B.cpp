#include <bits/stdc++.h>
#define ff first
#define ss second
using namespace std;
int n, a, sum;
int if_can[1000005];
int pom[1000005];
int klo[2005];
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cin >> n;
    for(int i = 1; i <= n; i++)
    {
        cin >> klo[i];
    }
    sort(klo+1, klo+n+1);
    for(int i = 1; i <= n; i++)
    {
        sum+=klo[i];
        for(int j = 0; j <= sum; j++)
        {
            if(if_can[j])
            {
                if(j - klo[i] >= 0)
                {
                    pom[j-klo[i]] = max(pom[j-klo[i]], if_can[j]);
                }
                else
                {
                    pom[abs(j-klo[i])] = max(pom[abs(j-klo[i])], if_can[j] + klo[i] - j);
                }
                pom[j + klo[i]] = max(pom[j + klo[i]], if_can[j] + klo[i]);
            }
        }
        pom[klo[i]] = max(pom[klo[i]], klo[i]);
        for(int j = 0; j <= sum; j++)
        {
            if_can[j] = max(if_can[j], pom[j]);
            pom[j] = 0;
        }
    }
    if(if_can[0])
    {
        cout << "TAK" << endl;
        cout << if_can[0] << endl;
    }    
    else
    {
        for(int i = 1; i <= sum; i++)
            if(if_can[i] && if_can[i] != i)
            {
                cout << "NIE" << endl;
                cout << i << endl;
                return 0;
            }
    }
}