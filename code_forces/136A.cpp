#include <iostream>

using namespace std;

int main() {
    int no;
    cin >> no;

    int array[no+1] ={0};

    for(int i=0;i<no;i++){
        int temp;
        cin >> temp;
        array[temp] = i+1;

    }

    for(int a=1;a<no+1;a++){
        cout << array[a] << " ";
    }

}