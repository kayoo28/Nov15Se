#include<iostream>
using namespace std;

class BankAccount
{
	private:
		int balance=10000;
		int amount;
	
	public:
		void withDraw()
		{
			cout<<"\nEnter the amount to withdraw : ";		cin>>amount;
			
			if(amount<=balance)
			{
				cout<<"\nWithdraw Successfull!!!!!";
			}
			else
			{
				cout<<"\nInsufficient Balance";
			}
			
		}
		void deposit()
		{
			cout<<"\nEnter the amount to Deposit : ";		cin>>amount;
			
			balance = balance + amount;
			cout<<"\nDeposit Successfully";
			
		}
};
int main()
{
	BankAccount a;
	a.deposit();
	a.withDraw();
	return 0;
}

