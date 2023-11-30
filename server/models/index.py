# import conn
import models.Bomba as Bomba
import models.Humedad as Humedad
import models.Planta as Planta
import models.Sistema as Sistema
from db import engine




BombaDAO = Bomba.BombaDAO(engine)
HumedadDAO = Humedad.HumedadDAO(engine)
PlantaDAO = Planta.PlantaDAO(engine)
SistemaDAO = Sistema.SistemaDAO(engine)

