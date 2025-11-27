#include<stdio.h>
void main()
{
	int p,r,n;
	printf("\n Enter the principal : ");
	scanf("%d",&p);
	
	printf("\n Enter the rate : ");
	scanf("%d",&r);
	
	printf("\n Enter the time : ");
	scanf("%d",&n);
	
	printf("\nSimple Interest  :  %f",(float)(p*r*n)/100);
	getch();
}
