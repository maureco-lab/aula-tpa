lista = []

for i in range (5):
  num = int(input("Digite um numero: "))
  lista.append(num)
  tamanho = len(lista)
for a in range (tamanho - 1):
  for b in range (tamanho - 1):
    if lista[b] > lista[b + 1]:
      lista[b], lista[b + 1] = lista[b + 1], lista[b]
print(lista)