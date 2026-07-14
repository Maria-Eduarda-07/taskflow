from task_manager import TaskManager


def menu():
    gerenciador = TaskManager()

    while True:
        print("\n========== TASKFLOW ==========")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Sair")

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
            print("\nEncerrando o sistema...")
            break

        else:
            print("\n❌ Opção inválida!")


if __name__ == "__main__":
    menu()
