from entities.livro import Livro

class LivroRepositoryTXT:

    def listar(self):
        livros = []

        try:
            with open("livros.txt", "r") as f:
                for linha in f:
                    nome, preco = linha.strip().split(",")
                    livros.append(Livro(nome, float(preco)))
        except FileNotFoundError:
            pass

        if not livros:
            livros = [
                Livro("Python", 50),
                Livro("Engenharia", 70),
                Livro("Morro", 50)
            ]

        return livros

    # salvar compra (histórico)
    def salvar(self, livro):
        with open("compras.txt", "a") as f:
            f.write(f"{livro.nome},{livro.preco}\n")

    #  listar compras
    def listar_compras(self):
        compras = []

        try:
            with open("compras.txt", "r") as f:
                for linha in f:
                    nome, preco = linha.strip().split(",")
                    compras.append(Livro(nome, float(preco)))
        except FileNotFoundError:
            pass

        return compras