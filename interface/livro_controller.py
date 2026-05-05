from use_cases.livro_usecase import LivroUseCase
from infra.livro_repository_txt import LivroRepositoryTXT
from entities.livro import Livro

class LivroController:
    def __init__(self):
        repo = LivroRepositoryTXT()
        self.usecase = LivroUseCase(repo)

    def listar_livros(self):
        return self.usecase.listar_livros()

    def comprar_livro(self, nome, preco):
        livro = Livro(nome, preco)
        self.usecase.comprar_livro(livro)

    def listar_compras(self):
        return self.usecase.listar_compras()