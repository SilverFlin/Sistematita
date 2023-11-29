from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, ForeignKey, Enum
import os

load_dotenv()

user = 'root'
password = os.environ.get('DB_PASSWORD','root')
host = '127.0.0.1'
port = 3306
database = os.environ.get('DB_NAME','planta_db')

# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
    return create_engine(
    url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
    user, password, host, port, database
    )
)


def createTables(metadata, engine):
    # Bomba: Hora de llenado (fecha y hora), cantidadDeAgua (int)
    # Planta
    # Sistema: Hora de encendido (fecha y hora), hora de apagado (fecha y hora)
    # Huemdad: humedad actual (tres niveles de humedad, usar un enum), hora de medicion (fecha y hora)
    
    # Relaciones
    # Bomba - Planta: 1 a N
    # Planta - Sistema: N - 1
    # Planta - Humedad: 1 a N
    
    # Tablas
    Bomba = Table('Bomba', metadata,
        Column('idBomba', Integer, primary_key=True),
        Column('horaDeLlenado', DateTime),
        Column('cantidadDeAgua', Integer),
        
        # Ejemplo horaDeLlenado
        # 2020-11-11 12:00:00
        
        
    )
    
    Planta = Table('Planta', metadata,
        Column('idPlanta', Integer, primary_key=True),
        Column('nombre', String(50)),
        Column('idSistema', Integer, ForeignKey('Sistema.idSistema')),
        Column('idBomba', Integer, ForeignKey('Bomba.idBomba')),
    )
    
    Sistema = Table('Sistema', metadata,
        Column('idSistema', Integer, primary_key=True),
        Column('horaDeEncendido', DateTime),
        Column('horaDeApagado', DateTime),
    )
    
    Humedad = Table('Humedad', metadata,
        Column('idHumedad', Integer, primary_key=True),
        Column('humedadActual', Enum('Baja', 'Media', 'Alta')),
        Column('horaDeMedicion', DateTime),
        Column('idPlanta', Integer, ForeignKey('Planta.idPlanta'))
    )
                    
    
 
    
    print("Creating tables...")
    
    metadata.create_all(engine)
    
    
# def insertSistema(conn, horaDeEncendido, horaDeApagado):
#     conn.execute("INSERT INTO Sistema (horaDeEncendido, horaDeApagado) VALUES (%s, %s)", (horaDeEncendido, horaDeApagado))
    
# def insertBomba(conn, horaDeLlenado, cantidadDeAgua, idSistema):
#     conn.execute("INSERT INTO Bomba (horaDeLlenado, cantidadDeAgua) VALUES (%s, %s)", (horaDeLlenado, cantidadDeAgua))
#     conn.execute("UPDATE Planta SET idBomba = (SELECT idBomba FROM Bomba ORDER BY idBomba DESC LIMIT 1) WHERE idSistema = %s", (idSistema))
    
# def insertPlanta(conn, nombre, idSistema, idBomba):
#     conn.execute("INSERT INTO Planta (nombre, idSistema, idBomba) VALUES (%s, %s, %s)", (nombre, idSistema, idBomba))
    
# def insertHumedad(conn, humedadActual, horaDeMedicion):
#     conn.execute("INSERT INTO Humedad (humedadActual, horaDeMedicion) VALUES (%s, %s)", (humedadActual, horaDeMedicion))
#     conn.execute("UPDATE Planta SET idHumedad = (SELECT idHumedad FROM Humedad ORDER BY idHumedad DESC LIMIT 1) WHERE idSistema = %s", (idSistema))
    

# def insertFakeData(conn):
#     # Un sistema, una bomba, una planta, y varias temperaturas
#     # TODO
#     print('Inserting fake data...')
    
    
# export conn variable

engine = get_connection()
conn = engine.connect()



    

# if __name__ == '__main__':

#     try:
#     # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
#         engine = get_connection()
#         conn = engine.connect()
#         print("Connection Successful!")
#         # imprime las tablas
#         metadata = MetaData() #extracting the metadata
#         createTables(metadata, engine)
        
#         insertFakeData(conn)
#         # muestra las tablas
        
        
#     except Exception as ex:
#         print("Connection could not be made due to the following error: \n", ex)




