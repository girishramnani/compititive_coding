#include<iostream>

using namespace std;

long long * find_all_fib(){

    static long long answer[50] = {0};
    answer[0] = 0L;
    answer[1] = 1L;
    
    for(int i=2;i<50;i++){

        answer[i] = answer[i-1]+answer[i-2];

    }
    return answer;

}

int main(){
    long iters;
    cin >> iters;
    long long * ans = find_all_fib();
    long num;
    while(iters--){

    cin >> num;
    
    cout << ans[num+2] << endl;

    }

}
