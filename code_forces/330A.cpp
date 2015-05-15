
#include<iostream>
#include<vector>
using namespace std;

int main ( int argc, char *argv[] )
{
	int row,column;
	cin >>row >>column;
	int rowdone,columndone;
	rowdone =0;
	columndone =0;
	vector<int> row_straw;
	vector<int> column_straw;
	int sum=0;
	for(int i=0;i<row ;i++){
		
	for(int j=0;j<column;j++){
	char temp;
	cin >>temp;
	if (temp =='S'){
	row_straw.push_back(i);
	column_straw.push_back(j);
	
}
	
}
if(row_straw.size()==0){
row_straw.push_back(-1);
column_straw.push_back(-1);
}

}
	int a=0;
	for(int i=0;i<row;i++){
	a =row_straw.front();
	cout << "a " <<a<<endl;
	if(i!=a){
	cout << "i " <<i <<" a "<<a<<endl;
	sum+=(column-columndone);
	rowdone++;
	cout <<sum <<endl; 
	}
	else{
	row_straw.erase (row_straw.begin());
}
}
	a =-1;
	for(int i=0;i<column;i++){
	a =column_straw.front();
	if(i!=a){
	sum+=(row-rowdone);
	columndone++;
	}
	else{
	column_straw.erase (column_straw.begin());
}
}
	cout << sum <<endl;
	
	return 0;
}					/* ----------  end of function main  ---------- */
