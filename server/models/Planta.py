from sqlalchemy import text

class PlantaDAO:
    def __init__(self, conn):
        self.conn = conn
        
    # insert segun db.__init__.py
    
    def insert(self, estadoHumedad):
        query = f"INSERT INTO Planta (estadoHumedad) VALUES ('{estadoHumedad}');"
        
        try:
            with self.conn.connect() as connection:
                result_proxy = connection.execute(text(query))
                inserted_id = result_proxy.lastrowid
                connection.commit()
                return inserted_id
        except Exception as e:
            print(e, "Error en insert de PlantaDAO")
                
    def getById(self, idPlanta):
        query = f"SELECT * FROM Planta WHERE idPlanta = {idPlanta};"
        try:
            with self.conn.connect() as connection:
                result = connection.execute(text(query)).fetchone()
                result_dict = dict(result._mapping.items()) if result else None
                return result_dict

        except Exception as e:
            print(e, "Error en getById de PlantaDAO")
    
    def getAll(self):
        query = "SELECT * FROM planta;"
        try:
            with self.conn.connect() as connection:
                result = connection.execute(text(query)).fetchall()
                result_list = [dict(row._mapping.items()) for row in result]
                return result_list
        except Exception as e:
            print(e, "Error en getAll de PlantaDAO")