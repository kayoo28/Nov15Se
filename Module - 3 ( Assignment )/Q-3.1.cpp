#include<iostream>
using namespace std;
int main()
{
	int mark;
	
	cout<<"\nEnter the mark : ";	cin>>mark;
	
	if(mark>90) cout<<"\nGrade A";
	else if(mark>75 && mark<=90) cout<<"\nGrade B";
	else if(mark>60 && mark<=75) cout<<"\nGrade C";
	else if(mark>50 && mark<=60) cout<<"\nGrade D";
	else if(mark>40 && mark<=50) cout<<"\nGrade E";
	else cout<<"\nGrade F";
}
