#include<stdio.h>
void prime(int x){
	
	int j,count=0;
	for(j=2; j<x; j++){
		if(x%j==0){
			count++;
		}
	}
	
	if(count==0){
		printf("%d \t",x);
	}
}
void main()
{
	int num,i;
	
	printf("\nEnter the number :");
	scanf("%d",&num);
	
	for(i=1; i<=num; i++){
		prime(i);
	}
}
