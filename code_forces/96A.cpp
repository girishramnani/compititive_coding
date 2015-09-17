#include <bits/stdc++.h>
using namespace std;
bool comp(int a,int b)
{
    return (a>b);
}
int gcd(long long int a,long long int b)
{
    if(b==0)
        return a;
    else
        return gcd(b,a%b);
}
int main(void) {
    int n,m;
    cin>>n>>m;
    int a,i,j;
    bool b[1001]={0},t[1001];
    for(i=0;i<n;++i)
    {
        cin>>a;
        a=a%m;
        for(j=0;j<m;++j)
            t[j]=b[j];
        for(j=0;j<m;++j)
        {
            if(t[j])
                b[(j+a)%m]=1;
        }
        b[a]=1;
        if(b[0])
        {
            cout<<"YES";
            return 0;
        }
    }
    cout<<"NO";
    return 0;
}