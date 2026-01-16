#include<iostream>
using namespace std;

int main()
{
	int A[2][2],B[2][2],C[2][2];
	int i,j;
	
	cout<<"\nEnter element of Array (A) : ";
	for(i=0; i<2; i++)
	{
		for(j=0; j<2; j++)
		{
			cin>>A[i][j];
		}
	}
	
	cout<<"\nEnter element of Array (B) : ";
	for(i=0; i<2; i++)
	{
		for(j=0; j<2; j++)
		{
			cin>>B[i][j];
		}
	}
	
	for(i=0; i<2; i++)
	{
		for(j=0; j<2; j++)
		{
			C[i][j]=A[i][j]+B[i][j];
			cout<<"\t"<<C[i][j];
		}
		cout<<"\n";
	}
	return 0;
}
