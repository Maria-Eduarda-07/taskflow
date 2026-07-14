from task import Task


class TaskManager:
    """
    Responsável por gerenciar as tarefas do sistema.
    """

    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, titulo, descricao, prioridade):
        tarefa = Task(titulo, descricao, prioridade)
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        if not self.tarefas:
            print("\nNenhuma tarefa cadastrada.\n")
            return

        print("\n===== LISTA DE TAREFAS =====")
        for indice, tarefa in enumerate(self.tarefas, start=1):
            print(f"\nTarefa {indice}")
            print(tarefa)
            print("-" * 30)

    def quantidade_tarefas(self):
        return len(self.tarefas)

    def editar_tarefa(self, indice, titulo, descricao, prioridade):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice] = Task(titulo, descricao, prioridade)
            return True
        return False

    def excluir_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas.pop(indice)
            return True
        return False

    def concluir_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].concluir()
            return True
        return False


def menu():
    gerenciador = TaskManager()

    while True:
        print("\n========== TASKFLOW ==========")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Editar tarefa")
        print("4 - Excluir tarefa")
        print("5 - Concluir tarefa")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            prioridade = input("Prioridade (Alta, Média ou Baixa): ")
            gerenciador.adicionar_tarefa(titulo, descricao, prioridade)
            print("\n✅ Tarefa cadastrada com sucesso!")

        elif opcao == "2":
            gerenciador.listar_tarefas()

        elif opcao == "3":
            gerenciador.listar_tarefas()
            if gerenciador.quantidade_tarefas() == 0:
                continue

            try:
                numero = int(
                    input("\nNúmero da tarefa que deseja editar: ")) - 1
                titulo = input("Novo título: ")
                descricao = input("Nova descrição: ")
                prioridade = input("Nova prioridade (Alta, Média ou Baixa): ")

                if gerenciador.editar_tarefa(numero, titulo, descricao, prioridade):
                    print("\n✅ Tarefa atualizada com sucesso!")
                else:
                    print("\n❌ Tarefa não encontrada.")
            except ValueError:
                print("\n❌ Por favor, digite um número válido!")

        elif opcao == "4":
            gerenciador.listar_tarefas()
            if gerenciador.quantidade_tarefas() == 0:
                continue

            try:
                numero = int(
                    input("\nNúmero da tarefa que deseja excluir: ")) - 1

                if gerenciador.excluir_tarefa(numero):
                    print("\n✅ Tarefa excluída com sucesso!")
                else:
                    print("\n❌ Tarefa não encontrada.")
            except ValueError:
                print("\n❌ Por favor, digite um número válido!")

        elif opcao == "5":
            gerenciador.listar_tarefas()
            if gerenciador.quantidade_tarefas() == 0:
                continue

            try:
                numero = int(
                    input("\nNúmero da tarefa que deseja concluir: ")) - 1

                if gerenciador.concluir_tarefa(numero):
                    print("\n✅ Tarefa marcada como concluída!")
                else:
                    print("\n❌ Tarefa não encontrada.")
            except ValueError:
                print("\n❌ Por favor, digite um número válido!")

        elif opcao == "6":
            print("\nEncerrando o sistema...")
            break
        else:
            print("\n❌ Opção inválida!")


if __name__ == "__main__":
    menu()
