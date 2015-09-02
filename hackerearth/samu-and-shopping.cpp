#include<iostream>

using namespace std;

int main(){
   int t,n;
   cin >> t;
   while(t--){
    cin >> n;
    int ** array = new int*[n];
    for(int j=0;j<n;j++) array[j] = new int[3];
    for(int i=0;i<n;i++){
     for(int j=0;j<3;j++){
     cin >> array[i][j];
     
     }
    }
    int ** mem = new int*[n];
    for(int j=0;j<n;j++) mem[j] = new int[3];
    for(int j=0;j<3;j++) mem[0][j] = array[0][j];
    for(int i=1;i<n;i++) {
        for (int j = 0; j < 3; j++) {
            int minv = 0;
            for (int k = 0; k < 3; k++) {
                if (k == j) continue;
                int temp;
                temp = mem[i - 1][k] + array[i][j];
                if (minv > temp || minv == 0) minv = temp;
            }
            mem[i][j] = minv;


        }


    }
    int ans = (mem[n-1][0]> (mem[n-1][1]>mem[n-1][2] ? mem[n-1][2] : mem[n-1][1] ) ) ? mem[n-1][1] : mem[n-1][0];
    cout << ans << endl;

    


   }
   


    return 0;
}
