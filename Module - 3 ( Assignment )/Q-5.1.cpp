#include<iostream>
using namespace std;
int main()
{
	int A[10];
	int sum=0,i;
	
	cout<<"\nEnter the elements of Array : ";
	
	for(i=0; i<10; i++)
	{
		cin>>A[i];
		sum=sum+A[i];
	}
	
	cout<<"\nAverage : "<<(float)sum/(10);
}
