from flask import Flask, jsonify, render_template
from flask_cors import CORS
from interface.livro_controller import LivroController

# template_folder='.' busca os arquivos HTML na raiz do repositório no Azure
app = Flask(__name__)

# CORS libera o acesso do Front-end (rodando no navegador) ao Back-end
CORS(app, resources={r"/*": {"origins": "*"}})

controller = LivroController()

# ==========================================================
# --- ROTAS DE PÁGINA (FRONTEND - Carregam o Visual) ---
# ==========================================================

@app.route("/")
def index():
    """Rota raiz que carrega a página inicial da livraria."""
    return render_template('index.html')

@app.route("/compra")
def pagina_compra():
    """Rota que carrega a página de confirmação (recibo)."""
    return render_template('compra.html')

@app.route("/compras")
def pagina_historico():
    """Rota que carrega a página do histórico."""
    return render_template('compras.html')

# ==========================================================
# --- ROTAS DE API (BACKEND - Processam Dados) ---
# ==========================================================

# Rota 1: Retorna o catálogo de livros em JSON
@app.route("/api/livros", methods=['GET'])
def listar_livros():
    livros_objetos = controller.listar_livros()
    return jsonify([{"id": i, "nome": l.nome, "preco": l.preco} for i, l in enumerate(livros_objetos)])

# Rota 2: Processa a compra de um livro (RECEBE ID NA URL)
@app.route("/api/comprar/<int:id>", methods=['POST', 'GET'])
def comprar(id):
    livros = controller.listar_livros()

    # Validação de segurança
    if id < 0 or id >= len(livros):
        return jsonify({"erro": "Livro não encontrado"}), 404

    # Pega o livro correspondente ao ID
    livro = livros[id]

    # Executa a lógica de compra (provavelmente salvando em um banco/arquivo)
    controller.comprar_livro(livro.nome, livro.preco)

    return jsonify({
        "mensagem": "Sucesso!",
        "livro": {
            "nome": livro.nome,
            "preco": livro.preco
        }
    })

# Rota 3: Retorna o histórico de compras em JSON
@app.route("/api/compras", methods=['GET'])
def listar_compras():
    compras_objetos = controller.listar_compras()
    return jsonify({"historico_compras": [{"nome": c.nome, "preco": c.preco} for c in compras_objetos]})

# ==========================================================
# --- INICIALIZAÇÃO DO SERVIDOR ---
# ==========================================================

if __name__ == "__main__":
    # Host '0.0.0.0' é necessário para o Azure reconhecer a aplicação
    # O Azure ignora a porta 5000, mas mantemos para teste local.
    app.run(host='0.0.0.0', port=5000)
