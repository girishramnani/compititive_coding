#include <iostream>

using namespace std;

bool check_for_seven(string data,int a){
    int count =0;
    for(int i=0;i<data.length();i++){
        if((data[i]-'0')==a){
            count++;
            if(count==7){
                return true;
            }
        }
        else{
            count=0;
        }
    }
    return false;
}

int main() {
    string data;
    cin >> data;

    string d = (check_for_seven(data,1) || check_for_seven(data,0)) ? "YES" : "NO";
    cout << d;

}