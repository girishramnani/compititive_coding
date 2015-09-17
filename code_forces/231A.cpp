#include <iostream>

using namespace std;

int main() {
   int iteration;
    cin >> iteration;
    int count=0;
    int petya,vasya,tonya,temp;
    while(iteration--){
        temp=0;
        cin >> petya>>vasya>>tonya;
        if(petya) temp++;
        if(vasya) temp++;
        if(tonya) temp++;
        if(temp>=2) count++;

    }
    cout << count<<endl;
}