/*
 * =====================================================================================
 *
 *       Filename:  test.cpp
 *
 *    Description:  my program
 *
 *        Version:  1.0
 *        Created:  07/10/2015 08:52:51 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */

#include <stdio.h>

int main ( int argc, char *argv[] )
{
    int i =10;
    float j =1000.0;
    char* x =(char *) &j;
    printf("%d %d",x[0],x[8]);
       
    return 0;
}					/* ----------  end of function main  ---------- */

