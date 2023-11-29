class BombaDAO:
    # conn
    def __init__(self, conn):
        self.conn = conn
        
    def insert(self, horaDeLlenado, cantidadDeAgua):
        self.conn.execute("INSERT INTO Bomba (horaDeLlenado, cantidadDeAgua) VALUES (%s, %s)", (horaDeLlenado, cantidadDeAgua))
        return self.conn.execute("SELECT * FROM Bomba WHERE idBomba = %s", (idBomba)).fetchone()
        
    def getById(self, idBomba):
        return self.conn.execute("SELECT * FROM Bomba WHERE idBomba = %s", (idBomba)).fetchone()
    
    def getAll(self):
        try:
            return self.conn.execute("SELECT * FROM bomba").fetchall()   
        except Exception as e:
            print(e, "Error en getAll de BombaDAO")
            return 'Error en getAll de BombaDAO'    
        