#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

int max(int a, int b)
{   return (a > b)? a : b; }

int lst(string word){
  
  int length = word.length();
  string rev(word);
  reverse(rev.begin(),rev.end());
  cout << rev << endl;
  cout << word.length() <<endl;
  int memo[length+1][length+1]={0};
  int i,j;
  i=1;
  j=1;
  for(;i<=length;i++){

    for(;j<=length;j++){
      if(word[i-1]==rev[j-1]){
	cout << word[i-1] << " " << rev[j-1] <<endl;
	memo[i][j] = memo[i-1][j-1]+1;
      }
      else{
	memo[i][j] = max(memo[i-1][j],memo[i][j-1]);
 
      }
      cout << memo[i][j] <<endl;

    }
  }
  cout << memo[length][length] <<endl;
  return length - memo[length][length];
  
}



int main(){

  int iterations;
  cin >> iterations;
  while(iterations--){
    string word;
    cin >> word;
    cout << lst(word) <<endl;
  }

  return 0;

}
