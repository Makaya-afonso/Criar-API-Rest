from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados fictícios para a biblioteca
livros = [
    {'id': 1, 'titulo': '1984', 'autor': 'George Orwell'},
    {'id': 2, 'titulo': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien'},
    {'id': 3, 'titulo': 'O Pequeno Príncipe', 'autor': 'Antoine de Saint-Exupéry'},
    {'id': 4, 'titulo': 'Moby Dick', 'autor': 'Herman Melville'},
    {'id': 5, 'titulo': 'Orgulho e Preconceito', 'autor': 'Jane Austen'},
    {'id': 6, 'titulo': 'A Revolução dos Bichos', 'autor': 'George Orwell'},
    {'id': 7, 'titulo': 'O Hobbit', 'autor': 'J.R.R. Tolkien'},
    {'id': 8, 'titulo': 'O Sol é Para Todos', 'autor': 'Harper Lee'},
    {'id': 9, 'titulo': 'Dom Casmurro', 'autor': 'Machado de Assis'},
    {'id': 10, 'titulo': 'Cem Anos de Solidão', 'autor': 'Gabriel García Márquez'}
]

# Rota para obter todos os livros
@app.route('/livros', methods=['GET'])
def get_livros():
    return jsonify(livros)

# Rota para obter um livro pelo ID
@app.route('/livros/<int:id>', methods=['GET'])
def get_livro(id):
    livro = next((livro for livro in livros if livro['id'] == id), None)
    return jsonify(livro) if livro else ('', 404)

# Rota para adicionar um novo livro
@app.route('/livros', methods=['POST'])
def add_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(novo_livro), 201

# Rota para atualizar um livro existente
@app.route('/livros/<int:id>', methods=['PUT'])
def update_livro(id):
    livro = next((livro for livro in livros if livro['id'] == id), None)
    if livro:
        dados = request.get_json()
        livro.update(dados)
        return jsonify(livro)
    return ('', 404)

# Rota para deletar um livro
@app.route('/livros/<int:id>', methods=['DELETE'])
def delete_livro(id):
    global livros
    livros = [livro for livro in livros if livro['id'] != id]
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)
