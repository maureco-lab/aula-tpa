a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))

if a==b:
    print("Os valores não podem ser iguais")

else:
    if a<b:
        a = a+5

    else:
        b = b+5



    if a>b:
        print(f'Esse é o maior valor: {a}')

    else:
        print(f'Esse é o maior valor: {b}')



    
