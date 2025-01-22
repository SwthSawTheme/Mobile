import time
import os
#Definir cores para o terminal sendo reset o último
reset_color = "\033[0m"
red = "\033[1;31;40m"
green = "\033[1;32;40m"
yellow = "\033[1;33;40m"
blue = "\033[1;34;40m"
magenta = "\033[1;35;40m"
cyan = "\033[1;36;40m"
#Funcao para imprimir o texto na tela de forma animada
def textoImpresso(texto,timer=0.2):
    for letra in texto:
        print(cyan+letra+reset_color,end='',flush=True)
        time.sleep(timer)
    
texto = "Frase animada!"    
textoImpresso(texto,0.1)    