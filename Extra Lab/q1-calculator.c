#include<stdio.h>
void main()
{
	int num1,num2,choice;
	
	printf("\nEnter first number : ");
	scanf("%d",&num1);
	
	printf("\nEnter Second number : ");
	scanf("%d",&num2);
	
	printf("\n1 -> Addition");
	printf("\n2 -> Subtraction");
	printf("\n3 -> Multiplication :");
	printf("\n4 -> Division :");
	printf("\n5 -> Modulo : ");
	
	printf("\nEnter your choice : ");
	scanf("%d",&choice);
	
	switch(choice)
	{
		case 1:
			printf("\nAddition : %d",num1+num2);
		break;
		
		case 2:
			printf("\nSubtraction : %d",num1-num2);
		break;
		
		case 3:
			printf("\nMultiplication : %d",num1*num2);
		break;
		
		case 4:
			printf("\nDivision : %f",(float)num1/num2);
		break;
		
		case 5:
			printf("\nModulo : %d",num1%num2);
		break;
		
		default:
			printf("\nInvalid Choice!!!!!!!");
	}
}
