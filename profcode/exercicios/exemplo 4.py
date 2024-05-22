import math,os
import os
os.system('cls')

num = int(input('Digite um numero inteiro: '))

resp = 'par' if num%2 == 0 else 'inpar'
print(f'{num} é {resp}')
