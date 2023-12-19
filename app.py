from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de monstros como um exemplo
monsters = [
    {"name": "Devil Shadow of Devah", "level": 1, "details": "Um monstro sombrio."},
    {"name": "Dawn Shadow of Devah", "level": 2, "details": "Um monstro da alvorada."}
]

@app.route('/buscar_monstro', methods=['GET'])
def buscar_monstro():
    level_monstro = request.args.get('level_monstro')

    # Verifique se o parâmetro level_monstro é um número inteiro
    try:
        level_monstro = int(level_monstro)
    except ValueError:
        return jsonify({"error": "O nível do monstro deve ser um número inteiro"}), 400

    # Lógica para buscar detalhes do monstro pelo nível
    detalhes_do_monstro = None
    for monster in monsters:
        if monster['level'] == level_monstro:
            detalhes_do_monstro = {
                "name": monster["name"],
                "level": monster["level"],
                "details": monster["details"]
            }
            break

    if detalhes_do_monstro:
        return jsonify(detalhes_do_monstro)
    else:
        return jsonify({"error": "Monstro não encontrado para o nível especificado"}), 404

# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)