import math
valor_compra = float(input("Digite o valor da compra: "))

if valor_compra > 200:
    desconto = 0.2 * valor_compra
    valor_compra_com_desconto = valor_compra - desconto
    print(f"O valor da compra com desconto é: R$ {valor_compra_com_desconto:.2f}")
else:
    print(f"O valor da compra é: R$ {valor_compra:.2f}")