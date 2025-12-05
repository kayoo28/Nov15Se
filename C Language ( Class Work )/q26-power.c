#include<stdio.h>
void main()
{
	int num,n,pow=1,i;
	
	printf("\nEnter the Number : ");
	scanf("%d",&num);
	
	printf("\nEnter power : ");
	scanf("%d",&n);
	
	for(i=1; i<=n; i++){
		pow=pow*num;
	}
	
	printf("\nPower : %d",pow);
	
}
