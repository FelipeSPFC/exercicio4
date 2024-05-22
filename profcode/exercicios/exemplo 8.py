import math
num = float(input("Digite um número qualquer: "))
if num >= 0:
    r = math.sqrt(num)
    print(f"A raiz quadrada de {num:.2f} é: {r:.2f}")
        
else:
    print("Fm R, não há raiz quadrada ded numero negativo")