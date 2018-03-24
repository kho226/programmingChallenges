//CPP program that illustrates operator overloading

#include <iostream>

using namespace std;

class Complex{
    private:
        int real, img;
    public:
        Complex(int r = 0, int i = 0){real = r; img = i;}

        Complex operator + (Complex const &obj){
            Complex res;
            res.img = img + obj.img;
            res.real = real + obj.real;
            return res;
        }

        //to - do ~> subtraction

        void print(){
            cout << real << "+ i" << img << endl;
        }
};


int main(){

    Complex img(6,10), img1(5,6);
    Complex img2 = img1 + img;

    img1.print();

    return 0;
}
