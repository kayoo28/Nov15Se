#include<stdio.h>
void main()
{
	char choice;
	
	printf("\nEnter R for Red");
	printf("\nEnter Y for Yellow");
	printf("\nEnter G for Green");
	
	printf("\n\nEnter you choice : ");
	scanf("%c",&choice);
	
	switch(choice){
		case 'R':
			printf("\nRed :- Stop");
		break;
		case 'Y':
			printf("\nYellow :- Ready");
		break;
		case 'G':
			printf("\nGreen :- Go");
		break;
		default:
			printf("\nInvalid Choice");
		break;
	}
}
