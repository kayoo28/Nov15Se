#include<stdio.h>
void main()
{
	int year;
	
	printf("\nEnter the year : ");
	scanf("%d",&year);
	
	if((year%400==0) || (year%4==0 && year%100!=0)){
		printf("\n%d is leap Year",year);
	}
	else{
		printf("\n%d is not a leap Year",year);
	}
}
