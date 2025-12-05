#include<stdio.h>
void main()
{
	int num;
	
	printf("\nEnter the number : ");
	scanf("%d",&num);
	
	if(num==0){
		printf("\n%d is zero",num);
	}
	else{
		printf("\n%d is non-zero",num);
	}
}
