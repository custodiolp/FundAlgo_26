anoAtual = int(input("Digite o ano atual: "))
anoNasc = int(input("Digite o ano de nascimento: "))

calculo = anoAtual - anoNasc

if calculo >= 18:
    print("Apto a tirar CNH")
else:
    print("Nâo apto a tirar a CNH")