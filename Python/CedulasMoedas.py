valor = float(input())

n1 = valor // 100
valor %= 100

n2 = valor // 50
valor %= 50

n3 = valor // 20
valor %= 20

n4 = valor // 10
valor %= 10

n5 = valor // 5
valor %= 5

n6 = valor // 2
valor %= 2

n7 = valor // 1
valor %= 1

n8 = valor // 0.50
valor %= 0.50

n9 = valor // 0.25
valor %= 0.25

n10 = valor // 0.10
valor %= 0.10

n11 = valor // 0.05
valor %= 0.05

n12 = valor // 0.01

print("NOTAS:")
print(f"{round(n1)} nota(s) de R$ 100.00")
print(f"{round(n2)} nota(s) de R$ 50.00")
print(f"{round(n3)} nota(s) de R$ 20.00")
print(f"{round(n4)} nota(s) de R$ 10.00")
print(f"{round(n5)} nota(s) de R$ 5.00")
print(f"{round(n6)} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{round(n7)} moeda(s) de R$ 1.00")
print(f"{round(n8)} moeda(s) de R$ 0.50")
print(f"{round(n9)} moeda(s) de R$ 0.25")
print(f"{round(n10)} moeda(s) de R$ 0.10")
print(f"{round(n11)} moeda(s) de R$ 0.05")
print(f"{round(n12)} moeda(s) de R$ 0.01")