import math

num = int(input("Digite um número : "))
if 0 <= num <= 9:
    r = math.sqrt(num)
    print(f"o valor correto é {num:.2f}")
else:
    print("Valor incorreto")