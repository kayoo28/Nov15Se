#include<stdio.h>
void main()
{
	int mark;
	
	printf("\nEnter the mark : ");
	scanf("%d",&mark);
	
	if(mark>90){
		printf("\nGrade A");
	}
	else if(mark>75 && mark<=90){
		printf("\nGrade B");
	}
	else if(mark>50 && mark<=75){
		printf("\nGrade C");
	}
	else{
		printf("\nGrade D");
	}
}
