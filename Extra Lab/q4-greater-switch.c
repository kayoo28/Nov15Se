#include<stdio.h>
void main()
{
	int a,b,c,choice;
	
	printf("\nEnter 3 number : ");
	scanf("%d %d %d",&a, &b,&c);
	
	choice=((a>b && a>c)? 1:(b>a && b>c)?2:3);
	
	switch(choice)
	{
		case 1:
			printf("\n%d is greatest",a);
		break;
		
		case 2:
			printf("\n%d is greatest",b);
		break;
		
		case 3:
			printf("\n%d is greatest",c);
		break;
	}
}
