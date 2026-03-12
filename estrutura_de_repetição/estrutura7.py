num = int(input("Digite um número inteiro: "))
original = num 
contador = 0

if num == 0:
    contador = 1
else:
    num = abs(num)

    while num > 0:
        num = num // 10
        contador += 1
print(f"O numero {original} tem {contador} digitos.")