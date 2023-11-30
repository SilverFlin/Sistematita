class BombaDAO:
    # conn
    def __init__(self, conn):
        self.conn = conn
        
    def insert(self, horaDeLlenado, cantidadDeAgua):
        query = f"INSERT INTO Bomba (horaDeLlenado, cantidadDeAgua) VALUES ('{horaDeLlenado}', {cantidadDeAgua});"
        
        try:
            with self.conn.connect() as connection:
                result_proxy = connection.execute(text(query))
                inserted_id = result_proxy.lastrowid
                connection.commit()
               
                return inserted_id
            
        except Exception as e:
            print(e, "Error en insert de BombaDAO")
            
    def getById(self, idBomba):
        query = f"SELECT * FROM Bomba WHERE idBomba = {idBomba};"
        try:
            with self.conn.connect() as connection:
                result = connection.execute(text(query)).fetchone()
                result_dict = dict(result._mapping.items()) if result else None
                return result_dict
        
        except Exception as e:
            print(e, "Error en getById de BombaDAO")
            
    
    def getAll(self):
        query = "SELECT * FROM Bomba;"
        try:
            with self.conn.connect() as connection:
                result = connection.execute(text(query)).fetchall()
                result_list = [dict(row._mapping.items()) for row in result]
                return result_list
        except Exception as e:
            print(e, "Error en getAll de BombaDAO")
        