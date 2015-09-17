#include <iostream>
#include <set>
using namespace std;

int main() {
   string data;
    cin >> data;
    set<char> s;
    for( char a : data){
        s.insert(a);
    }
    if(s.size()%2 ==0 ){
        cout << "CHAT WITH HER!"<<endl;
    }
    else{
        cout << "IGNORE HIM!" <<endl;
    }


}