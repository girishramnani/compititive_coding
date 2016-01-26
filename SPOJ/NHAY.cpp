#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

void compute_lps(int * array,string word,int length){

    int count =0,rev=length-1;
    int i=1;

    while(i < length){
        if(word[i] == word[count]){

            count++;
            array[i]=count;
            i++;
        }
        else{
            if(count != 0){
                count = array[count-1];
            }
            else{
                 array[i] =0;
                i++;
            }
        }
    }


}

void search(){


}

int main() {

    int test=0;
    string main,pat;
    int M,N,len,count;
    while(scanf("%d",&test) != EOF){

    cin >> pat>>main;
    M = main.length();
    N = pat.length();

    len = pat.length();
    int array[len] = {0};
    compute_lps(array,pat,len);

    int i=0,j=0;

        count=0;

    while(i<M){
        if(pat[j] == main[i]){
            j++;
            i++;
        }
        if(j==N){
            cout<<i-N<<endl;
            j = array[j-1];
        }
        else if(i<M && pat[j] != main[i]){
            if(j!=0){
                j=array[j-1];
            }
            else {
                i=i+1;
            }
        }
    }
        cout <<endl;
    }




}