a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite mais um número: "))

if a>b:
    if a>c:
        print(f'Esse é o maior número: {a}')

if b>a:
    if b>c:
        print(f'Esse é o maior número: {b}')

if c>a:
    if c>b:
        print(f'Esse é o maior número: {c}')
        

