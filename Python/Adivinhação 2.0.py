import time
import os
import random

def game():
    global pontos
    global tentativas
    pontos = 0
    tentativas = 5
    
    while tentativas > 0:
        print('Jogo da adivinhação\n')
        print(f'Pontos:{pontos}')
        print(f'Tentativas:{tentativas}\n')
        pc = random.randint(1,3)
        print(f'teste:{pc}')
        try:
            escolha = int(input('Em qual número de 1 a 3 estou pensando?: '))
        
            if escolha == pc:
                print('Você acertou e ganhou 100 pontos!')
                pontos += 100
                input()
                os.system('clear')
                
            elif escolha not in (1,2,3):
                print('Digite um comando valido!')
                input()
                os.system('clear')
                
            elif pontos <= 0:
                print('Você errou e perdeu 1 tentativa!')
                tentativas -= 1
                input()
                os.system('clear')
                
            else:
                print('Você errou e perdeu 50 pontos!')
                pontos -= 50
                input()
                os.system('clear')
                
        except:
            print('Digite um comando válido!')
            input()
            os.system('clear')
            
game()            
