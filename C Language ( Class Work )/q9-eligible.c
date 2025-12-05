#include<stdio.h>
void main()
{
	int age;
	
	printf("\nEnter the age : ");
	scanf("%d", &age);
	
	if(age>=18){
		printf("\nEligible for Vote");
	}
	else{
		printf("\nNot Eligible for Vote");
	}
}
