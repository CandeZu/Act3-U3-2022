class Contrato:
    __fechainicio = ""
    __fechafin = ""
    __pagomensual = 0
    __equipo = None
    __jugador = None

    def __init__(self, fechainicio, fechafin, pagomensual, equipo, jugador):
        self.__fechainicio = fechainicio
        self.__fechafin = fechafin
        self.__pagomensual = pagomensual
        self.__equipo = equipo
        self.__jugador = jugador
    
    def getFechaInicio(self):
        return self.__fechainicio
    
    def getFechaFin(self):
        return self.__fechafin

    def getPagoMensual(self):
        return self.__pagomensual
    
    def getEquipo(self):
        return self.__equipo
    
    def getJugador(self):
        return self.__jugador
    
    def getImporte(self):
        return (self.__pagomensual*((self.__fechafin-self.__fechainicio).days//30))
    