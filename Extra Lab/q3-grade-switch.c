#include<stdio.h>
void main()
{
	int mark,grade;
	
	printf("\nEnter the mark : ");
	scanf("%d",&mark);
	
	grade=((mark>90)? 1 : (mark>75 && mark<=90)? 2 : (mark>50 && mark<=75)? 3 : 4);
	
	switch(grade)
	{
		case 1:
			printf("\nGrade A");
		break;
		
		case 2:
			printf("\nGrade B");
		break;
		
		case 3:
			printf("\nGrade C");
		break;
		
		case 4:
			printf("\nGrade D");
		break;
	}
}
