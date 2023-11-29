# import conn
import models.Bomba as Bomba
import models.Humedad as Humedad
import models.Planta as Planta
import models.Sistema as Sistema
from db import conn




BombaDAO = Bomba.BombaDAO(conn)
HumedadDAO = Humedad.HumedadDAO(conn)
PlantaDAO = Planta.PlantaDAO(conn)
SistemaDAO = Sistema.SistemaDAO(conn)

