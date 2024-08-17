#EJERCICIO 3 DEL TALLER DE REPASO, TAREA PROGRAMACION III
# MAURICIO CARRANZA - SMTR059023

class Auto:
    def __init__(self, marca, modelo, año, color, tipo_de_motor, 
                 tipo_de_combustible, kilometraje, precio_compra, 
                 origen, transmision):


        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.tipo_motor = tipo_de_motor
        self.tipo_combustible = tipo_de_combustible
        self.kilometraje = kilometraje
        self.precio_compra = precio_compra
        self.origen = origen  
        self.transmision = transmision  
        self.precio_venta = self.calcular_precio_venta()
        self.ruedas = 4
        self.capacidad_pasajeros = 5

    def calcular_precio_venta(self):
        return self.precio_compra * 1.4

    def mostrar_informacion(self):
        #print(f"\nInformación del Vehículo:")
        print(f"\nMarca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Tipo de Motor: {self.tipo_motor}")
        print(f"Tipo de Combustible: {self.tipo_combustible}")
        print(f"Kilometraje: {self.kilometraje} km")
        print(f"Transmisión: {self.transmision}")
        print(f"Origen: {self.origen}")
        print(f"Precio de Compra: ${self.precio_compra:.2f}")
        print(f"Precio de Venta: ${self.precio_venta:.2f}")
        print(f"Ruedas: {self.ruedas}")
        print(f"Capacidad de Pasajeros: {self.capacidad_pasajeros}")
        print()


auto1 = Auto(
    marca="Ford",
    modelo="Mustang",
    año=2023,
    color="Rojo",
    tipo_de_motor="2.3L Turbo",
    tipo_de_combustible="Gasolina",
    kilometraje=0,
    precio_compra=35000.0,
    origen="Nacional",
    transmision="Automática"
)


auto2 = Auto(
    marca="Honda",
    modelo="Civic",
    año=2023,
    color="Azul",
    tipo_de_motor="2.0L",
    tipo_de_combustible="Gasolina",
    kilometraje=0,
    precio_compra=22000.0,
    origen="Importado",
    transmision="Manual"
)

auto3 = Auto(
    marca="Chevrolet",
    modelo="Malibu",
    año=2023,
    color="Negro",
    tipo_de_motor="1.5L Turbo",
    tipo_de_combustible="Gasolina",
    kilometraje=0,
    precio_compra=25000.0,
    origen="Nacional",
    transmision="Automática" 
)

print("\n****INFORMACION DE LOS AUTOS****")
auto1.mostrar_informacion()
auto2.mostrar_informacion()
auto3.mostrar_informacion()

