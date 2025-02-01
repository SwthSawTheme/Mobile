#include <iostream>
#include <vector>

using namespace std;

int mathAdi(int a, int b) {
    return a + b;
}

int mathSub(int a, int b) {
    return a - b;
}

int mathMult(int a, int b){
    return a * b;
}

int main(){

    int input;
    cout << "Digite um numero de 0 a 10 para ver a tábuada!" << endl;
    cout << "Número:";
    cin >> input;
    for (int i=0; i < 10; i++) {
        cout << i+1 << " x " << input << " = " << (i+1) * input << endl;
    }

    return 0;
}