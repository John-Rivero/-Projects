#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

int main()

{
	double classGrade;
	double totalGrade = 0;
	int classCount = 0;
	string className;
	char programComplete;
	double gradeAverage;

	cout << "Welcome to my grade calculator program" << endl;
	cout << "Please enter the name of the class" << endl;
	getline(cin, className);
	cout << "You entered " << className << endl;


	while (true)
	{
		cout << "Please enter your grades (if you are finished please type 'done')" << endl;
		cin >> classGrade;
		totalGrade += classGrade;
		classCount++;

		cout << "Press 'y' to continue or 'n' to quit" <<endl;
		cin >> programComplete;


		if (programComplete == 'y')
		{
			continue;
		}

		else if (programComplete == 'n')
		{
			break;
		}

		else
		{
			cout << "Incorrect input, please try again" << endl;
			continue;
		}

	}

	cout << "The total average of your grades is: " << endl;
	gradeAverage = (totalGrade / classCount);
	cout << gradeAverage;

	return 0;





}
