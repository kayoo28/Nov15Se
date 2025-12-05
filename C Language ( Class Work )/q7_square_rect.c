#include<stdio.h>
void main(){
	int a,b,l;
	printf("\n Enter the length of a side of square : ");
	scanf("%d",&a);
	
	printf("\n Enter the length of a side of rectangle : ");
	scanf("%d %d",&l,&b);
	
	printf("\nArea of Square :- %d",a*a);
	printf("\nArea of Rectangle :- %d",l*b);
	getch();
}
