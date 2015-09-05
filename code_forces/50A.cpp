#include <iostream>

using namespace std;

int main() {
    int x,y;
    cin >> x >> y;
    int ans;
    ans = (x/2)*y;
    x=x%2;
    ans +=(y/2)*x;
    cout << ans;

}