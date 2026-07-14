from task_manager import TaskManager


def menu():
    gerenciador = TaskManager()

    while True:
        print("\n========== TASKFLOW ==========")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Editar tarefa")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            prioridade = input("Prioridade (Alta, Média ou Baixa): ")

            gerenciador.adicionar_tarefa(
                titulo,
                descricao,
                prioridade
            )

            print("\n✅ Tarefa cadastrada com sucesso!")

        elif opcao == "2":
            gerenciador.listar_tarefas()

        elif opcao == "3":

            gerenciador.listar_tarefas()

            if gerenciador.quantidade_tarefas() == 0:
                continue

            numero = int(input("\nNúmero da tarefa: ")) - 1

            titulo = input("Novo título: ")
            descricao = input("Nova descrição: ")
            prioridade = input("Nova prioridade: ")

            if gerenciador.editar_tarefa(
                numero,
                titulo,
                descricao,
                prioridade
            ):
                print("\n✅ Tarefa atualizada!")
            else:
                print("\n❌ Tarefa não encontrada.")

        elif opcao == "4":
            print("\nEncerrando o sistema...")
            break

        else:
            print("\n❌ Opção inválida!")


if __name__ == "__main__":
    menu()
