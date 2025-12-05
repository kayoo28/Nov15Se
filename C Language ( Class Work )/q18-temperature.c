#include<stdio.h>
void main()
{
	int temp;
	
	printf("\nEnter the temperature : ");
	scanf("%d",&temp);
	
	if(temp<=10){
		printf("\nCold");
	}
	else if(temp>=11 && temp<=30){
		printf("\nWarm");
	}
	else if(temp>=31 && temp<=45){
		printf("\nHot");
	}
	else{
		printf("\nVery-Hot");
	}
}
