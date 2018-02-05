#include <vector>
#include <iostream>
#include <thread>

using namespace std;

vector<int> vec;
void push()
{
	for (int i = 0; i != 10; ++i)
	{
		cout << "Push " << i << endl;
		_sleep(500);
		vec.push_back(i);
	}
}
void pop()
{
	for (int i = 0; i != 10; ++i)
	{
		if (vec.size() > 0)
		{
			int val = vec.back();
			vec.pop_back();
			cout << "Pop "<< val << endl;
		}
	_sleep(500);
	}
}
int main()
{
	//create two threads
	thread push(push);
	thread pop(pop);
	if (push.joinable())
		push.join();
	if (pop.joinable())
		pop.join();
}
