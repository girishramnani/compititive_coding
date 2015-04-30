/*
 * =====================================================================================
 *
 *       Filename:  10A.cpp
 *
 *    Description:  my program
 *
 *        Version:  1.0
 *        Created:  Thursday 30 April 2015 02:56:43  IST
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
	int n,P1,P2,P3;
	vector<int> time;
	int T1,T2;
	cin >>n>>P1>>P2>>P3>>T1>>T2;
	int ans=0;
	int past_n=0;
	while(n--){
	int l1,r1;
	cin >>l1>>r1;
	ans+=P1*(r1-l1);
	if (past_n){

	// making this like a method call so that no parameters are needed to be passed
	int free_time = l1-past_n;
	while(free_time){
	if(free_time >(T2+T1)){
	ans+=P3*(free_time-(T2+T1));
	free_time =(T2+T1);

}
else if(free_time >T1){
ans+=P2*(free_time-T1);
free_time =T1;
}
else{
ans+=P1*free_time;
free_time =0;
}
}
		
}
past_n = r1;
}
					/* ----------  end of function main  ---------- */
cout << ans<<endl;	
}
