#include<iostream>
#include<stdlib.h>
#include<memory.h>
using namespace std;

int main(){
    int scenario,bug,interactions;
    scanf("%d",&scenario);
    for(int i=0;i<scenario;i++){
    scanf("%d %d",&bug,&interactions);
    char bugs[bug+1];
    char cycle[] = {'m','f'};
    memset(&bugs[0],0,sizeof(bugs));
    int f,s;

    bool suspecious = false;

    while(interactions--){
       scanf("%d %d",&f,&s);
       if(bugs[f]==0 && bugs[s]==0){
            bugs[f]='m';
            bugs[s]='f';
       }
       else if (bugs[f]==bugs[s]){
            suspecious = true;
       }
       else if (bugs[f]=='m'){
            bugs[s] = 'f';
       }
       else if (bugs[f]=='f'){
           bugs[s]='m';
        }
       else if (bugs[f]==0){
            bugs[f] = bugs[s]=='m' ? 'f' :'m';
       }

    }
    printf("Scenario #%d:\n%s bugs found!\n",i,suspecious == true ? "Suspicious":"No suspicious");
    }


}
