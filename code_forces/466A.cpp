#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int n,m,a,b;
    cin >> n >> m >> a >> b ;
    long sum=0,temp=0;
    int opt,mul;
    float div = (b)/(float)m;
    if(div > a){
        opt=1;
        mul=a;
    }
    else {
        opt=m;
        mul=b;
    }
    sum+=((n/opt)*mul);
    temp =(ceil(n/(float)opt)*mul);

    sum+=((n%opt)*a);
    long ans =sum < temp ? sum : temp;
    cout << ans  << endl;


}