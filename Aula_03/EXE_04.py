salario = float(input("Digite seu salario: "))

if salario > 1250:
    aumento = salario * 0.10
    total = aumento + salario
    print("Seu novo salario com aumento de 10% é: ", total)

elif salario <= 1250:
    aumento = salario * 0.15
    total = aumento + salario
    print("Seu novo salario com aumento de 15% é: ", total)
