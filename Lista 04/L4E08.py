a = int(input('Digite um numero: '))

if a>=10:
    print(f'{a} será somado a 5')
    a = a+5
    if a>25:
        print(f'{a} somado á 5, é maior que 25')

    else:
        print(f'{a} somado á 5, é menor que 25')

else:
    print(f'{a} será somado a 20')
    a = a+20
    if a>25:
        print (f'{a} é maior que 25')

    else:
        print (f'{a} é menor que 25')
