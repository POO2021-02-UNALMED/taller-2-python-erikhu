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
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = [asiento for asiento in asientos if asiento != None]
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1

    def cantidadAsientos(self):
        len(self.asientos)

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
        if tipo in ['electrico', 'gasolina']:
            self.tipo = tipo
