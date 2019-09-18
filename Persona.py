
class Persona:

   def __init__(self, nombres, apellidos):
      self.__nombres = nombres
      self.__apellidos = apellidos

   def getNombres(self):
      return self.__nombres

   def getApellidos(self):
      return self.__apellidos
