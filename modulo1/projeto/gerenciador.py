def adicionarTarefa(tarefas, nomeTarefa):
    tarefa = {"Tarefa:": nomeTarefa, "Completa:": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nomeTarefa} foi adicionada com sucesso!")
    return


def verTarefas(tarefas):
    print("\nlista de tarefas")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["Completa:"] else " "
        nomeTarefa = tarefa["Tarefa:"]
        print(f"{indice}. [{status}] {nomeTarefa}")
    return
    

def atualizarNomeTarefa(tarefas, indiceTarefa, novoNomeTarefa):
    indiceTarefaAjustado = indiceTarefa - 1
    if indiceTarefaAjustado >= 0 and indiceTarefaAjustado < len(tarefas):
        tarefas[indiceTarefaAjustado]["Tarefa:"] = novoNomeTarefa
        print(f"\nTarefa{indiceTarefa} atualizada para {novoNomeTarefa}")
    else:
        print("\nIndice de tarefas invalido")
    return

def completarTarefa(tarefas, indiceTarefa):
    indiceTarefaAjustado = int(indiceTarefa) -1
    tarefas[indiceTarefaAjustado]["Completa:"] = True
    print(f"Tarefa {indiceTarefa} marcada como completada")
    return

def DeletarTarefaCompletadas(tarefas):
    for tarefa in tarefas:
        if tarefa ["Completa:"]:
            tarefas.remove(tarefa)
    print("tarefas completadas foram deletadas")
    return


tarefas = []

while True:
    print("\nMenu do Gerenciador de Lista de Tarefas")
    print("1. Adicionar tarefa")
    print("2. Ver tarefa")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completas")
    print("6. Sair")

    escolha = input("\nDigiter a sua escolha: ")

    if escolha == "1":
        nomeTarefa = input("\nDigite o nome da sua tarefa que deseja adicionar: ")
        adicionarTarefa(tarefas, nomeTarefa)

    elif escolha == "2":
        verTarefas(tarefas)

    elif escolha == "3":
        verTarefas (tarefas)
        indiceTarefa = int(input("\nDigite o numero da tarefa que deseja atulizar:"))
        novoNomeTarefa= input("\nDigite o novo nome da tarefa:")
        atualizarNomeTarefa(tarefas, indiceTarefa, novoNomeTarefa)
    
    elif escolha == "4":
        verTarefas(tarefas)
        indiceTarefa = input("Digite o numero da tarefa que deseja completar")
        completarTarefa(tarefas, indiceTarefa)
    
    elif  escolha == "5":
        DeletarTarefaCompletadas(tarefas)
        verTarefas(tarefas)
        

    elif escolha == "6":

        break

print("\nPrograma finalizado")


