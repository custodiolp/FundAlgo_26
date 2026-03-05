somatoria = 0
media = 0
qnt = 0

while True:
    entrada = int(input("Digite um numero a somar ou 0 pra sair:  "))
    if entrada == 0:
        break
    else:
        somatoria = somatoria + entrada
        qnt = qnt + 1
        media = somatoria / qnt

print("Quantidade: ", qnt)
print("Somatoria: ", somatoria)
print("Média: ", media)