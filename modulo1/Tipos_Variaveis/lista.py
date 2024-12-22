#Declaração

minhaLista = [1, 2, 3, 7, 5, 6 , 8, 122, 2, 13]

#Exibindo a lista por completo
print("Miinha lista de exemplo", minhaLista)

#Exibindo a lista
print("minhas listas", minhaLista[0])
print("minhas listas", minhaLista[0], minhaLista[4])
print("minhas listas", minhaLista[1:7])
print("minhas listas", minhaLista[:6])
print("minhas listas", minhaLista[2:])


#modificação de dados:
minhaLista[0] = 60
print("Minha lista atualizada", minhaLista)

#metodos de lista:

#metodo append() adciona um elemtno no final da lista;
minhaLista.append(6)
print("Minha lista com um novo elemmento em seu final", minhaLista)

#metodo index aumenta o slot da lista

indece= minhaLista.index(6)
print("indice do elemento 6",indece)

#metodo insert: insere um elemento em um indice(slot) especifico
minhaLista.insert(2, 10)
print("Lista com isert", minhaLista[2])

#metodo pop (remove)
elementoRemovido = minhaLista.pop(3)
print("Retira o slot deseja (3)", minhaLista)

#metodo remove
minhaLista.remove(2)
print("Após remove(True)", minhaLista)

#metodo sort (organizar)
minhaLista.sort()
print("Após sort()", minhaLista)