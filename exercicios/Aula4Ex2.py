import math
turno = input("Digite o seu turno de trabalho (N para noturno, D para diurno): ").upper()
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))

if turno in {"N", "D"} and horas_trabalhadas >= 0:
    valor_hora = 45.00 if turno == "N" else 37.50
    salario = valor_hora * horas_trabalhadas 
    print(f"O valor do salário é: R$ {salario:.2f}")
else:
    print("Turno inválido." if turno not in {"N", "D"} else "Erro: A quantidade de horas trabalhadas não pode ser negativa.")