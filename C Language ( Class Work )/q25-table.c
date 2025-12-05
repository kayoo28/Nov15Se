#include<stdio.h>
void main()
{
	int num,i;
	
	printf("\nEnter Number : ");
	scanf("%d",&num);
	
	for(i=1; i<=10; i++){
		printf("%d * %d = %d\n",num,i,num*i);
	}
	getch();
}
