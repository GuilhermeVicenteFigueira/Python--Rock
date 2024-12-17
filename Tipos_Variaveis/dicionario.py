# dicionario de exemplo


pessoa = {"nome": "Guilherme", "idade": 30 , "cidade": "Marilia"}

print("Meu dicionario de exemplo :" , pessoa)

#Acessando valores por chaves

print("Nome:", pessoa ["nome"])
print("Idade:", pessoa ["idade"])
print("Cidade:", pessoa["cidade"])

pessoa["sobrenome"] = "Vicente"
print("sobrenome", pessoa["sobrenome"])


pessoa["idade:"] = 31
print("Idade:", pessoa["idade"])

#remover chave e valor

del pessoa["sobrenome"]
print("Meu dicionario de exemplo :" , pessoa)


# metodo: keys()

chave = pessoa.keys()
print("chaves do dicionario:", chave)

chave = list(pessoa.keys())
print("chaves do dicionario:", chave)
print("primeria chave do dicionario:", chave[0])


# metodo: values()

valores = pessoa.values()
print("Valores do dicionario:", valores)

valores = list(pessoa.values())
print("Valores do dicionario:", valores)
print("primerio valor do dicionario:", valores[0])


# metodo: items()

itens = pessoa.items()
print("pares chaves-valor do dicionario", itens)

itens = list(pessoa.items())
print("pares chaves-valor do dicionario", itens)
print("primeria chave-valor do dicionario: %s = %s " % (itens[0][0], itens [0][2]))





