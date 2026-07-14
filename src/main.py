from task_manager import TaskManager


gerenciador = TaskManager()

gerenciador.adicionar_tarefa(
    "Fazer relatório",
    "Escrever documentação",
    "Alta"
)

gerenciador.adicionar_tarefa(
    "Criar testes",
    "Implementar testes unitários",
    "Média"
)

gerenciador.listar_tarefas()
