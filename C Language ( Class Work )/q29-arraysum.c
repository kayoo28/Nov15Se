#include<stdio.h>
void main()
{
	int a[10],i,sum=0;
	
	printf("\nEnter the element of array : ");
	for(i=0; i<10; i++){
		scanf("%d",&a[i]);
	}
	
	for(i=0;i<10;i++){
		sum=sum+a[i];
	}
	printf("\nSum : %d",sum);
}
