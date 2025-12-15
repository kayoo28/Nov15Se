#include<stdio.h>
void main()
{
	int A[20],i,min,max;
	
	printf("\nEnter the elements of an Array : ");
	for(i=0;i<10;i++){
		scanf("%d",&A[i]);
	}
	
	min=A[0];
	max=A[0];
	
	for(i=0;i<10;i++){
		if(A[i]<=min){
			min=A[i];
		}
		if(A[i]>=max){
			max=A[i];
		}
	}
	
	printf("\nMinimum : %d",min);
	printf("\nMaximum : %d",max);
}
