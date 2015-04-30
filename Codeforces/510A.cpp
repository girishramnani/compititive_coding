/*
 * =====================================================================================
 *
 *       Filename:  510A.cpp
 *
 *    Description:  my program
 *
 *        Version:  1.0
 *        Created:  Thursday 30 April 2015 03:38:53  IST
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
	int r,c;
	cin >>r>>c;	
for(int i=1;i<=r;i++){
	if(i&1){
	string temp =string(c,'#');
	cout << temp<<endl;
}
else if(i%4==0){
cout <<'#'<< string(c-1,'.')<<endl;
}
else{

cout <<string(c-1,'.')<<'#'<<endl;
}
}
	return 0;
}					/* ----------  end of function main  ---------- */

