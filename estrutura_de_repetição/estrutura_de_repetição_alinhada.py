qtd = int(input("Digite a quantidade de numeros a serem testados: "))

i = 1
total_primos = 0 

while i <= qtd:
    numero = int(input(f"Digite o numero {i}: "))
    if numero > 1:
        divisor = 1
        qtd_divisores = 0
        while divisor <= numero:
            if numero % divisor == 0:
                qtd_divisores = qtd_divisores + 1
            divisor = divisor + 1
        if qtd_divisores == 2:
            total_primos = total_primos + 1
    i = i + 1

print(f"Você digitou {total_primos} números primos de um total de {qtd} números.")