from flask import Flask, jsonify, request
import json

app = Flask(__name__)

monsters = []

# Lista de mobs
with open('mobs.json', 'r') as file:
    monsters = json.load(file)

# Rota para obter todos os mobs
@app.route('/monsters', methods=['GET'])
def get_monsters():
    return jsonify({'monsters': monsters})

# Rota para obter informações sobre um mob específico
@app.route('/monsters/<int:monster_id>', methods=['GET'])
def get_monster(monster_id):
    monster = next((m for m in monsters if m['id'] == monster_id), None)
    if monster:
        return jsonify({'monster': monster})
    return jsonify({'message': 'Mob não encontrado'}), 404

# Rota para adicionar um novo mob
@app.route('/monsters', methods=['POST'])
def add_monster():
    new_monster = request.get_json()
    new_monster['id'] = len(monsters) + 1
    monsters.append(new_monster)
    return jsonify({'message': 'Mob adicionado com sucesso'}), 201

# Rota para atualizar informações de um mob
@app.route('/monsters/<int:monster_id>', methods=['PUT'])
def update_monster(monster_id):
    monster = next((m for m in monsters if m['id'] == monster_id), None)
    if monster:
        updated_monster = request.get_json()
        monster.update(updated_monster)
        return jsonify({'message': 'Mob atualizado com sucesso'})
    return jsonify({'message': 'Mob não encontrado'}), 404

# Rota para excluir um mob
@app.route('/monsters/<int:monster_id>', methods=['DELETE'])
def delete_monster(monster_id):
    global monsters
    monsters = [m for m in monsters if m['id'] != monster_id]
    return jsonify({'message': 'Mob excluído com sucesso'})

if __name__ == '__main__':
    app.run(debug=True)
