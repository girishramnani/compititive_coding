/*
 * =====================================================================================
 *
 *       Filename:  479A.cpp
 *
 *    Description:  my program
 *
 *        Version:  1.0
 *        Created:  Thursday 30 April 2015 01:52:51  IST
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
	vector<int> ans;
	int a,b,c;
	cin >>a;
	cin >>b;
	cin >>c;
	ans.push_back(a+b+c);
	ans.push_back((a*b)+c);
	ans.push_back(a*b*c);
	ans.push_back(a+(b*c));
	ans.push_back((a+b)*c);
	ans.push_back(a*(b+c));
	auto max =ans[0];
	for(auto &i:ans){
	if (i > max){
	max = i;
	}
	}
	cout << max;

	return 0;
}					/* ----------  end of function main  ---------- */

