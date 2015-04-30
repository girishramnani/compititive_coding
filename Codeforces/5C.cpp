/*
 * =====================================================================================
 *
 *       Filename:  5C.cpp
 *
 *    Description:  girish
 *
 *        Version:  1.0
 *        Created:  Saturday 04 April 2015 05:18:25  IST
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */


#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <cassert>

using namespace std;

int main ( int argc, char *argv[] )
{
string s;
getline(cin,s);
const int n =s.length();

int arra[n][n] ={0};

for(int i=0;i<n;i++){
for(int j=i;j<n;j++){

if(arra[i][j] ==0 && s[j]==")"){
arra[i][j] =-1;
}
}
}


}

}

cout <<s<<endl;
	return 0;
}					/* ----------  end of function main  ---------- */
