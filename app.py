from flask import Flask, jsonify, render_template
from flask_cors import CORS
from interface.livro_controller import LivroController

app = Flask(__name__, template_folder='.')
CORS(app)
controller = LivroController()

# --- ROTAS DE PÁGINA (FRONTEND) ---
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/compra")
def pagina_compra():
    return render_template('compra.html')

@app.route("/compras")
def pagina_historico():
    return render_template('compras.html')

# --- ROTAS DE API (BACKEND) ---
@app.route("/api/livros", methods=['GET'])
def listar_livros():
    livros_objetos = controller.listar_livros()
    return jsonify([{"id": i, "nome": l.nome, "preco": l.preco} for i, l in enumerate(livros_objetos)])

@app.route("/api/comprar/<int:id>", methods=['POST', 'GET'])
def comprar(id):
    livros = controller.listar_livros()
    if id < 0 or id >= len(livros): return jsonify({"erro": "Não encontrado"}), 404
    livro = livros[id]
    controller.comprar_livro(livro.nome, livro.preco)
    return jsonify({"mensagem": "Sucesso!", "livro": {"nome": livro.nome, "preco": livro.preco}})

@app.route("/api/compras", methods=['GET'])
def listar_compras():
    compras = controller.listar_compras()
    return jsonify({"historico_compras": [{"nome": c.nome, "preco": c.preco} for c in compras]})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
