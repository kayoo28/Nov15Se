#include<stdio.h>
void main()
{
	int a,b;
	
	printf("\nEnter two number a & b : ");
	scanf("%d %d",&a,&b);
	
	if(a>b){
		printf("\n%d is greater",a);
	}
	else if(b>a){
		printf("\n%d is greater",b);
	}
	else{
		printf("\n%d and %d is equal",a,b);
	}
}
