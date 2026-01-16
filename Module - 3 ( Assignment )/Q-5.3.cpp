#include <iostream>
using namespace std;
int lengthOfString(char str1[]);

const char* palindrome(char str1[], char str2[])
{
    int i, l, j;
    int flag = 1;

    l = lengthOfString(str1);
    j = l - 1;

    for (i = 0; i < l; i++)
    {
        str2[i] = str1[j];
        j--;
    }
    str2[l] = '\0';

    for (i = 0; i < l; i++)
    {
        if (str1[i] != str2[i])
        {
            flag = 0;
            break;
        }
    }

    if (flag == 1)
        return "Palindrome";
    else
        return "Not Palindrome";
}

int lengthOfString(char str1[])
{
    int i, l = 0;
    for (i = 0; str1[i] != '\0'; i++)
    {
        l++;
    }
    return l;
}

int main()
{
    char str1[20], str2[20];

    cout << "Enter the string: ";
    cin >> str1;

    cout << palindrome(str1, str2);
    return 0;
}
