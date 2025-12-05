#include<stdio.h>
void main()
{
	int num;
	
	printf("\nEnter the number : ");
	scanf("%d",&num);
	
	if(num%3==0){
		if(num%5==0){
			printf("\n%d is divisible by 3 & 5",num);
		}
		else{
			printf("\n%d is not divisible by 3 & 5",num);
		}
	}
	else{
		printf("\n%d is not divisible by 3 & 5",num);
	}
}
