#include <iostream>
using namespace std;
int x = 10;

void show()
{
    int x = 20;

    cout << "\nInside function show()";
    cout << "\nLocal x = " << x;
    cout << "\nGlobal x = " << ::x; 
}

int main()
{
    cout << "\nInside main() : ";
    cout << "\nGlobal x = " << x;

    show();

    return 0;
}
