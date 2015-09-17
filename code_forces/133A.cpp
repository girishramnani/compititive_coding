#include <iostream>
#include <set>

using namespace std;

int main() {
    char words[] = {'H','Q','9'};
    string word;
    cin >> word;
    set<char> setofchar;
    for(char a : word){
        setofchar.insert(a);
    }
    bool flag=true;
    for(char b : words){
        if(setofchar.find(b) !=setofchar.end()){
            cout << "YES";
            flag = false;
            break;
        }
    }
    if(flag) cout << "NO";

}