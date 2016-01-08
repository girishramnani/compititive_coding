#include <iostream>

using namespace std;

int main() {
    int iter,n,m,d;
    cin >> iter ;
    
    int health;

    
    while (iter--){

        int count=0,mul,rem;
        cin >> n >> m >> d;
        while(n--) {
        cin >> health;
        rem = health % d;

        mul = health / d;
        if (rem ==0){
        if (mul > 0){
            mul--;
        }
        }
        count+=mul;

        }
        if ( count >= m){
        cout << "YES" << endl;
        }
        else{
        cout << "NO" << endl;
        }



    }



}
