from sqlalchemy import text

class ContenedorDAO:
    def __init__(self, conn):
        self.conn = conn
        
    def insert(self, estado):
        query = f"INSERT INTO contenedor (estado) VALUES ('{estado}');"
        
        try:
            with self.conn.connect() as connection:
                result_proxy = connection.execute(text(query))
                inserted_id = result_proxy.lastrowid
                connection.commit()
               
                return inserted_id
            
        except Exception as e:
            print(e, "Error en insert de ContenedorDAO")
            
        
    def getById(self, idContenedor):
        query = f"SELECT * FROM contenedor WHERE idContenedor = {idContenedor};"
        try:
            with self.conn.connect() as connection:
                result = connection.execute(text(query)).fetchone()
                result_dict = dict(result._mapping.items()) if result else None
                return result_dict
            
        except Exception as e:
            print(e, "Error en getById de ContenedorDAO")
    
    def getAll(self):
        query = "SELECT * FROM contenedor;"
        try:
            with self.conn.connect() as connection:
                result = connection.execute(text(query)).fetchall()
                result_list = [dict(row._mapping.items()) for row in result]
                return result_list
        except Exception as e:
            print(e, "Error en getAll de ContenedorDAO")
    
    