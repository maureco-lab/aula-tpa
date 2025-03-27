a = int(input('Digite um numero: '))
b = int(input('Digite um numero: '))

if a<b:
    a = a*10
    b = b//2
    r1 = a+b
    if r1 % 2 ==0:
        print(f' {r1} é par')
    else:
        print(f' {r1} é impar')

else:
    b = b*10
    a = a//2
    r2 = a+b
    if r2 % 2 ==0:
        print(f' {r2} é par')
    else:
        print(f' {r2} é impar')
