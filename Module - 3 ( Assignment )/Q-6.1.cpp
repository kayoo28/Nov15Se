#include<iostream>
using namespace std;
class Calculator
{
	public:
		int a,b;
		
		void getData()
		{
			cout<<"\nEnter 2 value : ";		cin>>a>>b;
		}
		void addition()
		{
			cout<<"\nAddition : "<<a+b;
		}
		void subtraction()
		{
			cout<<"\nSubtraction : "<<a-b;
		}
		void Multiplication()
		{
			cout<<"\nMultiplication : "<<a*b;
		}
		void Division()
		{
			cout<<"\nDivision : "<<(float)a/b;
		}
		void Modulo()
		{
			cout<<"\nModulo : "<<a%b;
		}
};
int main()
{
	Calculator c;
	c.getData();
	c.addition();
	c.subtraction();
	c.Multiplication();
	c.Division();
	c.Modulo();
	
	return 0;
}
