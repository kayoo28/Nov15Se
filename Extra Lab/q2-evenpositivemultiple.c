#include<stdio.h>
void main()
{
	int num;
	
	printf("\nEnter the number : ");
	scanf("%d",&num);
	
	//Even or Odd
	if(num%2==0){
		printf("\n%d is even",num);
	}
	else{
		printf("\n%d is odd",num);
	}
	
	//Positive, Negative or Zero
	if(num>0){
		printf("\n%d is positive.",num);
	}
	else if(num<0){
		printf("\n%d is negative",num);
	}
	else{
		printf("\n%d is zero",num);
	}
	
	//Multiple of both 3 and 5
	if(num%3==0 && num%5==0){
		printf("\n%d is multiple of 3 & 5.",num);
	}
	else{
		printf("\n%d is not multiple of 3 & 5",num);
	}
	getch();
}
