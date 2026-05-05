from flask import Flask, jsonify, render_template
from flask_cors import CORS
from interface.livro_controller import LivroController

# O template_folder='.' avisa ao Flask que os arquivos HTML estão na raiz
app = Flask(__name__, template_folder='.')

# O CORS permite que o Frontend acesse os dados da API sem bloqueios
CORS(app)

controller = LivroController()

# --- ROTAS DE PÁGINAS (FRONTEND) ---
# Essas rotas carregam os arquivos HTML que você subiu na raiz

@app.route("/")
def index():
    """Carrega a página principal da livraria"""
    return render_template('index.html')

@app.route("/compra")
def pagina_compra():
    """Carrega a página de confirmação de compra (recibo)"""
    return render_template('compra.html')

@app.route("/compras")
def pagina_historico():
    """Carrega a página do histórico de todas as compras"""
    return render_template('compras.html')


# --- ROTAS DE API (BACKEND) ---
# Essas rotas lidam com os dados e são chamadas pelo JavaScript do seu site

@app.route("/api/status", methods=['GET'])
def status():
    """Verificação rápida se o servidor está online"""
    return jsonify({
        "mensagem": "Servidor da Livraria online!",
        "status": "OK"
    })

@app.route("/api/livros", methods=['GET'])
def listar_livros():
    """Retorna a lista de livros disponível no catálogo"""
    livros_objetos = controller.listar_livros()
    livros_json = []
    for index, livro in enumerate(livros_objetos):
        livros_json.append({
            "id": index,
            "nome": livro.nome,
            "preco": livro.preco
        })
    return jsonify(livros_json)

@app.route("/api/comprar/<int:id>", methods=['POST', 'GET'])
def comprar(id):
    """Processa a compra de um livro específico pelo ID"""
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
    """Retorna o histórico de compras formatado em JSON"""
    compras_objetos = controller.listar_compras()
    compras_json = []
    for compra in compras_objetos:
        compras_json.append({
            "nome": compra.nome,
            "preco": compra.preco
        })
    return jsonify({"historico_compras": compras_json})


if __name__ == "__main__":
    # No Azure, o servidor ignora o debug=True e a porta 5000, 
    # mas mantemos aqui para você testar localmente se precisar.
    app.run(debug=True, port=5000)
