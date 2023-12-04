from flask import Flask, request, redirect, url_for, flash, jsonify
from models.index import BombaDAO, ContenedorDAO, PlantaDAO, SistemaDAO







app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world!'

@app.route('/bomba', methods=['GET', 'POST'])
def bomba():
    if request.method == 'POST':
        duracionEnSegundos = request.json['duracionEnSegundos']        
        inserted_id = BombaDAO.insert(duracionEnSegundos)

        return jsonify({"message": "Record inserted successfully", "id": inserted_id})
        
    elif request.method == 'GET':
        result = BombaDAO.getAll()
        if result is not None:
            return jsonify(result)
        else:
            return jsonify({"error": "No data found"}), 404
    
@app.route('/bomba/<int:idBomba>', methods=['GET'])
def bombaById(idBomba):
    result = BombaDAO.getById(idBomba)

    if result is not None:
        return jsonify(result)
    else:
        return jsonify({"error": "No data found"}), 404

@app.route('/planta', methods=['GET', 'POST'])
def planta():
    if request.method == 'POST':
        estadoHumedad = request.json['estadoHumedad']
        
        inserted_id = PlantaDAO.insert(estadoHumedad)

        return jsonify({"message": "Record inserted successfully", "id": inserted_id})
        
    elif request.method == 'GET':
        result = PlantaDAO.getAll()
        if result is not None:
            return jsonify(result)
        else:
            return jsonify({"error": "No data found"}), 404 

        
@app.route('/planta/<int:idPlanta>', methods=['GET'])
def plantaById(idPlanta):
    result = PlantaDAO.getById(idPlanta)

    if result is not None:
        return jsonify(result)
    else:
        return jsonify({"error": "No data found"}), 404

@app.route('/sistema', methods=['GET', 'POST'])
def sistema():
    if request.method == 'POST':
        estado = request.json['estado']
        
        inserted_id = SistemaDAO.insert(estado)
        
        if inserted_id is not None:
            return jsonify({"message": "Record inserted successfully", "id": inserted_id})
        else:
            return jsonify({"error": "No data found"}), 404

    elif request.method == 'GET':
        result = SistemaDAO.getAll()
        if result is not None:
            return jsonify(result)
        else:
            return jsonify({"error": "No data found"}), 404 
    
@app.route('/sistema/<int:idSistema>', methods=['GET'])
def sistemaById(idSistema):
    result = SistemaDAO.getById(idSistema)

    if result is not None:
        return jsonify(result)
    else:
        return jsonify({"error": "No data found"}), 404
    
@app.route('/contenedor', methods=['GET', 'POST'])
def contenedor():
    if request.method == 'POST':
        estado = request.json['estado']
        
        inserted_id = ContenedorDAO.insert(estado)

        return jsonify({"message": "Record inserted successfully", "id": inserted_id})
        
    elif request.method == 'GET':
        result = ContenedorDAO.getAll()
        if result is not None:
            return jsonify(result)
        else:
            return jsonify({"error": "No data found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    