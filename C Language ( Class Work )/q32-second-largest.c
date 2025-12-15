#include<stdio.h>
void main()
{
	int A[20],i,min,max,secondLargest;
	
	printf("\nEnter the elements of an Array : ");
	for(i=0;i<10;i++){
		scanf("%d",&A[i]);
	}
	
	min=A[0];
	max=A[0];
	
	
	for(i=0;i<10;i++){
		if(A[i]<=min) min=A[i];
		if(A[i]>=max) max=A[i];
	}
	
	if(min == max){
        printf("\nSecond Largest does not exist");
        return;
    }
	secondLargest=min;
	
	for(i=0;i<10;i++){
		if(A[i]>=secondLargest && A[i]<max){
			secondLargest = A[i];
		}
	}
	
	printf("\nSecond Largest : %d",secondLargest);
}
