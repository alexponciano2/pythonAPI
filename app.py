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


# Rota para obter informações sobre um mob específico pelo level
@app.route('/monsters/level/<int:monster_level>', methods=['GET'])
def get_monster_by_level(monster_level):
    monsters_by_level = [m for m in monsters if m['Level'] == monster_level]
    if monsters_by_level:
        return jsonify({'monsters': monsters_by_level})
    return jsonify({'message': 'Nenhum mob encontrado para o nível especificado'}), 404

