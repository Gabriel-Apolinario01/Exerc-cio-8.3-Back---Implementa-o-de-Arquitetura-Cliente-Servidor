from flask import Flask, jsonify, render_template
from flask_cors import CORS
from interface.livro_controller import LivroController

# O template_folder='.' busca os arquivos HTML na raiz do repositório
app = Flask(__name__, template_folder='.')
CORS(app)

controller = LivroController()

# --- NAVEGAÇÃO (Caminhos para o navegador abrir as páginas) ---

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/compra")
def pagina_compra():
    return render_template('compra.html')

@app.route("/compras")
def pagina_historico():
    return render_template('compras.html')


# --- API (Caminhos que o JavaScript usa para pegar dados) ---

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

# CORREÇÃO AQUI: Adicionado <int:id> para o Flask receber o número do livro
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

@app.route("/api/compras", methods=['GET'])
def listar_compras():
    compras_objetos = controller.listar_compras()
    compras_json = []
    for compra in compras_objetos:
        compras_json.append({
            "nome": compra.nome,
            "preco": compra.preco
        })
    return jsonify({"historico_compras": compras_json})


if __name__ == "__main__":
    # O host '0.0.0.0' garante que o Azure consiga "enxergar" a aplicação
    app.run(host='0.0.0.0', port=5000)
