#include<stdio.h>
void main()
{
	int a,b,c,max,min;
	
	printf("\nEnter 3 number : ");
	scanf("%d %d %d",&a, &b,&c);
	
	if(a>b && a>c){
		max=a;
	}
	else if(b>c && b>c){
		max=b;
	}
	else{
		max=c;
	}
	
	if(a<b && a<c){
		min=a;
	}
	else if(b<a && b<c){
		min=b;
	}
	else{
		min=c;
	}
	
	printf("\nMax : %d",max);
	printf("\nMin : %d",min);
}
