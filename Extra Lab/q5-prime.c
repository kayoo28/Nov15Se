#include<stdio.h>
void main()
{
	int num,flag=0,i;
	printf("\nEnter the number : ");
	scanf("%d",&num);
	
	for(i=2; i<num; i++){
		if(num%i==0){
			flag=1;
			break;
		}
	}
	
	if(flag==0){
		printf("\n%d is prime number.",num);
	}
	else{
		printf("\n%d is not prime number.",num);
	}
}
