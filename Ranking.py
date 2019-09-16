
class Ranking:

   def __init__(self):
      self.__lista = [None, None, None, None, None]

   def evaluarJugador(self, jugador):
      for i in range(5):
         if (self.__lista[i] != None):
            if (jugador.getSkill() > self.__lista[i].getSkill()):
               if (i == 4):
                  self.__lista[i] = jugador
               else:
                  temp = self.__lista[i]
                  self.__lista[i] = jugador
                  self.evaluarJugador(temp)
                  break
         else:
            self.__lista[i] = jugador
            break

   def getLista(self):
      return self.__lista
