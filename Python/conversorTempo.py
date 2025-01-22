def conversor(sec):
    hora = sec // 3600
    r = sec % 3600
    minuto = r // 60
    segundo = r % 60
    return hora,minuto,segundo
    
n = int(input())
hora, minuto, segundo = conversor(n)

print(f"{hora}:{minuto}:{segundo}")