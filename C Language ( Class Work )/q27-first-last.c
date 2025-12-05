#include<stdio.h>
void main()
{
	int num,rem=0,num2=0,sum=0;
	
	printf("\nEnter number : ");
	scanf("%d",&num);
	
	sum=num%10;
	
	while(num!=0){
		rem=num%10;
		num=num/10;
		num2=num2*10+rem;	
	}
	sum=sum + (num2%10);
	
	printf("\nSum of first & last digit : %d",sum);
}
