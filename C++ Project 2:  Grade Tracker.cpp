#include <iostream>
#include <string>

using namespace std;

int main()

{
	double grades;
	double totalOfGrades = 0;
	int amountOfClass = 0;
	string className;


	cout << "Welcome to my Grade Calculator Version 2" << endl;
	cout << "Please enter your grades (enter -1 if you are finished)" << endl;
	cin >> grades;

	while (grades != -1)
	{
		totalOfGrades += grades;
		amountOfClass++;

		cout << "Please enter your grades (enter -1 if you are finished" << endl;
		cin >> grades;
	}

	cout << "The average of your total grades is " << endl;
	cout << (totalOfGrades / amountOfClass);


	return 0;
}
