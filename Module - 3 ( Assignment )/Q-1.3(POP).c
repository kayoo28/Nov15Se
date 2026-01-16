#include<stdio.h>

int Rectangle(int l, int b)
{
	return l*b;
}
void main()
{
	int l,b;
	
	printf("\nEnter the length and breadth : ");
	scanf("%d %d",&l,&b);
	
	printf("\nArea of Rectangle : %d",Rectangle(l,b));
}
