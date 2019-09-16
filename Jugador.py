
from Persona import Persona

class Jugador(Persona):

   def __init__(self, nombres, apellidos, club, posicion, numero, skill, nacionaldiad):
      super().__init__(nombres, apellidos)
      self.__club = club
      self.__posicion = posicion
      self.__numero = numero
      self.__skill = skill
      self.__nacionalidad = nacionaldiad

   def validarDatos(self):
      output = [True, ""]
      if(self.__skill < 50 or self.__skill > 100):
         output[0] = False
         output[1] = "\nEl valor de skill debe estar entre 50 y 100...\n"
      if (self.__numero <= 0):
         output[0] = False
         output[1] = "\nEl número del jugador debe ser positivo y diferente de cero...\n"
      if (self.getNombres() == "" or self.getApellidos() == "" or self.__club == "" or self.__posicion == ""):
         output[0] = False
         output[1] = "\nNinguno de los datos del jugador puede estar vacío...\n"
      return output

   def getClub(self):
      return self.__club

   def getPosicion(self):
      return self.__posicion

   def getNumero(self):
      return self.__numero

   def getSkill(self):
      return self.__skill

   def getNacionalidad(self):
      return self.__nacionalidad


