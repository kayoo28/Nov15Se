#include<iostream>
using namespace std;
int main()
{
	int n,i;
	
	cout<<"\nEnter the number : ";		cin>>n;
	
	for(i=1; i<=10; i++)
	{
		cout<<"\n"<<n<<" * "<<i<<" : "<<n*i;
	}
}
