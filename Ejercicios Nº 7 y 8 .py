import math
from abc import ABC, abstractclassmethod


class Persona(ABC):
    def __init__(self, nombre, apellido, DNI, cuenta):
        self.nombre = nombre
        self.apellido = apellido
        self.DNI = DNI
        self.cuenta = cuenta
        
    @abstractclassmethod
    def mostrar(self):
        pass
    
    

class Cuenta(Persona):
    def __init__(self, nombre, apellido, DNI, cuenta):
        super().__init__(nombre, apellido, DNI, cuenta)
        
    def mostrar(self):
        print('El detalle de la Cuenta es: ')


class CuentaJovern(Persona):
    def __init__(self, nombre, apellido, DNI, cuenta):
        super().__init__(nombre, apellido, DNI, cuenta)
        
    def mostrar(self):
        print('El detalle de la Cuenta Joven es: ')










