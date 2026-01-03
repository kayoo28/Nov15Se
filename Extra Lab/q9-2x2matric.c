#include<stdio.h>
void main()
{
	int i,j,A[2][2],B[2][2],C[2][2];
	
	printf("\nEnter the elements of A(2x2) matrix : ");
	for(i=0;i<2;i++){
		for(j=0;j<2;j++){
			scanf("%d",&B[i][j]);
		}
	}
	
	printf("\nEnter the elements of B(2x2) matrix : ");
	for(i=0;i<2;i++){
		for(j=0;j<2;j++){
			scanf("%d",&B[i][j]);
		}
	}
	
	for(i=0;i<2;i++){
		for(j=0;j<2;j++){
			C[i][j]=A[i][j]+B[i][j];
		}
		printf("\n");
	}
	
	for(i=0;i<2;i++){
		for(j=0;j<2;j++){
			printf("%d ",C[i][j]);
		}
		printf("\n");
	}
}
