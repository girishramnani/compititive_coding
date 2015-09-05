#include <iostream>

using namespace std;

int main() {
    int a;
    string word;
    cin >>a;
    while(a--){
        cin >> word;
        if(word.length()>10){
            cout <<word[0]<<word.length()-2<<word.back()<<endl;
        }
        else {
            cout << word <<endl;
        }
    }
}