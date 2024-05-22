n1= float(input('digite a 1ª nota: '))
n2= float(input('digite a 2ª nota: '))

media = (n1+n2)/2
resultado = 'aprovado' if media >= 6 else 'reprovado'

print(f'vove foi {resultado}, com media: {media} ')