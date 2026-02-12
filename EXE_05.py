HoraTrabalho = float(input("Digite o valor de hora de trabalho: "))
HoraTrabalhada = float(input("Digite o numero de horas trabalhadas: "))

salariobruto = HoraTrabalho * HoraTrabalhada
print("+ salario bruto:R$ ", salariobruto)
IR = 0.11 * salariobruto
print("- IR (11%):R$ ", IR)
INSS = 0.08 * salariobruto
print("- INSS (8%):R$ ", INSS)
Sindicato = 0.05 * salariobruto
print("- sindicato (5%):R$ ", Sindicato)
Salarioliq = salariobruto - IR - INSS - Sindicato
print("+ salario Liquido:R$ ", Salarioliq)
