from sqlalchemy import text
import datetime

class SistemaDAO:
    def __init__(self, conn):
        self.conn = conn
        
    def insert(self, horaDeEncendido, horaDeApagado):
        # string template
        query = f"INSERT INTO sistema (horaDeEncendido, horaDeApagado) VALUES ('{horaDeEncendido}', '{horaDeApagado}');"
        # query = "INSERT INTO sistema (horaDeEncendido, horaDeApagado) VALUES (:horaDeEncendido, :horaDeApagado);"
        
        try:
            return self.conn.execute(text(query))
            # return self.conn.execute("SELECT * FROM sistema ORDER BY idSistema DESC LIMIT 1").fetchone()
        except Exception as e:
            print(e, "Error en insert de SistemaDAO")
            return 'Error en insert de SistemaDAO'
        
    def getById(self, idSistema):
        query = "SELECT * FROM sistema WHERE idSistema = :idSistema;"
        try:
            return self.conn.execute(text(query), idSistema=idSistema).fetchone()
        except Exception as e:
            print(e, "Error en getById de SistemaDAO")
            return 'Error en getById de SistemaDAO'
    def getAll(self):
        query = "SELECT * FROM sistema;"
        try:
            return self.conn.execute(text(query)).fetchall()
        except Exception as e:
            print(e, "Error en getAll de SistemaDAO")
            return 'Error en getAll de SistemaDAO'
    
    
    