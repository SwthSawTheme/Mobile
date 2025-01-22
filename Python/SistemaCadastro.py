import random
import os

class Usuario():
    def __init__(self):
        self.usuarios = {}
        
    def Register(self):
        print('Registro de usuário\n')
        login = input('Login: ')
        
        if login == '':
            print('Login inválido!')
        else:
            if login in self.usuarios:
                print('Login já existe!')
            else:
                senha = input('Password: ')
                self.usuarios[login] = senha
                print('Usuario registrado!')
                
    def Login(self):
        print('Entrar\n')
        login = input('Login: ')
        if login in self.usuarios:
            senha = input('Password: ')
            if senha == self.usuarios[login]:
                print('Logado com sucesso!')
            else:
                print('Senha incorreta!')
        else:
            print('Login não encontrado!')        


def main():
    user = Usuario()
    user.usuarios = {}
    
    while True:
        print('Controle de Usuario\n')
        menu = ['1.Entrar','2.Registrar','3.Sair\n']
        
        for item in menu:
            print(item)
        escolha = input(':/>')
        
        if escolha == '1':
            os.system('clear')
            user.Login()
            input()
            os.system('clear')
        elif escolha == '2':
            os.system('clear')
            user.Register()
            input()
            os.system('clear')
        elif escolha == '3':
            break
        else:
            print('Comando invalido!')  
            input()
            os.system('clear')      
        
main()        