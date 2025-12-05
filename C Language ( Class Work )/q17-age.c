#include<stdio.h>
void main()
{
	int age;
	
	printf("\nEnter the age : ");
	scanf("%d",&age);
	
	if(age>=1 && age<=12){
		printf("\n%d year old person is Child",age);
	}
	else if(age>=13 && age<=19){
		printf("\n%d year old person is Teenager",age);
	}
	else if(age>20 && age<=50){
		printf("\n%d year old person is Adult",age);
	}
	else if(age>=51){
		printf("\n%d year old person is Senior",age);
	}
	else{
		printf("\nInvalid age!!!!");
	}
}
