from src.task_manager import TaskManager


def test_adicionar_tarefa():
    gerenciador = TaskManager()

    gerenciador.adicionar_tarefa(
        "Estudar Python",
        "Aprender Pytest",
        "Alta"
    )

    assert gerenciador.quantidade_tarefas() == 1
