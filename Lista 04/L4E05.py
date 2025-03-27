a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
c = int(input('Digite outro numero: '))

if a<b:
    if a<c:
        print(f'O menor numero é {a}, e somado a 5 é {a+5}')

if b<a:
    if b<c:
        print(f'O menor numero é {b}, e somado a 5 é {b+5}')

if c<a:
    if c<b:
        print(f'O menor numero é {c}, e somado a 5 é {c+5}')


