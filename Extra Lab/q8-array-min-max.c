#include<stdio.h>
void main()
{
	int a[10],min,max,i;
	
	printf("\nEnter 10 elements of array : ");
	for(i=0; i<10;i++){
		scanf("%d",&a[i]);
	}
	
	min=a[0];
	max=a[0];
	
	for(i=0; i<10; i++){
		if(a[i]<=min){
			min=a[i];
		}
		
		if(a[i]>=max){
			max=a[i];
		}
	}
	
	printf("\nMinimum : %d",min);
	printf("\nMaximum : %d",max);
}
