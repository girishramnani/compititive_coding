#include <iostream>

using namespace std;

int main() {
    int a,b,intput,test2,test1=0,ans;

    cin >> a >> b;
    ans = b;
    int temp = b+1;



    for(int i=1;i<=a;i++){
       cin >> intput ;
        if (intput>0){
            test1 = i;
        }
        if (i == b){
            test2 = intput;
        }
        else if (i > b){
            if(test2 == intput){
                ans =i;
            }
        }
    }

    if(test2 != 0) {
        cout <<ans;
    }
    else{
        cout << test1;
    }



    return 0;
}