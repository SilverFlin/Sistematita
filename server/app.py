from flask import Flask, request, redirect, url_for, flash
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
        horaDeEncendido = request.form['horaDeEncendido']
        horaDeApagado = request.form['horaDeApagado']
        return SistemaDAO.insert(horaDeEncendido, horaDeApagado)
        
    elif request.method == 'GET':
        return SistemaDAO.getAll()
    
@app.route('/sistema/<int:idSistema>', methods=['GET'])
def sistemaById(idSistema):
    return SistemaDAO.getById(idSistema)









if __name__ == '__main__':
    app.run(debug=True)
    