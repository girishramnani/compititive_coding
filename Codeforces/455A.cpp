/*
 * =====================================================================================
 *
 *       Filename:  455A.cpp
 *
 *    Description:  my program
 *
 *        Version:  1.0
 *        Created:  Thursday 30 April 2015 11:36:38  IST
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
	int num;
	vector<int> vec;
	long arr[100000]={0};
	cin >> num;
	while(num--){
	long temp;
	cin >>temp;
	arr[temp]++;
}	
	long long  ans[100000]={0};
	ans[1]=arr[1];
	long long max=ans[1];
	for(int i=2;i<100000;i++){
	ans[i]= ans[i-1] >(arr[i]*i+ans[i-2]) ? ans[i-1] : (arr[i]*i+ans[i-2]); 
	if(ans[i] > max){
	max = ans[i];
}
}
	cout << max<<endl;
	return 0;
}					/* ----------  end of function main  ---------- */

