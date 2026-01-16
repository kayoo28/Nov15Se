#include<iostream>
using namespace std;

int main()
{
	int a=5,b=3;
	
	cout<<"\nArithmetic Operation : ";
	cout<<"\nAddition : "<<a+b;
	cout<<"\nSubtraction : "<<a-b;
	cout<<"\nMultiplication : "<<a*b;
	cout<<"\nDivision : "<<(float)a/b;
	cout<<"\nModulo : "<<a%b;
	
	cout<<"\n\nRelational Operator : ";
	cout<<"\n "<<a<<" < "<<b<<" : "<<(a<b);
	cout<<"\n "<<a<<" > "<<b<<" : "<<(a>b);
	cout<<"\n "<<a<<" <= "<<b<<" : "<<(a<=b);
	cout<<"\n "<<a<<" >= "<<b<<" : "<<(a>=b);
	cout<<"\n "<<a<<" == "<<b<<" : "<<(a==b);
	cout<<"\n "<<a<<" != "<<b<<" : "<<(a!=b);
	
	cout<<"\n\nLogical Operation ";
	cout<<"\n("<<a<<" < "<<b<<") && ("<<a<<" > "<<b<<") : "<<((a<b)&&(a>b));
	cout<<"\n("<<a<<" < "<<b<<") || ("<<a<<" > "<<b<<") : "<<((a<b)||(a>b));
	cout<<"\n!(("<<a<<" < "<<b<<") && ("<<a<<" > "<<b<<")) : "<<!((a<b)&&(a>b));
	
	cout<<"\n\nBitwise Operator : ";
	cout<<"\n"<<a<<" & "<<b<<" : "<<(a&b);
	cout<<"\n"<<a<<" | "<<b<<" : "<<(a|b);
	cout<<"\n"<<a<<" >> "<<1<<" : "<<(a>>1);
	cout<<"\n"<<a<<" << "<<1<<" : "<<(a<<1);
}
