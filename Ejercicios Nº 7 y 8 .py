import math
from abc import ABC, abstractclassmethod


class Persona(ABC):
    def __init__(self, nombre, apellido, DNI, cuenta):
        self.nombre = nombre
        self.apellido = apellido
        self.DNI = DNI
        self.cuenta = cuenta
        
    @abstractclassmethod
    def registrarse(self):
        pass
    
    

class Cuenta(Persona):
    def __init__(self, nombre, apellido, DNI, cuenta):
        super().__init__(nombre, apellido, DNI, cuenta)
        
    def registrarse(self):
        print('El registro de la Cuenta se realizo con exito: ')


class CuentaJoven(Persona):
    def __init__(self, nombre, apellido, DNI, cuenta, bonificacion):
        super().__init__(nombre, apellido, DNI, cuenta, bonificacion)
        self.bonificacion = bonificacion
        
    def registrarse(self):
        print('El registro de la Cuenta Joven fue un exito: ')


nueva_cuenta = Cuenta('Juan', 'Perez', 23456543, 345)
nueva_cuenta.registrarse()

nueva_cuentajoven = CuentaJoven('Marcos', 'Doe', 54677843, 223, '15%')
nueva_cuentajoven.registrarse()







