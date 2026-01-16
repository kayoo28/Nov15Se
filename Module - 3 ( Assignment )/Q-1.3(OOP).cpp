#include<iostream>
using namespace std;
class Rectangle
{
	public:
		int l,b;
		
		void getInfo()
		{
			cout<<"\nEnter the length and breadth : ";	cin>>l>>b;
		}
		
		void showInfo()
		{
			cout<<"\nArea of Rectangle : "<<l*b;
		}
};
int main()
{
	Rectangle r;
	r.getInfo();
	r.showInfo();
	return 0;
}
