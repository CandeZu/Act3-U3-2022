from ManejadorContrato import ManejadorContratos
from ManejadorJugador import ManejadorJugadores
from ManejadorEquipo import ManejadorEquipos
from Equipo import Equipo
from Jugador import Jugador
from Contrato import Contrato
import os

class Menu:
    __contrato = None
    __equipo = None
    __jugador = None
    __op = 0

    def __init__(self, op= 0):
        self.__contrato = ManejadorContratos()
        self.__equipo = ManejadorEquipos()
        self.__jugador = ManejadorJugadores()
        self.__op = op

    def opciones(self):
            print("Se cargan datos de los equipos")
            self.__equipo.cargarArchivo()
            os.system("cls")
            continuar = True


            while continuar:
                print("[1] Contratar un jugador")
                print("[2] Consultar jugadores contratados")
                print("[3] Consultar contratos")
                print("[4] Obtener importe de contratos")
                print("[0] Para salir del menu")
                self.__op = int(input("INGRESE OPCION\n"))
                os.system("cls")

                if(self.__op == 1):
                    print("CARGA DE DATOS DEL JUGADOR".center(40,"-"))
                    nombre = input("Ingrese nombre del jugador\n".capitalize())
                    os.system("cls")
                    apellido = input("Ingrese apellido del jugador\n".capitalize())
                    os.system("cls")
                    nombreJugador = nombre+" "+apellido
                    dni = int(input("Ingrese documento nacional de identidad(DNI)\n"))
                    os.system("cls")
                    ciudad = input("Ingrese ciudad natal\n")
                    os.system("cls")
                    pais = input("Ingrese pais de origen\n")
                    os.system("cls")
                    print("Ingrese fecha de nacimiento del jugador")
                    dia = input("DIA--> ")
                    mes = input("MES--> ")
                    año = input("AÑO--> ")
                    fecha = date(int(año),int(mes),int(dia))
                    os.system("cls")
                    NuevoJugador = jugador(nombreJugador,dni,ciudad,pais,fecha)

                    equipoDeContrato = input("Ingrese nombre del equipo con el cual se realizara el contrato\n")
                    buscar = self.__equipo.buscarEquipo(equipoDeContrato)
                    while(buscar == -1):
                        equipoDeContrato = input("El equipo ingresado no existe o esta mal escrito, INGRESE NUEVAMENTE\n")
                        buscar = self.__equipo.buscarEquipo(equipoDeContrato)
                    
                    print("Equipo ingresado encontrado")
                    print(self.__equipo.getEquipo(buscar))
                    input("ENTER PARA CONTINUAR")
                    os.system("cls")

                    print("CREAR CONTRATO".center(20,"-"))
                    print("Ingrese fecha de inicio de contrato")
                    dia = input("DIA--> ")
                    mes = input("MES--> ")
                    año = int(input("AÑO--> "))
                    fechaInicio = date(año,int(mes),int(dia))
                    os.system("cls")
                    """print("El contrato finalizara 2 años pasados el inicio del mismo")
                    año += 2"""
                    print("Ingrese fecha de fin de contrato")
                    dia = input("DIA--> ")
                    mes = input("MES--> ")
                    año = int(input("AÑO--> "))
                    fechaFin = date(año,int(mes),int(dia))
                    os.system("cls")
                    pago = float(input("Ingrese pago mensual del jugador\n"))
                    contratoNuevo = contrato(fechaInicio,fechaFin,pago,NuevoJugador,self.__Equipos.getEquipo(buscar))
                    
                    #Seteamos el contrato en cada clase
                    self.__contrato.agregarContrato(contratoNuevo)
                    NuevoJugador.setContrato(contratoNuevo)
                    self.__jugadore.agregarJugador(NuevoJugador)
                    self.__equipo.setContrato(buscar,contratoNuevo)


                elif(self.__op ==2):
                    dnijugador = int(input("Ingrese DNI del jugador que desea buscar\n"))
                    busqueda = self.__Jugadores.buscarJugador(dnijugador)
                    while(busqueda == -1):
                        dnijugador = input("El DNI ingresado no existe o esta mal escrito, INGRESE NUEVAMENTE\n")
                        busqueda = self.__Equipos.buscarEquipo(dnijugador)
                    
                    print("Jugador encontrado")
                    print("EQUIPO".center(20,"-"))
                    print("{}".format(self.__Jugadores.getEquipo(busqueda)))
                    print("Fecha de finalizacion de contrato:{}".format(self.__Jugadores.getFechaFin(busqueda)))
        
                elif(self.__op ==3):
                    equipoContratos = input("Ingrese equipo del cual quiere consultar contratos\n")
                    buscar = self.__Equipos.buscarEquipo(equipoContratos)
                    while(buscar == -1):
                        equipoContratos = input("El equipo ingresado no existe o esta mal escrito, INGRESE NUEVAMENTE\n")
                        buscar = self.__Equipos.buscarEquipo(equipoContratos)
                    
                    print("Equipo ingresado encontrado")
                    equipoIngresado = self.__Equipos.getEquipo(buscar)
                    print(equipoIngresado)
                    input("ENTER PARA CONTINUAR")
                    os.system("cls")
                    equipoIngresado.contratosVencimiento()

                elif (self.__op ==4):
                    equipoContratos = input("Ingrese equipo del cual quiere consultar importe total en jugadores\n")
                    buscar = self.__Equipos.buscarEquipo(equipoContratos)
                    while(buscar == -1):
                        equipoContratos = input("El equipo ingresado no existe o esta mal escrito, INGRESE NUEVAMENTE\n")
                        buscar = self.__Equipos.buscarEquipo(equipoContratos)

                    print("Equipo ingresado encontrado")
                    equipoIngresado = self.__Equipos.getEquipo(buscar)
                    print(equipoIngresado)
                    input("ENTER PARA CONTINUAR")
                    os.system("cls")
                    equipoIngresado.getImporteTotal()

                elif(self.__op == 0):
                    continuar = not continuar
                    print("PROGRAMA FINALIZADO")
                else: 
                    print("Opcion incorrecta, ingrese nuevamente")