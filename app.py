from flask import Flask, jsonify, render_template
from flask_cors import CORS
from interface.livro_controller import LivroController

# O template_folder='.' é essencial porque seus arquivos estão na raiz
app = Flask(__name__, template_folder='.')
CORS(app)

controller = LivroController()

# --- ROTAS DE NAVEGAÇÃO (Para abrir as páginas HTML) ---

@app.route("/")
def index():
    # Agora a página inicial carrega o seu index.html em vez de um JSON
    return render_template('index.html')

@app.route("/compra")
def pagina_compra():
    # Essa rota resolve o problema de o compra.html não abrir
    return render_template('compra.html')

@app.route("/compras")
def pagina_historico():
    # Essa rota resolve o problema de o compras.html não abrir
    return render_template('compras.html')

# --- ROTAS DE API (Para processar os dados dos livros) ---

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

@app.route("/api/comprar/<int:id>", methods=['POST', 'GET'])
def comprar(id):
    livros = controller.listar_livros()
    if id < 0 or id >= len(livros):
        return jsonify({"erro": "Livro não encontrado"}), 404
    livro = livros[id]
    controller.comprar_livro(livro.nome, livro.preco)
    return jsonify({
        "mensagem": "Compra realizada com sucesso!",
        "livro": {"nome": livro.nome, "preco": livro.preco}
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
    # Configuração necessária para rodar corretamente no Azure
    app.run(host='0.0.0.0', port=5000)
