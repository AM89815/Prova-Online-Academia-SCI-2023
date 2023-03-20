#Solicitar 5 números, ao fim, imprimir o número maior e o número menor.
valor = 0
maior = 0
menor = 1000000000000
lista = []

print("Insira 5 números! ")
for count in range(5): 
    valor = input("Número {}: " .format(count+1))
    if int(valor) > maior:
        maior = int(valor)
    if int(valor) < menor:
        menor = int(valor)
    
print('O maior número é: ' + str(maior))
print('O menor número é: ' + str(menor))