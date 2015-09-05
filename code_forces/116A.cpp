#include <iostream>

using namespace std;

int main() {
   int iteration;
   cin >> iteration;
   int entering,exiting;

   int total_capacity=0;
   int max_capacity = 0;
   while(iteration--){
      cin >> exiting>> entering;
      total_capacity -= exiting;
      total_capacity += entering;
      if(max_capacity < total_capacity){
         max_capacity = total_capacity;
      }

   }
   cout << max_capacity<<endl;
}