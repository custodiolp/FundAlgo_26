cont = 0
maior = -999999

while cont < 6:
    nro = int(input("Digite um numero: "))
    if nro > maior:
        maior = nro
    cont = cont + 1

print(maior)
