#include<iostream>
using namespace std;
int main()
{
	int i,j;
	int n;
	
	cout<<"\nEnter the number : ";	cin>>n;
	
	for(i=1; i<=n; i++)
	{
		for(j=1; j<=n; j++)
		{
			if(i==n || j==1 || (i==j))
			{
				printf("* ");
			}
			else
			{
				cout<<"  ";
			}
		}
		cout<<"\n";
	}
	return 0;
}
