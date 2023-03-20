# Solicitar a inserção de 5 números, ao final, imprimir os números pares, números ímpares e a média geral desses números
valor = 0
soma = 0
lista = []
listaPares = []
listaImpares = []

print("Insira 5 números! ")
for count in range(5): 
    valor = input("Número {}: " .format(count+1))
    lista.append(int(valor)) 

for count in range(len(lista)):
    resultado = lista[count] % 2
    if resultado == 0:
        listaPares.append(lista[count])
    else:
        listaImpares.append(lista[count])
    soma += lista[count]
    count += 1

media = soma / len(lista)
print('Os números pares são: ')
for count in range(len(listaPares)):
    print(listaPares[count])

print('Os números ímpares são: ')
for count in range(len(listaImpares)):
    print(listaImpares[count])

print('A média geral dos números inseridos é: ' + str(media))
