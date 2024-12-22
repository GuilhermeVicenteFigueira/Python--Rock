print("For utilizando lista")
lista = [1, 2, 3, 4, 5]

for elemento in lista:
    print(elemento)


print("For utilizando tupla")
tupla = (1, 2, 3, 4, 5)

for elemento in tupla:
    print(elemento)


pessoa={"nome": "Guilherme ", "idade": 18, "cidade": "Marilia "}

print("\nFor utilizando dicionario keys()")
for chave in pessoa.keys():
    print(chave)

print("\nFor utilizando dicionario values()")
for chave in pessoa.values():
    print(chave)

print("\nFor utilizando dicionario - items()")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")


# range(); intervalo numerico
#[0,1,2,3,4,5,6,7,8,9]

print("\nUtilizando a função range")
for numero in range(5):
    print("Numero", numero)


print("\nUtilizando a função range() cm len()")
lista = [1, 2, 3, 4, 5]
print(lista)
for indice in range(0, len(lista)): 
    if indice == 3:
        lista[indice] = 5
    else:
        lista[indice] = 0
print(lista)

# enumerate()

listaEnumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista):
    print(f"{indice}, {valor}")
    if indice == 1:
        print("Indice 1")
    
