#include <iostream>

int getNumber(int arg1,int arg2){
    int sum = arg1 + arg2;
    return sum;
}

int main(){

    int num;
    int num1;

    std::cout << "Digite um numero: " << std::endl;
    std::cin >> num;
    std::cout << "Digite outro número: " << std::endl;
    std::cin >> num1;
    std::cout << "A soma de " << num << " e " << num1 << " = " << getNumber(num,num1) << std::endl;
    return 0;
}    