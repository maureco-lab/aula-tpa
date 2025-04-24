a = int(input("Digite um numero entre 5 e 10: "))

while a<5:
    print("O valor deve ser entre 5 e 10!")
    a = int(input("Digite novamente: "))

while a>10:
    print("O valor deve ser entre 5 e 10!")
    a = int(input("Digite novamente: "))

print(f' O valor digitado foi {a} !')
