#include <iostream>

using namespace std;


class Fish{

  private:
    int fins;
    string privateMember;
    static int counter;
    //counter = 0;

  protected:
    string protectedMember;

  public:
    string publicMember;

    Fish(){
      privateMember = "I am private";
      protectedMember = "I am protected";
      publicMember = "I am public";
      counter++;
    }

    int getFins(){
      return fins;
    }
    void setFins(int num){
      fins = num;
    }
    void delFins(){
      fins=0;
    }

    static int FishInstances(){
      //static int counter;
      return counter;
    }


    virtual void swim(){
      cout << "Swim" <<endl;
    }
    virtual void swim_backwards(){
      cout << "Back" << endl;
    }
    virtual void skeleton(){
      cout << "Skel" <<endl;
    }
};

int Fish::counter = 0;

class Shark: Fish{

public:

  int teeth;

  Shark(int num){
    teeth = num;
  }

  virtual void swim(){
    cout << "Swim Shark" <<endl;
  }
  virtual void swim_backwards(){
    cout << "Back Shark" << endl;
  }
  virtual void skeleton(){
    cout << "Skel Shark" <<endl;
  }


};

int main(){

    Fish f;
    f.swim();

    Fish f2;
    //f.swim();

    Shark s(97);
    s.swim();

    cout << Fish::FishInstances()<<endl;
    
    return 0;
}
