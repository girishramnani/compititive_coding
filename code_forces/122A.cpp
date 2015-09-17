#include <iostream>

using namespace std;

int main() {
   int lucky_number[] = {4,7,47,77,444,474,477,447,744,747,774,777};
    int temp;
    cin >>temp;
    bool flag = true;
    for(int a : lucky_number){
        if(temp % a == 0) {
            cout << "YES" << endl;
            flag =false;
            break;
        }
    }
    if(flag) cout << "NO" <<endl;

}