#include<stdio.h>
void main()
{
	int a[20],odd[20],i=0,j;
	
	printf("\nEnter the elements of an array : ");
	for(i=0; i<10; i++){
		scanf("%d",&a[i]);
	}
	j=0;
	for(i=0; i<10; i++){
		if((a[i]%2)!=0)
		{
			odd[j]=a[i];
			j++;
		}
	}
	
	for(i=0;i<j;i++){
		printf("%d\t",odd[i]);
	}
	
}
