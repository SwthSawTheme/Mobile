#include <stdio.h>
#include <stdlib.h>

int main(void) {

    char nome[16];
    double salario;
    double vendas;
    double porcentagem; 
    
    scanf("%s",&nome);
    scanf("%lf",&salario);
    scanf("%lf",&vendas);
    
    porcentagem = (vendas * 0.15) + salario;
    
    printf("TOTAL = R$ %.2lf\n", porcentagem);

    return 0;
}    