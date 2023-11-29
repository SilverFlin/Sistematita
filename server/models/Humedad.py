class HumedadDAO:
    # conn
    def __init__(self, conn):
        self.conn = conn
        
    def insert(self, humedadActual, horaDeMedicion):
        self.conn.execute("INSERT INTO Humedad (humedadActual, horaDeMedicion) VALUES (%s, %s)", (humedadActual, horaDeMedicion))
        
    def getById(self, idHumedad):
        return self.conn.execute("SELECT * FROM Humedad WHERE idHumedad = %s", (idHumedad)).fetchone()
    
    def getAll(self):
        return self.conn.execute("SELECT * FROM Humedad").fetchall()
    
    def getHumedadActual(self):
        return self.conn.execute("SELECT humedadActual FROM Humedad ORDER BY idHumedad DESC LIMIT 1").fetchone()
    