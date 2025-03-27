a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
c = int(input('Digite outro numero: '))

if a<b:
    if a<c:
        if b<c:
            print(f' A ordem crescente é : {a}, {b}, {c}')
        else:
            print(f' A ordem crescente é : {a}, {c}, {b}')

if b<a:
    if b<c:
        if a<c: 
            print(f' A ordem crescente é : {b}, {a} ,{c}')
        else:
            print(f' A ordem crescente é : {b}, {c}, {a}')

if c<a:
    if c<b:
        if a<b:
            print(f' A ordem crescente é : {c}, {a}, {b}')
        else:
            print(f' A ordem crescente é : {c}, {b}, {a}')
