#include <iostream>

using namespace std;

int main() {
    string data;
    int num;
    cin >> num;
    int ans=0;
    while(num--){
        cin >> data;

        if(data[0]=='+' || data[2]=='+'){
            ans++;
        }
        else{
            ans--;
        }

    }
    cout << ans<<endl;
}