//Project#1 Basic Signup Project

#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

int main()

{

	string personName;
	int age;
	string userName;
	string lettersPassword;

	//Enter basic info
	cout << "Please enter your name" << endl;
	getline	(cin, personName);
	cout << "You entered " << personName << endl;


	cout << "Enter your age" << endl;
	cin.ignore();
	cin >> age;
	if (age <= 18)
	{
		cout << "Thank you" << endl;
	}
	else
		cout << "Your age is below the limit" <<endl;


	cout << "Please enter your username" << endl;
	cin.ignore();
	getline(cin, userName);
	cout << "You entered " << userName << endl;


	cout << "Please enter your password ";
	getline(cin, lettersPassword);

	cout << lettersPassword;





	return 0;
}
