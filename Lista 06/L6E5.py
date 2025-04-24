a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))
c = int(input("Digite outro valor: "))

if a>b:
    if a>c:
        if b>c: # A 1º e B 2º
            while b<a:
                print (b)
                b= b + 1

if b>a:
    if b>c:
        if a>c: #B 1º e A 2º
            while a<b:
                print (a)
                a= a + 1

if a>c:
    if a>b:
        if c>b: #A 1º e C 2º
            while c<a:
                print (c)
                c= c + 1

if b>a:
    if b>c:
        if c>a: #B 1º e C 2º
            while c<b:
                print (c)
                c= c + 1

if c>a:
    if c>b:
        if a>b: #C 1º e A 2º
            while a<c:
                print (a)
                a= a + 1

if c>a:
    if c>b:
        if b>a: #C 1º e B 2º
            while b<c:
                print (b)
                b= b + 1



