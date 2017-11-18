#include <vector>
#include <iostream>
//#include <thread>

using namespace std;




int main()
{

//use a vector
vector<int> arr;


//push two elements into vector
arr.push_back(4);
arr.push_back(7);


//try to access the third element that does not exist
try
{
	arr.at(2);
}

catch (exception &e)//catch all exceptions
{
	cout << "Exception happened" << endl;
	try{throw e;}
	catch(...){
	}

}


}
