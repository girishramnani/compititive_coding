/*
 * =====================================================================================
 *
 *       Filename:  527A.cpp
 *
 *    Description:  my program
 *
 *        Version:  1.0
 *        Created:  Thursday 30 April 2015 11:16:23  IST
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
	long long a,b;
	cin >>a>>b;
	long long count =0;
	while(a>0 &&  b>0 ){
	if(a>b ){
	 count+=(a/b);
	a=a%b;
	}
	else{
	count+=(b/a);
	b=b%a;
	}
}
cout << count <<endl;

	return 0;
}					/* ----------  end of function main  ---------- */

