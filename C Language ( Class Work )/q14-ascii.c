#include<stdio.h>
void main()
{
	char c;
	int ascii;
	
	printf("\nEnter any character : ");
	scanf("%c",&c);
	
	ascii = c;
	
	if((ascii>=65 && ascii<=90) || (ascii>=97 && ascii <=122)){
		printf("\n%c is alphabet.",c);
	}
	else if(ascii>=48 && ascii<=57){
		printf("\n%c is digit.",c);
	}
	else if((ascii>=33 && ascii<=38) || ascii == 0){
		printf("\n%c is special Character",c);
	}
	else{
		printf("\nInvalid Input.");
	}
}
