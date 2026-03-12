n = int(input("Digite um número inteiro maior ou igual a zero: "))

a = 0
b = 1

while a < n:
    a, b = b, a + b

if a == n or n == 0:
    print("Verdadeiro")
else:
    print("Falso")