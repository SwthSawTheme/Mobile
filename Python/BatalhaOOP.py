from random import randint
import os
import time

class Entity():
    
    def __init__(self, name, life, damage, defense):
        self.name = name
        self.life = life
        self.damage = damage
        self.defense = defense
        self.level = 1
    
    def attack(self, entity):
        entity.life -= self.damage
        print(f'{entity.name} recebeu {self.damage} de dano! Vida:{entity.life}')
    
    def batalha(self, entity2):
        print(f'\n{self.name}\nVida:{self.life}')
        self.attack(entity2)
    
    def set_acao(self):
        pass


def game():
    print('='*10,"THE VALEY",'='*10)
    name = input('Nome do personagem: ')
    player = Entity(name,100,randint(1,5),3)
    enemy = Entity('Globin',50,randint(1,3),3)
    
    while True:
        print('1.Procurar Inimigo')
        print('2.Inventario')
        print('3.Sair')
        
        try:
            choice = int(input('✎: '))
            
            if choice == 1:
               chance = randint(1,2)
               if chance == 2:
                   print("Você encontrou algo a espreita...")
                   time.sleep(2)
                   os.system('clear')
                   print(f'{enemy.name} iniciou um combate!')
                   input()
                   os.system('clear')
                   
                   while enemy.life > 0 and player.life > 0:
                       player.batalha(enemy)
                       input()
                       os.system('clear')
                       if enemy.life <= 0:
                           print(f'{player.name} venceu a batalha!')
                           input()
                           os.system('clear')
                           break

                       enemy.batalha(player)
                       input()
                       os.system('clear')
                       if player.life <= 0:
                           print(f'{enemy.name} venceu a batalha!')
                           input()
                           os.system('clear')
                           break

               else:
                   print('Inimigo não encontrado...')
                   input()
                   os.system('clear')
                               
            elif choice == 2:
                pass
                os.system('clear')
                
            elif choice == 3:
                print('Saindo...')
                time.sleep(1)
                break  
        except ValueError:
            print('Comando invalido!')
            input()
            os.system('clear')
game()            
        
        
        
        
    
                  