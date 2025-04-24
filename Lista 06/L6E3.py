a= int(input("Digite um valor: "))
b= int(input("Digite outro valor: "))


if a<b:
    while a<=b:
        print(a)
        a+=1

else:
    while a>=b:
        print(a)
        a-=1
