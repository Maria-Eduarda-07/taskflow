class Task:
    """
    Representa uma tarefa do sistema.
    """

    def __init__(self, titulo, descricao, prioridade):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = "Pendente"

    def concluir(self):
        self.status = "Concluída"

    def __str__(self):
        return (
            f"Título: {self.titulo}\n"
            f"Descrição: {self.descricao}\n"
            f"Prioridade: {self.prioridade}\n"
            f"Status: {self.status}"
        )
