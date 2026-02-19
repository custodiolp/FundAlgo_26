km = int(input("Digite a quantidade de KM que deseja: "))

if km <= 200:
    preco = km * 0.50
    print("O valor da viagem é:R$", preco)

elif km > 200:
    preco = km * 0.45
    print("O valor da viagem é:R$", preco)