import os

global numero
numero = 0

def salvar():
    with open('/storage/emulated/0/Download/save.txt','w') as arquivo:
        arquivo.write(str(numero))
        
def load():
    with open('/storage/emulated/0/Download/save.txt', 'r') as arquivo:
        teste = arquivo.read()
    return int(teste)
    
def game():
    global numero
    while True:
        print(f'Numero:{numero}\n\n1.Sair\n')
        try:
            escolha = int(input('Digite um número: '))
        
            if escolha == 1:
                break
            elif escolha is not 1:   
                numero += escolha
                salvar()
            os.system('clear') 
        except:
            print('Somente número!')
            input()
            os.system('clear')
    
try:
    numero += load()
    game()
except:
    game()