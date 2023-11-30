from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, ForeignKey, Enum
import os
from sqlalchemy.sql import func

load_dotenv()

user = 'root'
password = os.environ.get('DB_PASSWORD','root')
host = '127.0.0.1'
port = 3306
database = os.environ.get('DB_NAME','planta_db')

def get_connection():
    return create_engine(
    url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
    user, password, host, port, database
    )
)


def createTables(metadata, engine):

    Bomba = Table('Bomba', metadata,
        Column('idBomba', Integer, primary_key=True),
        Column('horaDeEncendido', DateTime, server_default=func.now()),
        Column('duracionEnSegundos', Integer),
    )
    
    Planta = Table('Planta', metadata,
        Column('idPlanta', Integer, primary_key=True),
        Column('horaDeRegistro', DateTime, server_default=func.now()),
        Column('estadoHumedad', Enum('Baja', 'Media', 'Alta')),   
    )
    
    Sistema = Table('Sistema', metadata,
        Column('idSistema', Integer, primary_key=True),
        Column('horadeRegistro', DateTime, server_default=func.now()),
        Column('estado', Enum('Encendido', 'Apagado')),
    )
    
    Contenedor = Table('Contenedor', metadata,
        Column('idContenedor', Integer, primary_key=True),
        Column('horaRegistro', DateTime, server_default=func.now()),
        Column('estado', Enum('lleno', 'vacio', 'medio')),
    )
    
    metadata.create_all(engine)
        
engine = get_connection()
conn = engine.connect()
metadata = MetaData()


if not engine.dialect.has_table(conn, "Bomba"):
    createTables(metadata, engine)
    print("Tables created")
else:
    print("Tables already exist")
    
createTables(metadata, engine)