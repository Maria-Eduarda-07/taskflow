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
