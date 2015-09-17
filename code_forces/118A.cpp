#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

int main() {
   string word;

   cin >> word;
    set<char> data = {'a','e','i','o','u'};
    int i=0;
    transform(word.begin(), word.end(),word.begin() ,::tolower);
    while(i < word.length()){

        if(data.find(word[i]) != data.end()){
            word.erase(i,1);
            i--;
        }
        else{
            word.insert(i,".");
            i++;
        }
        i++;
    }


    cout << word<<endl;

}