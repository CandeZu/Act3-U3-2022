from ClaseContrato import contrato
from datetime import date

class equipo:
    __nombre = None
    __ciudad = None
    __contratos = None
    #Variables de clase
    __cantcontratos = 0

    def __init__(self,nombre = "",ciudad = ""):
        self.__nombre = nombre
        self.__ciudad = ciudad
        self.__contratos = []
    
    def getNombre(self):
        return self.__nombre
    
    @classmethod
    def getCantidadContratos(cls):
        cls.__cantcontratos += 1
        return cls.__cantcontratos
    
    def generarContrato(self,contratoNuevo):
        print("Contrato nro:{}\n".format(self.getCantidadContratos()))
        self.__contratos.append(contratoNuevo)
    
    def __str__(self):
        return ("Nombre:{} \nCiudad:{}".format(self.__nombre,self.__ciudad))
    
    def getContratos(self):
        return self.__contratos
    
    def getNombre(self):
        return self.__nombre
    
    def contratosVencimiento(self):
        print("Jugadores que vencen contrato en 6 meses")
        for contrato in self.__contratos:
            if (((contrato.getFechaFin() - date.today()).days // 30 ) == 6):
                print("".center(20,"-"))
                print("{}".format(contrato.getJugador()))
            
    def getImporteTotal(self):
        importe = 0
        for contrato in self.__contratos:
            importe += contrato.getImporte()
        
        print("El importe total en jugadores es de: ${}".format(importe))

