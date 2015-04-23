#include<iostream>
#include<cmath>
using namespace std;

int determinant(int b[101][101],int m)  
{
 int i,j,sum = 0,c[101][101];
 if(m==2)
  {                                        //BASE CONDITION
	sum = b[0][0]*b[1][1] - b[0][1]*b[1][0];
	return sum;
  }
 for(int p=0;p<m;p++)
 {
  int h = 0,k = 0;
  for(i=1;i<m;i++)
  {
	for( j=0;j<m;j++)
	{
	 if(j==p)
	  continue;
	 c[h][k] = b[i][j];
	 k++;
	 if(k == m-1)
	  {
		 h++;
		 k = 0;
	  }

	}
  }

  sum = sum + b[0][p]*pow(-1,p)*determinant(c,m-1);
 }
 return sum;
}

int main(int argc, char const *argv[])
{
	int size ;
	cin >> size;

	int matrix[101][101]={0};
	for(int i=0;i<size;i++){
		for(int j=0;j<size;j++){
			cin >> matrix[i][j]; 
		}
	}
	int a = determinant(matrix,size);
	if (a == 0){
		cout <<"YES";
	}
	else{
		cout <<"NO";
	}
	return 0;
}

