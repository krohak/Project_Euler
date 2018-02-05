#include<iostream>
using namespace std;

class Base
{
public:
	virtual void show() { cout<<" In Base \n"; }
	//virtual void hide() { cout<<"In Base \n"; }
};

class Derived: public Base
{
public:
	void show() { cout<<"In Derived \n"; }
	void hide() { cout<<"In Derived \n"; }
};

int main(void)
{
	Base *bp = new Derived;
	//Derived *bp = new Derived;
	bp->show(); // RUN-TIME POLYMORPHISM
	static_cast<Derived*>(bp)->hide();
	return 0;
}

