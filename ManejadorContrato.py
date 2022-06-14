
from Contrato import Contrato
import numpy as np
import os

class ManejadorContratos:
    __dimension  = 1
    __cantidad = 0
    __incremento = 1
    __contratos = None

    def __init__(self):
        self.__contratos = np.empty(self.__dimension,dtype=contrato)

    def agregarContrato(self,NuevoContrato):
        if(self.__cantidad == self.__dimension):
            self.__dimension += self.__incremento
            self.__contratos.resize(self.__dimension)
        self.__contratos[self.__cantidad] = NuevoContrato
        self.__cantidad += 1
    
    def getLista(self):
        return self.__contratos