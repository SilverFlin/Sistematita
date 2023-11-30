class HumedadDAO:
    # conn
    def __init__(self, conn):
        self.conn = conn
        
    def insert(self, humedadActual, horaDeMedicion):
        query = f"INSERT INTO Humedad (humedadActual, horaDeMedicion) VALUES ({humedadActual}, '{horaDeMedicion}');"
        
        try:
            with self.conn.connect() as connection:
                result_proxy = connection.execute(text(query))
                inserted_id = result_proxy.lastrowid
                connection.commit()
               
                return inserted_id
            
        except Exception as e:
            print(e, "Error en insert de HumedadDAO")
            
        
    def getById(self, idHumedad):
        query = f"SELECT * FROM Humedad WHERE idHumedad = {idHumedad};"
        try:
            with self.conn.connect() as connection:
                result = connection.execute(text(query)).fetchone()
                result_dict = dict(result._mapping.items()) if result else None
                return result_dict
            
        except Exception as e:
            print(e, "Error en getById de HumedadDAO")
    
    def getAll(self):
        query = "SELECT * FROM Humedad;"
        try:
            with self.conn.connect() as connection:
                result = connection.execute(text(query)).fetchall()
                result_list = [dict(row._mapping.items()) for row in result]
                return result_list
        except Exception as e:
            print(e, "Error en getAll de HumedadDAO")
    
    def getHumedadActual(self):
        query = "SELECT humedadActual FROM Humedad ORDER BY idHumedad DESC LIMIT 1;"
        try:
            with self.conn.connect() as connection:
                result = connection.execute(text(query)).fetchone()
                result_dict = dict(result._mapping.items()) if result else None
                return result_dict
        except Exception as e:
            print(e, "Error en getHumedadActual de HumedadDAO")
    