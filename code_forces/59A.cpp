#include<bits/stdc++.h>
#include<string>
#include<ctype.h>


using namespace std;


bool test_type_one(string t) {
	
	int a=0;
    
    for(int i=0;i<t.length();i++) {
    
        if (isupper(t[i]) ){
           a++; 
        } 
    }
	int b = t.length()-a;
    if ( a <= b ){
    	return true;
    }
    return false;

}

string switch_case(string t, bool sw) {

    for(int i=0;i<t.length();i++) {
        if (sw) {
        t[i] = tolower(t[i]);
        } else {
        t[i] = toupper(t[i]);
        }
    }
    return t;
}

int main(){

    string t;
    cin >> t;
    
    cout << switch_case(t,test_type_one(t))<<endl;
    


}
