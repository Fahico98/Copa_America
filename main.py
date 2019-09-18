
from Jugador import Jugador
from Tecnico import Tecnico
from Ranking import Ranking

selecciones = {}
mejoresJugadores = Ranking()

def regSeleccion():
   while(True):
      seleccion = input("Nombre de la selección: ")
      if(seleccion != ""):
         selecciones[seleccion.lower().title()] = {"jugadores" : [], "tecnico" : []}
         print("\n***** OPERACIÓN EXITOSA *****\n")
         break
      else:
         print("\nNombre del país no valido...\n")
         continue

def regJugador():
   seleccion = input("\nIngrese el nombre de la selección a la cual desea agregar un jugador: ")
   if (seleccion.lower().title() in selecciones):
      while (True):
         nombres = input("  Nombres: ")
         apellidos = input("  Apellidos: ")
         club = input("  Club: ")
         posicion = input("  Posición: ")
         numero = input("  Número: ")
         skill = input("  Skill: ")
         numero = 0 if (numero == "") else int(numero)
         skill = 0 if (skill == "") else int(skill)
         jugador = Jugador(
            nombres.lower().title(),
            apellidos.lower().title(),
            club.lower().title(),
            posicion.lower().title(),
            numero,
            skill,
            seleccion.lower().title()
         )
         numeroRepetido = False
         validacion = [None, None]
         for jugador in selecciones[seleccion.lower().title()]["jugadores"]:
            if(jugador.getNumero() == numero):
               numeroRepetido = True
               break
         if(numeroRepetido):
            validacion[0] = False
            validacion[1] = "\nEl numero que ingresó para el jugador ya existe en la selección...\n"
         else:
            validacion = jugador.validarDatos()
         if(validacion[0]):
            selecciones[seleccion.lower().title()]["jugadores"].append(jugador)
            mejoresJugadores.evaluarJugador(jugador)
            print("\n***** OPERACIÓN EXITOSA *****\n")
            break
         else:
            print(validacion[1])
            continue
   else:
      print("\nEl nombre de la selección que ha ingresado no existe en la base de datos...\n")

def regTecnico():
   seleccion = input("\nIngrese el nombre de la selección a la cual desea agregar un miembro del cuerpo técnico: ")
   if (seleccion.lower().title() in selecciones):
      while(True):
         nombres = input("  Nombres: ")
         apellidos = input("  Apellidos: ")
         funcion = input("  Función dentro del equipo: ")
         tecnico = Tecnico(
            nombres.lower().title(),
            apellidos.lower().title(),
            funcion.lower().title()
         )
         validacion = tecnico.validatDatos()
         if (validacion[0]):
            selecciones[seleccion.lower().title()]["tecnico"].append(tecnico)
            print("\n***** OPERACIÓN EXITOSA *****\n")
            break
         else:
            print(validacion[1])
            continue
   else:
      print("\nEl nombre de la selección que ha ingresado no existe en la base de datos...\n")

def mostrarTodo():
   for (seleccion, data) in selecciones.items():
      print("\nSELECCIÓN DE " + seleccion.upper() + "\n")
      for (rol, data) in selecciones[seleccion].items():
         if(rol == "jugadores"):
            print("  Lista de Jugadores:\n")
         else:
            print("  Lista de Miembros del Cuerpo Técnico:\n")
         for persona in selecciones[seleccion][rol]:
            print("    Nombres: " + persona.getNombres() + "\n    Apellidos: " + persona.getApellidos() + "\n")

def mostrarSeleccion():
   seleccion = input("\nIngrese el nombre de la selección cuyos jugadores quiere ver: ")
   if (seleccion.lower().title() in selecciones):
      print("\nSELECCIÓN DE " + seleccion.upper() + "\n")
      for jugador in selecciones[seleccion.lower().title()]["jugadores"]:
         print("  Nombres: " + jugador.getNombres() + "\n  Apellidos: " + jugador.getApellidos() + "\n")
   else:
      print("\nEl nombre de la selección que ha ingresado no existe en la base de datos...\n")

