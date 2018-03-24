//CPP program that illustrates function overloading


#include <iostream>

using namespace std;

void func(double x){
    cout << x << endl;
}

void func(int x){
    cout << x << endl;
}

void func(float x){
    cout << x << endl;
}

void func(float x, int y){
    cout << "float: " << x << endl;
    cout << "int: " << y << endl;
}


int main(){
    func(1.0);
    func(1);
    func(100,000);

    return 0;
}