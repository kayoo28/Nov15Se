#include <iostream>
#include <ctime>
#include <string>
using namespace std;

class ATM {
	private:
    	int atmPin;
    	double initialBalance;
    	double currentBalance;
    	int pinAttempts;
    
	public:
    	ATM() 
		{
        	atmPin = 12345;
        	initialBalance = 60000.0;
        	currentBalance = 20000.0;
        	pinAttempts = 0;
    	}
    
    	void displayDateTime()
    	{
    		time_t now = time(0);
    		char* dt = ctime(&now);
    		cout << "\n\t\tCurrent Date & Time: " << dt;
		}
    
    	void displayWelcomeScreen()
    	{
    		cout << "\n\n";
    		cout << "\t\t========================================\n";
    		cout << "\t\t     WELCOME TO ATM BANKING SYSTEM     \n";
    		cout << "\t\t========================================\n";
    		displayDateTime();
    		cout << "\n\t\t========================================\n\n";
		}
    
    void displayHelpScreen()
    {
    	cout << "\n\n";
    	cout << "\t\t========================================\n";
    	cout << "\t\t          ATM HELP SCREEN              \n";
    	cout << "\t\t========================================\n";
    	cout << "\n\t\tHow to use ATM:\n";
    	cout << "\t\t1. Enter your ATM PIN (Default: 12345)\n";
    	cout << "\t\t2. Select transaction type:\n";
    	cout << "\t\t   - Deposit Money\n";
    	cout << "\t\t   - Withdraw Money\n";
    	cout << "\t\t   - Check Balance\n";
    	cout << "\t\t3. Follow on-screen instructions\n";
    	cout << "\t\t4. Collect your card and cash\n";
    	cout << "\n\t\tFor assistance, contact: 1800-XXX-XXXX\n";
    	cout << "\t\t========================================\n\n";
	}
    
    bool verifyPin()
    {
    	int enteredPin;
    	cout << "\n\t\tEnter ATM PIN: ";
    	cin >> enteredPin;
    
    	if (enteredPin == atmPin) {
        	cout << "\n\t\t? PIN Verified Successfully!\n";
        	return true;
    	} else {
        	cout << "\n\t\t? INCORRECT PIN!\n";
        	cout << "\t\tExiting ATM System for security reasons.\n";
        	cout<<"\nNo more attempts allowed!! sorry!!";
        	cout << "\t\tThank you for using our service.\n\n";
        	return false;
   		 }
	}
    
    void displayMainMenu()
    {
    	cout << "\n\n";
    	cout << "\t\t========================================\n";
    	cout << "\t\t          MAIN MENU                    \n";
    	cout << "\t\t========================================\n";
    	cout << "\t\tEnter [1]. To Deposit Money\n";
    	cout << "\t\tEnter [2]. To Withdraw Money\n";
    	cout << "\t\tEnter [3]. To Balance Enquiry\n";
    	cout << "\t\tEnter [4]. To Exit ATM\n";
    	cout << "\t\t========================================\n";
	}
    
    void depositMoney()
    {
    	double amount;
    	cout << "\n\t\t========================================\n";
    	cout << "\t\t          DEPOSIT MONEY                \n";
    	cout << "\t\t========================================\n";
    	cout << "\t\tInitial Balance: Rs. " << initialBalance <<"\n";
    	cout << "\t\tCurrent Balance: Rs. " << currentBalance <<"\n";
    	cout << "\n\t\tEnter amount to deposit: Rs. ";
    	cin >> amount;
    
    	if (amount > 0) {
        	currentBalance += amount;
        	cout << "\n\t\t? Amount Deposited Successfully!\n";
        	cout << "\t\tNew Balance: Rs. " << currentBalance <<"\n";
        	cout << "\t\t========================================\n";
    	} else {
        	cout << "\n\t\t? Invalid amount! Please enter a positive value.\n";
    	}
	}
    
    void withdrawMoney()
    {
    	double amount;
    	cout << "\n\t\t========================================\n";
    	cout << "\t\t          WITHDRAW MONEY               \n";
    	cout << "\t\t========================================\n";
    	cout << "\t\tCurrent Balance: Rs. " <<currentBalance <<"\n";
    	cout << "\n\t\tEnter amount to withdraw: Rs. ";
    	cin >> amount;
    
    	if (amount > 0) {
        	if (amount <= currentBalance) {
            	currentBalance -= amount;
            	cout << "\n\t\t? Withdrawal Successful!\n";
           		cout << "\t\tWithdrawn Amount: Rs. " << amount <<"\n";
            	cout << "\t\tRemaining Balance: Rs. " << currentBalance <<"\n";
            	cout << "\t\t========================================\n";
        	} else {
            	cout << "\n\t\t========================================\n";
            	cout << "\t\t    UNSUCCESSFUL WITHDRAWAL            \n";
            	cout << "\t\t========================================\n";
            	cout << "\t\t? Insufficient Balance!\n";
            	cout << "\t\tYour Current Balance: Rs. " << currentBalance <<"\n";
            	cout << "\t\tRequested Amount: Rs. " << amount <<"\n";
            	cout << "\t\tShortfall: Rs. " << (amount - currentBalance) <<"\n";
            	cout << "\t\t========================================\n";
        	}
    	} else {
        	cout << "\n\t\t? Invalid amount! Please enter a positive value.\n";
    	}
	}
    
    void checkBalance()
    {
    	cout << "\n\t\t========================================\n";
    	cout << "\t\t          BALANCE INQUIRY              \n";
    	cout << "\t\t========================================\n";
    	cout << "\t\tInitial Balance: Rs. " <<initialBalance <<"\n";
    	cout << "\t\tCurrent Balance: Rs. " << currentBalance <<"\n";
    	cout << "\t\t========================================\n";
	}
    
    void runATM()
    {
    	int choice;
    	bool isLoggedIn = false;
    
    	displayWelcomeScreen();
    
    	while (true) {
        	if (!isLoggedIn) {
        		cout << "\t\t0. Help";
            	cout << "\n\t\t1. Enter ATM PIN\n";
            	cout << "\t\t2. Exit\n";
            	cout << "\n\t\tEnter your choice: ";
            	cin >> choice;
            
            	switch (choice) {
                	case 1:
                    	if (verifyPin()) {
                        	isLoggedIn = true;
                    	} else {
                        	return;
                    	}
                    	break;
                    
                	case 0:
                    	displayHelpScreen();
                    	break;
                    
                	case 2:
                    	cout << "\n\t\tThank you for using ATM Banking System!\n\n";
                    	return;
                    
                	default:
                    	cout << "\n\t\t? Invalid choice! Please try again.\n";
            	}
        	} else {
            	displayMainMenu();
            	cout << "\n\t\tEnter your choice: ";
            	cin >> choice;
            
            	switch (choice) {
                	case 1:
                   		depositMoney();
                    	break;
                    
                	case 2:
                    	withdrawMoney();
                    	break;
                    
                	case 3:
                    	checkBalance();
                    	break;
                    
                	case 4:
                    	cout << "\n\t\tThank you for using ATM Banking System!\n";
                    	cout << "\t\tPlease collect your card.\n\n";
                    	return;
                    
                	default:
                    	cout << "\n\t\t? Invalid choice! Please try again.\n";
            	}
        	}
   		}
	}
};


int main() {

    ATM myATM;

    myATM.runATM();
    
    return 0;
}
