#include<stdio.h>
void main(){
	float a;
	const float pi=3.14;
	printf("\n Enter the radius : ");
	scanf("%f",&a);
	
	printf("\nArea of circle :- %f",pi*a*a);
	getch();
}
