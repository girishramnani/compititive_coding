
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
	int row,column;
	cin >>row >>column;
	int rowdone,columndone;
	vector<int> row_straw;
	vector<int> column_straw;
	for(int i=0;i<row ;i++){
		
	for(int j=0;j<column;j++){
	char temp;
	cin >>temp;
	if (temp =='S'){
	row_straw.push_back(i);
	column_straw.push_back(j);
}
	
}

}
	return 0;
}					/* ----------  end of function main  ---------- */
