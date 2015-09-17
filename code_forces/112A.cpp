#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {





    std::string data ;
    cin >> data;
    std::transform(data.begin(), data.end(), data.begin(), ::tolower);
    std::string data2 ;
    cin >> data2;
    std::transform(data2.begin(), data2.end(), data2.begin(), ::tolower);


    int a = data.compare(data2);
    if(a < 0){
        cout << -1;
    }
    else if (a ==0){
        cout << 0 ;
    }
    else {
        cout << 1;
    }


}