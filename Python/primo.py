# Leia 4 valores inteiros A, B, C e D.
# A seguir, se B for maior do que C
# e se D for maior do que A, e a 
# soma de C com D for maior que a soma
# de A e B e se C e D, ambos, 
# forem positivos e se a 
# variável A for par escrever 
# a mensagem "Valores aceitos",
# senão escrever "Valores nao aceitos".
import math

def is_primo(n):
    # Números menores que 2 não são primos
    if n < 2:
        return False
    
    # Verifica se n é divisível por algum número de 2 até a raiz quadrada de n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

def primo():
    primo = []
    for num in range(1000):
        if is_primo(num):
            primo.append(num)
    return len(primo),primo   

num, lista = primo()
print(num)
print(lista)   
         