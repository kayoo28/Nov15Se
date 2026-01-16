#include <iostream>
#include <cstdlib>      
using namespace std;

int main()
{
    int guess, number, attempts = 0;

    number = (rand() % 100) + 1;

    cout << "Guess a number between 1 and 100\n";

    do 
    {
        cout << "Enter your guess: ";
        cin >> guess;
        attempts++;

        if (guess > number)
        {
            cout << "Too high! Try again.\n";
        }
        else if (guess < number)
        {
            cout << "Too low! Try again.\n";
        }
        else
        {
            cout << "Congratulations! You guessed the number.\n";
            cout << "Number of attempts: " << attempts << endl;
            break;
        }
    }while(guess!=number);

    return 0;
}
