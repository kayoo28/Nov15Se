#include<iostream>
using namespace std;

int main()
{
	int a=5;
	float b=2.5;
	int c=2;
	
	cout<<"\nImplicit Type Conversion : "<<a*b;
	cout<<"\nBefore Explicit Type Conversion : "<<a/c;
	cout<<"\nAfter Explicit Type Converison : "<<(float)a/c;
}