def mostrarClub():
   club = input("\nIngrese el nombre del club cuyos jugadores quiere ver: ")
   jugadoresClub = []
   for (seleccion, data) in selecciones.items():
      for jugador in selecciones[seleccion]["jugadores"]:
         if(jugador.getClub() == club.lower().title()):
            jugadoresClub.append(jugador)
   if(not(jugadoresClub)):
      print("\nNo se encontraron jugadores de ese club en ninguna de las selecciones.\n")
   else:
      print("\nJugadores del club " + club.lower().title() + ":\n")
      for jugador in jugadoresClub:
         print(
            "  Nombres: " + jugador.getNombres() + ".\n" +
            "  Apellidos: " + jugador.getApellidos() + ".\n" +
            "  Nacionalidad: " + jugador.getNacionalidad() + ".\n"
         )

def retirar():
   seleccion = input("\nIngrese el nombre de la selección de la cual quiere retirar uno de sus miembros: ")
   if (seleccion.lower().title() in selecciones):
      while(True):
         print(
            "\nSi desea retirar un miembro del cuerpo tecnico ingrese 't'.\n" +
            "Si desea retirar un jugador ingrese 'j'.\n" +
            ">>> ", end = ''
         )
         rol = input()
         if(rol == "j" or rol == "'j'" or rol == 'j'):
            rol = "jugadores"
            msg = "\nLista de Jugadores de la Selección de " + seleccion.lower().title() + ".\n"
         elif(rol == "t" or rol == "'t'" or rol == 't'):
            rol = "tecnico"
            msg = "\nLista de Miembros del Cuerpo Técnico de la Selección de " + seleccion.lower().title() + ".\n"
         else:
            print("\nLa opción ingresada no es valida...\n" + "Por favor intentelo de nuevo.")
            break
         i = 1
         print(msg)
         for persona in selecciones[seleccion.lower().title()][rol]:
            print("  " + str(i) + ". " + persona.getNombres() + " " + persona.getApellidos() + ".\n")
            i = i + 1
         j = int(input("Ingrese el número de la persona que desea retirar: "))
         if(j < 1 or j > i):
            print(
               "El valor ingresado es incorrecto.\n" +
               "Por favor intentelo de nuevo..."
            )
            continue
         else:
            del selecciones[seleccion.lower().title()][rol][j - 1]
            print("\n***** OPERACIÓN EXITOSA *****\n")
            break
   else:
      print("\nEl nombre de la selección que ha ingresado no existe en la base de datos...\n")

def mostrarMejoresJugadores():
   print("")
   for i in range(5):
      index = i + 1
      if(mejoresJugadores.getLista()[i] != None):
         print(
            str(index) +
            ". " +
            mejoresJugadores.getLista()[i].getNombres() +
            " " +
            mejoresJugadores.getLista()[i].getApellidos() +
            " (Skill: " +
            str(mejoresJugadores.getLista()[i].getSkill()) +
            ").\n"
         )

print("\n***** BIENVENIDO AL PROGRAMA DE GESTIÓN DE SELECCIONES DE FUTBOL *****\n")

while(True):
   print(
      "Acciones que ofrece el programa...\n" +
      "  1. Registrar selección.\n" +
      "  2. Registrar jugador.\n" +
      "  3. Registrar miembre del cuerpo técnico.\n" +
      "  4. Mostrar los jugadores y cuerpo técnico de cada equipo.\n" +
      "  5. Mostrar los jugadores de una selección.\n" +
      "  6. Buscar jugadores por club.\n" +
      "  7. Retirar a un jugador o miembre del cuerpo técnico de una selección.\n"
      "  8. Mostrar los 5 mejores jugadores del torneo.\n" +
      "  9. Salir.\n" +
      ">>> ", end = ''
   )
   userInput = input()
   if(userInput == "1" or userInput == "1."):
      regSeleccion()
   elif(userInput == "2" or userInput == "2."):
      regJugador()
   elif(userInput == "3" or userInput == "3."):
      regTecnico()
   elif(userInput == "4" or userInput == "4."):
      mostrarTodo()
   elif(userInput == "5" or userInput == "5."):
      mostrarSeleccion()
   elif(userInput == "6" or userInput == "6."):
      mostrarClub()
   elif(userInput == "7" or userInput == "7."):
      retirar()
   elif(userInput == "8" or userInput == "8."):
      mostrarMejoresJugadores()
   elif(userInput == "9" or userInput == "9."):
      print("\n***** FIN DEL PROGRAMA *****\n")
      break
   else:
      print(
         "\nEntrada no válida...\n" +
         "Por favor intentelo de nuevo."
      )