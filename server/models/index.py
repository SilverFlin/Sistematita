# import conn
import models.Bomba as Bomba
import models.Contenedor as Contenedor
import models.Planta as Planta
import models.Sistema as Sistema
from db import engine




BombaDAO = Bomba.BombaDAO(engine)
ContenedorDAO = Contenedor.ContenedorDAO(engine)
PlantaDAO = Planta.PlantaDAO(engine)
SistemaDAO = Sistema.SistemaDAO(engine)

