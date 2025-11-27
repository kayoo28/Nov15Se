#include<stdio.h>
void main()
{
	int a,b;
	
	printf("\nEnter values of a & b : ");
	scanf("%d %d",&a,&b);
	
	printf("\nAddition : %d",a+b);
	printf("\nMultiplication : %d",a*b);
	printf("\nSubtraction : %d",a-b);
	printf("\nDivision : %f",(float)a/b);
	printf("\nModulos : %d",a%b);
	getch();
}
