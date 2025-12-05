#include<stdio.h>
void main()
{
	int a,b,c;
	
	printf("\nEnter the side of triangle : ");
	scanf("%d %d %d", &a,&b,&c);
	
	if(a+b>c && a+c>b && b+c>a){
		if(a==b || b==c){
			if(a==b && b==c && a==c){
				printf("\nEquilateral Triangle");
			}
			else{
				printf("\nIsosceles Triagnle");
			}
		}
		else{
			printf("\nScalene Triangle");
		}
	}
	else{
		printf("\nNot Valid triangle");
	}
	
	
}
