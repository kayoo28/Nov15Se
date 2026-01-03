#include<stdio.h>
void main()
{
	int num,rem,sum=0,rev=0;
	
	printf("\nEnter the number : ");
	scanf("%d",&num);
	
	while(num!=0){
		rem=num%10;
		num=num/10;
		sum=sum+rem;
		rev=rev*10+rem;
	}
	
	printf("\nSum : %d",sum);
	printf("\nReverse : %d",rev);
}
