
from Persona import Persona

class Tecnico(Persona):

   def __init__(self, nombres, apellidos, funcion):
      super().__init__(nombres, apellidos)
      self.__funcion = funcion

   def getFuncion(self):
      return self.__funcion

   def validatDatos(self):
      output = [True, ""]
      if (self.getNombres() == "" or self.getApellidos() == "" or self.__funcion == ""):
         output[0] = False
         output[1] = "\nNinguno de los datos del miembro del cuerpo tecnico puede estar vacío...\n"
      return output