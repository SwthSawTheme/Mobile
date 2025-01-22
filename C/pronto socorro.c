#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_PACIENTES 100 //maximo de atendimentos
#define NOME_MAX 50 //maximo de caracteres em um nome
#define HORARIO_MAX 9 //maximo de caracteres em um horario (HH:MM:SS)

typedef struct {
    char nome[NOME_MAX];
    char prioridade[6]; //baixa, media ou alta
    char horario_chegada[HORARIO_MAX]; //horario de chegada
} Paciente;

Paciente pacientes[MAX_PACIENTES];
int contador = 0;

//Horário atual
void obterHorarioAtual(char *horario) {
    time_t t = time(NULL);
    struct tm *tm = localtime(&t);
    sprintf(horario, "%02d:%02d:%02d", tm->tm_hour, tm->tm_min, tm->tm_sec);
}

//Adicionar paciente
void adicionarPaciente() {
    if (contador >= MAX_PACIENTES){
        printf("Limite de pacientes atingido.\n"); 
        return;
    }

    Paciente p;
    printf("Selecionado: Adicionar Paciente\n\n");
    printf("Digite o nome do paciente: ");
    scanf(" %[^\n]", p.nome);

    // Validação da prioridade
    while (1) {
        printf("Digite a prioridade do paciente (baixa, media, alta): ");
        scanf(" %[^\n]", p.prioridade);
        
        if (strcmp(p.prioridade, "baixa") == 0 || strcmp(p.prioridade, "media") == 0 || strcmp(p.prioridade, "alta") == 0)
            break;
        else printf("\nPrioridade invalida. Tente novamente.\n");
    }
    
    // Horário de chegada
    obterHorarioAtual(p.horario_chegada);
    
    pacientes[contador++] = p;
    printf("\nPaciente adicionado com sucesso!\n\n");
}

// Indice do proximo paciente
int proximoPaciente() {
    for (int i = 0; i < contador; i++) {
        // Verifica prioridade alta
        if (strcmp(pacientes[i].prioridade, "alta") == 0) 
            return i;
    }
    for (int i = 0; i < contador; i++) {
        // Verifica prioridade media
        if (strcmp(pacientes[i].prioridade, "media") == 0)
            return i;
    }
    for (int i = 0; i < contador; i++) {
        // Verifica prioridade baixa
        if (strcmp(pacientes[i].prioridade, "baixa") == 0)
            return i;
    }
    return -1; // Não encontrou
}

// Atender o proximo paciente
void atenderPaciente() {
    printf("Selecionado: Atender Proximo Paciente\n\n");
    int indice = proximoPaciente();
    if (indice == -1) {
        printf("Nenhum paciente para atender.\n\n");
        return;
    }

    printf("Atendendo paciente: %s, Prioridade: %s\n\n", pacientes[indice].nome, pacientes[indice].prioridade);
    // Remover o paciente da lista
    for (int i = indice; i < contador - 1; i++) 
        pacientes[i] = pacientes[i + 1];
    contador--;
}

// Imprimir a lista de pacientes
void imprimirPacientes() {
    printf("Selecionado: Lista de Pacientes\n\n");
    if (contador == 0) {
        printf("Nenhum paciente na lista.\n\n");
        return;
    }
    printf("Lista de Pacientes:\n\n");
    for (int i = 0; i < contador; i++)
        printf("%s - Prioridade: %s - Horario de Chegada: %s\n", pacientes[i].nome, pacientes[i].prioridade, pacientes[i].horario_chegada);
    printf("\n");
}

int main() {
    int opcao;

    do {
        printf("------------------------------\n");
        printf("| \t    Menu:\t     |\n");
        printf("------------------------------\n");
        printf("| 1. Adicionar Paciente\t     |\n");
        printf("------------------------------\n");
        printf("| 2. Atender Proximo Paciente|\n");
        printf("------------------------------\n");
        printf("| 3. Listar Pacientes \t     |\n");
        printf("------------------------------\n");
        printf("| 0. Sair\t\t     |\n");
        printf("------------------------------\n");
        printf("\nEscolha uma opcao: ");

        // Validação
        while (scanf("%d", &opcao) != 1) {
            printf("\nEntrada invalida. Digite um numero: ");
            while (getchar() != '\n'); // Limpa o buffer de entrada
        }
        printf("\n");

        switch (opcao) {
            case 1:
                system("cls");
                adicionarPaciente();
                break;
            case 2:
                system("cls");
                atenderPaciente();
                break;
            case 3:
                system("cls");
                imprimirPacientes();
                break;
            case 0:
                system("cls");
                printf("Saindo do sistema.\n");
                break;
            default:
                printf("Opcao invalida. Tente novamente.\n");
        }
    } while (opcao != 0);

    return 0;
}
