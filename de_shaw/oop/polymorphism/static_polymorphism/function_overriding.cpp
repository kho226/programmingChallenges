//CPP program demonstrating dynamic polymorphism

#include <iostream>

using namespace std;

class Parent{
   
    public:

        void print(){
            cout << "Parent ~> Age()" << endl;
        }

};

class Child: public Parent{
    public:

        void print(){
            cout << "Child ~> Age()" << endl;
        }
};


int main(){

    Parent p;
    Child c = Child();
    
    c.print();
    p.print();

    return 0;
};