#include<stdio.h>
void main()
{
	int min,num,rem;
	
	printf("\nEnter the number : ");
	scanf("%d",&num);
	
	min=num%10;
	
	while(num!=0){
		rem=num%10;
		if(rem<=min){
			min=rem;
		}
		num=num/10;
	}
	
	printf("\nMinimum : %d",min);
}
