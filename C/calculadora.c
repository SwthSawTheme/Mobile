#include <stdio.h>
#include <stdbool.h>

int soma(int a, int b) {
    return a + b;
}

int subtracao(int a, int b) {
    return a - b;
}

int vezes(int a, int b) {
    return a * b;
}

int divisao(int a, int b) {
    return a / b;
}

int main(void) {
    int n1 = 0;
    int n2 = 0;
    char choice;
    bool parar = false;

    do {
        puts("Calculadora simples\n");
        printf("Escolha entre os operadores +, -, *, / ou 'q' para sair: ");
        // Leitura do caractere de escolha
        scanf("%c", &choice);

        // Verifica se o usuário deseja parar
        if (choice == 'q') {
            parar = true;
            continue;
        }

        printf("Digite o primeiro valor: ");
        scanf("%d", &n1);
        printf("Digite o segundo valor: ");
        scanf("%d", &n2);

        switch(choice) {
            case '+':
                printf("A soma de %d + %d = %d\n", n1, n2, soma(n1, n2));
                break;
            case '-':
                printf("A subtracao de %d - %d = %d\n", n1, n2, subtracao(n1, n2));
                break;
            case '*':
                printf("A multiplicacao de %d * %d = %d\n", n1, n2, vezes(n1, n2));
                break;
            case '/':
                // Verificar divisão por zero
                if (n2 != 0) {
                    printf("A divisao de %d / %d = %d\n", n1, n2, divisao(n1, n2));
                } else {
                    printf("Erro: Divisão por zero não é permitida.\n");
                }
                break;
            default:
                printf("Operador invalido.\n");
                break;
        }
    } while (!parar);

    return 0;
}
    