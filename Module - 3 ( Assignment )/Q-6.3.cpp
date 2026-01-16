#include <iostream>
using namespace std;
class Person
{
	protected:
    	int id;
    	string name;

	public:
    	void getPersonData()
    	{
        	cout << "Enter ID: ";		cin >> id;
        	cout << "Enter Name: ";		cin >> name;
    	}

    	void showPersonData()
    	{
        	cout << "ID: " << id <<"\n";
        	cout << "Name: " << name <<"\n";
    	}
};

class Student : public Person
{
    int marks;

	public:
    	void getStudentData()
    	{
        	getPersonData(); 
        	cout << "Enter Marks: ";		cin >> marks;
   		 }

    	void showStudentData()
    	{
        	showPersonData();  
        	cout << "Marks: " << marks <<"\n";
    	}
};
class Teacher : public Person
{
    string subject;

	public:
    	void getTeacherData()
    	{
        	getPersonData();
        	cout << "Enter Subject: ";		cin >> subject;
    	}

    	void showTeacherData()
    	{
        	showPersonData(); 
        	cout << "Subject: " << subject <<"\n";
    	}
};

int main()
{
    Student s;
    Teacher t;

    cout << "\nEnter Student Details\n";
    s.getStudentData();

    cout << "\n Enter Teacher Details\n";
    t.getTeacherData();

    cout << "\nStudent Information\n";
    s.showStudentData();

    cout << "\nTeacher Information\n";
    t.showTeacherData();

    return 0;
}
