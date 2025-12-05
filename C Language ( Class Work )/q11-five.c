#include<stdio.h>
void main()
{
	int num;
	
	printf("\nEnter the number : ");
	scanf("%d",&num);
	
	if(num%5 == 0){
		printf("\n%d is divisible by 5",num);
	}
	else{
		printf("\n%d is not divisble by 5",num);
	}
}
