import math
from abc import ABC, abstractclassmethod


class Persona(ABC):
    def __init__(self, nombre ='', apellido ='', dni =0, edad =0, cuenta =0, saldo_inicial =0):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad
        self.cuenta = cuenta
        self.saldo_inicial = saldo_inicial
        
    @abstractclassmethod
    def registrarse(self):
        pass
    
    def save(self):
        pass

class Cuenta(Persona):
    def __init__(self, nombre, apellido, dni, edad, cuenta, saldo_inicial):
        super().__init__(nombre, apellido, dni, edad, cuenta, saldo_inicial)
        self.__cuenta = Cuenta
        
    def registrarse(self):
        print('El registro de la Cuenta se realizo con exito: ')


class CuentaJoven(Persona):
    def __init__(self, nombre, apellido, dni, edad, cuenta, saldo_inicial, bonificacion):
        super().__init__(nombre, apellido, dni, edad, cuenta, saldo_inicial, bonificacion)
        self.bonificacion = bonificacion
        
    def registrarse(self):
        print('El registro de la Cuenta Joven fue un exito: ')
        
    def es_titular_valido(self):
        # if edad > 18 and < 25:
        pass
        
        
            
    def depositar(self, nuevo_saldo):
        float(input('Ingrese su monto a Depositar'))
        nuevo_saldo = (saldo_inicial + deposito)
        nuevo_saldo.save()
        print('Su nuevo saldo es: ', nuevo_saldo)
    
    def retiro(self, nuevo_saldo):
        int(input('Ingrese el Monto a Solicitado: '))
        nuevo_saldo = (saldo_inicial - retiro)
        nuevo_saldo.save()
        print('Su nuevo saldo es: ')
        


nueva.cuenta = Persona('juan', 'Gomez', 23456789, 44, 300, 1798,3),
nueva.cuenta2 = Persona('Gabriel', 'Perez', 54678908, 23, 301, 543)

nueva_cuentajoven = Persona('Marcos', 'Doe', 54677843, 223, '15%')
nueva_cuentajoven.registrarse()







