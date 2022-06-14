from datetime import date
from Contrato import Contrato

class jugador:
    __nombre = None
    __dni = None
    __ciudadNatal = None
    __paisOrigen = None
    __fecha_nacimiento = None
    __contrato = None

    def __init__(self,nombre,dni:int,ciudad,pais,date:date):
        self.__nombre = nombre
        self.__dni = dni
        self.__ciudadNatal = ciudad
        self.__paisOrigen = pais
        self.__fecha_nacimiento = date
    
    def __str__(self):
        cadena = ("Nombre:{}\n".format(self.__nombre))
        cadena += ("DNI:{}\n".format(self.__dni))
        cadena += ("Ciudad Natal:{}     Pais de Origen:{}\n".format(self.__ciudadNatal,self.__paisOrigen))
        cadena += ("Fecha de nacimiento:{}".format(self.__fecha_nacimiento))
        return cadena
    
    def setContrato(self,contrato:Contrato):
        self.__contrato = contrato

    def getNombre(self):
        return self.__nombre
    
    def getDNI(self):
        return self.__dni
    
    def getCiudad(self):
        return self.__ciudadNatal
    
    def getPais(self):
        return self.__paisOrigen
    
    def getFecha(self):
        return self.__fecha_nacimiento
    
    def getContrato(self):
        return self.__contrato