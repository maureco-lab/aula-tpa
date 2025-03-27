a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
c = int(input('Digite outro numero: '))
d = int(input('Digite outro numero: '))

r1 = a+b
r2 = c-d

r3= r1 + r2

if r3==10:
    print(f'{a} é igual a 10')

else:

    if r3 >=10:
        print(f'{r3} é maior que 10')

    else:
        print(f'{r3} é menor que 10')
