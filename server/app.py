from flask import Flask, request, redirect, url_for, flash, jsonify
from models.index import BombaDAO, HumedadDAO, PlantaDAO, SistemaDAO







app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world!'

@app.route('/bomba', methods=['GET', 'POST'])
def bomba():
    if request.method == 'POST':
        horaDeLlenado = request.form['horaDeLlenado']
        cantidadDeAgua = request.form['cantidadDeAgua']
        return BombaDAO.insert(horaDeLlenado, cantidadDeAgua)
        
    elif request.method == 'GET':
        return BombaDAO.getAll()
    
@app.route('/bomba/<int:idBomba>', methods=['GET'])
def bombaById(idBomba):
    return BombaDAO.getById(idBomba)

@app.route('/humedad', methods=['GET', 'POST'])
def humedad():
    if request.method == 'POST':
        humedadActual = request.form['humedadActual']
        horaDeMedicion = request.form['horaDeMedicion']
        return HumedadDAO.insert(humedadActual, horaDeMedicion)
        
    elif request.method == 'GET':
        return HumedadDAO.getAll()
    
@app.route('/humedad/<int:idHumedad>', methods=['GET'])
def humedadById(idHumedad):
    return HumedadDAO.getById(idHumedad)

@app.route('/planta', methods=['GET', 'POST'])
def planta():
    if request.method == 'POST':
        nombre = request.form['nombre']
        return PlantaDAO.insert(nombre)
        
    elif request.method == 'GET':
        return PlantaDAO.getAll()
    
@app.route('/planta/<int:idPlanta>', methods=['GET'])
def plantaById(idPlanta):
    return PlantaDAO.getById(idPlanta)

@app.route('/sistema', methods=['GET', 'POST'])
def sistema():
    if request.method == 'POST':
        hora_de_encendido = request.form['horaDeEncendido']
        hora_de_apagado = request.form['horaDeApagado']
        
        inserted_id = SistemaDAO.insert(hora_de_encendido, hora_de_apagado)

        # Returning a JSON response
        return jsonify({"message": "Record inserted successfully", "id": inserted_id})    
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










if __name__ == '__main__':
    app.run(debug=True)
    