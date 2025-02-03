#include <iostream>
#include <vector>

using namespace std;

bool isPrimo(int num) {
    if (num <= 1) return false;  // 0 e 1 não são primos
    if (num == 2) return true;   // 2 é primo
    if (num % 2 == 0) return false; // Números pares (exceto 2) não são primos

    // Verifica divisibilidade de 3 até sqrt(num), pulando números pares
    for (int i = 3; i * i <= num; i += 2) {
        if (num % i == 0) return false;
    }

    return true;
}

int main() {
    vector<int> primos;

    for (int i = 0; ; i++) {
        if (isPrimo(i)) {
            primos.push_back(i);
            cout << i << " é primo!" << endl;  // Imprime somente números primos
        }
    }

    return 0;
}
    