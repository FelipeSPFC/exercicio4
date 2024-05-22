conta_agua = float(input("Digite o valor da conta de água: "))
conta_luz = float(input("Digite o valor da conta de luz: "))
conta_telefone = float(input("Digite o valor da conta de telefone: "))
salario = float(input("Digite o valor do seu salário: "))

total_contas = conta_agua + conta_luz + conta_telefone

if salario >= total_contas:
    saldo_restante = salario - total_contas
    print(f"Sobrou R$ {saldo_restante:.2f} do seu salário após pagar as contas.")
else:
    print("Salário insuficiente!")