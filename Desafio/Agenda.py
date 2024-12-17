def adicionarContato(contatos, nomeContato, telefoneContato, emailContato):
    contato = {"Nome:": nomeContato, "Telefone:": telefoneContato, "Email:": emailContato, "Favorito:": False}
    contatos.append(contato)
    print(f"O Contato {nomeContato} foi adicionado com sucesso na sua agenda!")
    return



def verListaContato(contatos):
    print("\n Agenda")
    for indice, contato in enumerate(contatos, start=1):
        status = " (Favorito) " if contato["Favorito:"] else " "
        nomeContato = contato["Nome:"]
        print(f"{indice}{status} {nomeContato}")
    return
    
    

def editarContato(contatos, indiceContato, novoNomeContato):
    indiceContatoAjustado = indiceContato -1
    if indiceContato >=0 and indiceContatoAjustado <len(contatos):
        contatos[indiceContatoAjustado]["Nome:"] = novoNomeContato
        print(f"\n Contato{indiceContato} atualizado para {novoNomeContato}")
    else:
        print("\nIndice de contatos invalido!!")
    return



def marcarfavorito(contatos, indiceContato):
    indiceContatoAjustado = int(indiceContato) -1
    contatos [indiceContatoAjustado]["Favorito:"] = True
    print(f"Contato {indiceContato} adicionado a Lista de favoritos!")
    return


def desmarcarfavorito(contatos, indiceContato):
    print("\nLista de Contatos deseja tirar o Favorito:")
    indiceContatoAjustado = int(indiceContato) - 1
    if 0 <= indiceContatoAjustado < len(contatos):
        contatos[indiceContatoAjustado]["Favorito:"] = False
        print(f"Contato {contatos[indiceContatoAjustado]['Nome:']} removido da lista de favoritos!")
    else:
        print("Índice de contato inválido!")
    return
    

def verListaContatoFavorito(contatos):
    print("\nLista de Contatos Favorito:")
    for contato in contatos:
        if contato["Favorito:"]:  
            print(contato["Nome:"])  
    return

def apagarContato(contatos):
    print("\nQual contato deseja excluir?")
    if not contatos:  
        print("Nenhum contato disponível para excluir.")
        return
    for indice, contato in enumerate(contatos, start=1):
        print(f"{indice}. {contato['Nome:']}")  
    indiceContato = input("\nDigite o número do contato que deseja excluir: ")
    try:
        indiceContato = int(indiceContato) - 1  
        if 0 <= indiceContato < len(contatos): 
            contatoRemovido = contatos.pop(indiceContato)  
            print(f"Contato '{contatoRemovido['Nome:']}' foi excluído com sucesso!")
        else:
            print("Índice inválido! Nenhum contato foi apagado.")
    except ValueError:
        print("Por favor, insira um número válido.")



        

        
contatos = []

while True:
    print("\n Sua agenda telefonica!!")
    print(" 1.Adicionar contato")
    print(" 2.Vizulizar lista de contato")
    print(" 3.Editar contato")
    print(" 4.Marcar contato como favorito")
    print(" 5.Desmarcar como favorito")
    print(" 6.Ver a sua lista de contato favorito")
    print(" 7.Apagar contato")

    escolha = input("O que deseja fazer?")

    
    if escolha == "1":
        nomeContato = input("\nDigite o Nome do seu contato que deseja adicionar: ")
        telefoneContato = input("\nDigite o Telefone do seu contato que deseja adicionar: ")
        emailContato = input("\nDigite o Email do seu contato que deseja adicionar: ")
        adicionarContato(contatos, nomeContato, telefoneContato, emailContato) 

    elif escolha == "2":
        verListaContato(contatos)

    elif escolha == "3":
        verListaContato(contatos)
        indiceContato = int(input("\n Digite o numero do contato que deseja alterar?"))
        novoNomeContato = input("\n Digite o novo nome do contato")
        editarContato(contatos, indiceContato, novoNomeContato)

    elif escolha == "4":
        verListaContato(contatos)
        indiceContato = input("Digite o Numero que deseja favoritar!")
        marcarfavorito(contatos, indiceContato)

    elif escolha == "5":
        indiceContato = input("Digite o número do contato que deseja desfavoritar: ")
        desmarcarfavorito(contatos, indiceContato)
        verListaContato(contatos)

    elif escolha == "6":
        verListaContato(contatos)

    elif escolha == "7":
        apagarContato(contatos)
        verListaContato(contatos)     