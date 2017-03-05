#include<bits/stdc++.h>
#include<string>
#include<ctype.h>


using namespace std;


bool test_type_one(string t) {
    
    for(int i=1;i<t.length();i++) {
    
        if (! isupper(t[i]) ){
           return false; 
        } 
    }

    return true;

}

string switch_case(string t) {

    for(int i=0;i<t.length();i++) {
        if(isupper(t[i])) {
        t[i] = tolower(t[i]);
        }
        else {
        t[i] = toupper(t[i]);
        }
    }
    return t;
}

int main(){

    string t;
    cin >> t;
    if (test_type_one(t)) {
        cout << switch_case(t)<<endl;
    } else {
        cout << t << endl;
    }


}
