class LivroUseCase:
    def __init__(self, repo):
        self.repo = repo

    def listar_livros(self):
        return self.repo.listar()

    def comprar_livro(self, livro):
        self.repo.salvar(livro)

    def listar_compras(self):
        return self.repo.listar_compras()