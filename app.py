from flask import Flask, jsonify
from flask_cors import CORS
from interface.livro_controller import LivroController

app = Flask(__name__)
# O CORS é obrigatório na Arquitetura Cliente-Servidor para liberar o acesso do Front-end
CORS(app)

controller = LivroController()


# Rota Base: Evita o erro 404 e avisa que a API está online
@app.route("/", methods=['GET'])
def home():
    return jsonify({
        "mensagem": "API da Livraria rodando perfeitamente!",
        "dica": "Acesse /api/livros para ver o catálogo de livros."
    })


# Rota 1: Retorna o catálogo de livros
@app.route("/api/livros", methods=['GET'])
def listar_livros():
    livros_objetos = controller.listar_livros()

    livros_json = []
    for index, livro in enumerate(livros_objetos):
        livros_json.append({
            "id": index,
            "nome": livro.nome,
            "preco": livro.preco
        })

    return jsonify(livros_json)


# Rota 2: Processa a compra de um livro
@app.route("/api/comprar/<int:id>", methods=['POST', 'GET'])
def comprar(id):
    livros = controller.listar_livros()

    if id < 0 or id >= len(livros):
        return jsonify({"erro": "Livro não encontrado"}), 404

    livro = livros[id]

    controller.comprar_livro(livro.nome, livro.preco)

    return jsonify({
        "mensagem": "Compra realizada com sucesso!",
        "livro": {
            "nome": livro.nome,
            "preco": livro.preco
        }
    })


# Rota 3: Retorna o histórico de compras CORRIGIDO PARA OBJETOS
@app.route("/api/compras", methods=['GET'])
def listar_compras():
    compras_objetos = controller.listar_compras()

    compras_json = []
    for compra in compras_objetos:
        # Como o seu Clean Architecture já devolve objetos, é só pegar os atributos direto:
        compras_json.append({
            "nome": compra.nome,
            "preco": compra.preco
        })

    return jsonify({"historico_compras": compras_json})


if __name__ == "__main__":
    app.run(debug=True, port=5000)