#include<iostream>
using namespace std;
void calculator(int a, int b)
{
	cout<<"\nAddition : "<<a+b;
	cout<<"\nSubtraction : "<<a-b;
	cout<<"\nMultiplication : "<<a*b;
	cout<<"\nDivision : "<<(float)a/b;
	cout<<"\nModulo : "<<a%b;
}
int main()
{
	int a,b;
	
	cout<<"\nEnter value of a & b : ";		cin>>a>>b;
	calculator(a,b);
	return 0;
}
