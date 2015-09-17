#include <iostream>


using namespace std;

int main() {
    int T;

    cin >> T;

    string word;
    cin >> word;

    int i=1;
    int check=0,count=0;
    while(i < word.length()){
        if (word[check] == word[i]){
            i++;
            count++;
        }
        else{
            check=i;
            i++;
        }

    }
    cout << count << endl;
}