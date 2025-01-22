import os
import time

linhas = 5
colunas = 5
posicao = 0

matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(".")
    matriz.append(linha)
        
while True:
    
    for m in matriz:
        print(" ".join(m))
        
    os.system("clear")
    time.sleep(0.5)