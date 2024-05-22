import math, os
import os
os.system('cls')

n1 = float(input('digite a 1ª nota:'))
n2 = float(input('digite a 2ª nota:'))

media = (n1 + n2) /2
if media>= 5.0:
    print('aprovado')

else:
    print('reprovado')