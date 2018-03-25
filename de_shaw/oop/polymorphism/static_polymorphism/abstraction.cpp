//CPP program demonstrating abstraction

#include <iostream>

using namespace std;

class Fraction{
    public:
        Fraction(int n, int d){denominator = d; numerator = n;}
        void print(){
            cout << numerator << " / " << denominator << endl;
        }
        Boolean operator == (Fraction const &obj){
            Boolean res = 0;
            int compare = (obj.numerator / obj.denominator);
            if (compare == (numerator / denominator)){
                res = true;
            };
            return res;
        }
    private:
        int denominator;
        int numerator;
};

int main(){

    Fraction f1(5,6);
    Fraction f2(-5,-6);

    f2.print();
    f1.print();

    if (f2 == f1){
        cout << "equal" << endl;
    }else{
        cout << "not equal" << endl;
    }

    return 0;
}