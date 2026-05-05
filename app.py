from flask import Flask, jsonify
from flask_cors import CORS
from interface.livro_controller import LivroController

app = Flask(__name__)

# Libera acesso do front (Azure)
CORS(app, resources={r"/*": {"origins": "*"}})

controller = LivroController()

# ==========================================================
# --- ROTA BASE (TESTE DA API) ---
# ==========================================================

@app.route("/")
def home():
    return jsonify({
        "mensagem": "API da Livraria rodando 🚀"
    })

# ==========================================================
# --- ROTAS DE API ---
# ==========================================================

# Rota 1: Listar livros
@app.route("/api/livros", methods=['GET'])
def listar_livros():
    livros_objetos = controller.listar_livros()

    return jsonify([
        {
            "id": i,
            "nome": livro.nome,
            "preco": livro.preco
        }
        for i, livro in enumerate(livros_objetos)
    ])

# Rota 2: Comprar livro
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

# Rota 3: Histórico de compras
@app.route("/api/compras", methods=['GET'])
def listar_compras():
    compras_objetos = controller.listar_compras()

    return jsonify({
        "historico_compras": [
            {
                "nome": compra.nome,
                "preco": compra.preco
            }
            for compra in compras_objetos
        ]
    })

# ==========================================================
# --- INICIALIZAÇÃO ---
# ==========================================================

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
