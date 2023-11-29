class PlantaDAO:
    def __init__(self, conn):
        self.conn = conn
        
    # insert, getbyid, getall
    
    def insert(self, nombre, idSistema, idBomba):
        self.conn.execute("INSERT INTO Planta (nombre, idSistema, idBomba) VALUES (%s, %s, %s)", (nombre, idSistema, idBomba))
        
    def getById(self, idPlanta):
        return self.conn.execute("SELECT * FROM Planta WHERE idPlanta = %s", (idPlanta)).fetchone()
    
    def getAll(self):
        return self.conn.execute("SELECT * FROM Planta").fetchall()