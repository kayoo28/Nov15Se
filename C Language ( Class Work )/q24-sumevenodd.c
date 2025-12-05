#include<stdio.h>
void main()
{
	int even=0,odd=0,i;
	
	for(i=1; i<=10; i++){
		if(i%2==0){
			even=even+i;
		}
		else{
			odd=odd+i;
		}
	}
	
	printf("\nSum of even : %d",even);
	printf("\nSum of odd : %d",odd);
	
	getch();
}
