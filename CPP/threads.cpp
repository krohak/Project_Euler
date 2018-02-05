//https://www.tutorialcup.com/cplusplus/multithreading.htm

#include <iostream>
#include <thread> 

using namespace std;

void threadFunc()
{
	cout << "Welcome to Multithreading" << endl;

}

int main()
{
	//pass a function to thread
	thread funcTest1(threadFunc);

	funcTest1.detach();

	if (funcTest1.joinable())
	{
	//main is blocked until funcTest1 is not finished
	funcTest1.join();
	}
	
	else
	{
	cout << "functTest1 is detached" << endl;
	}


}
