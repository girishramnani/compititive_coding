#include <stdio.h>      /* printf */
#include <stdlib.h>     /* qsort */
#include <algorithm>

int values[] = { 40, 10, 100, 90, 20, 25 };

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}
int main(){

	int test,k,n;
	long heights[20000],min;
	
	scanf("%d",&test);
	
	while(test--){
		
		scanf("%d %d",&k,&n);
		for(int i=0;i<k;i++){
		
			scanf("%ld",&heights[i]);
		}
		std::sort(heights,heights+k);
		min = 1000000000;
		for(int i=0;i<=k-n;i++){
			if(heights[i+n-1]-heights[i] < min ){
			min = heights[i+n-1]-heights[i];
			}
			
			}
		
		
		
		
		printf("%ld \n",min);
		
	
	}

}
