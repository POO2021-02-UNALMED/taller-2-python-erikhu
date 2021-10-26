#!/usr/bin/env python3

class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if(color in ['rojo', 'verde', 'amarillo', 'negro']):
            self.color = color

class Auto:
    def __init__(self, modelo, precio, asientos, marca, motor, registro, cantidadCreados):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidadCreados = cantidadCreados

    def cantidadAsientos(self):
        [asiento for asiento in self.asientos if asiento].count()

    def verificarIntegridad(self):
        for asiento in self.asientos:
            if asiento.registro != self.motor.registro or asiento.registro != self.registro:
                return "Las piezas no son originales"
        return "Auto original"

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindro = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if self.tipo in ['electrico', 'gasolina']:
            self.tipo = tipo