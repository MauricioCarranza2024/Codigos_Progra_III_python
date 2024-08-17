# EJERCICIO 1 DEL TALLER DE REPASO, TAREA PROGRAMACION III
# MAURICIO CARRANZA - SMTR059023

class Perro:
    def __init__(self, nombre, raza, edad, peso, color, dueño):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.color = color
        self.dueño = dueño
        self.estado = "NO ATENDIDO"
        self.tipo_perro = "Perro Grande" if peso >= 10 else "Perro Pequeño"

    def registrar(self):
        self.estado = "ATENDIDO"
        self.mostrar_info()

    def mostrar_info(self):
        print("\nInformación del Perro:")
        print(f"\nNombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Color: {self.color}")
        print(f"Nombre del dueño: {self.dueño}")
        print(f"Estado: {self.estado}")
        print(f"Tipo de Perro: {self.tipo_perro}")


nombre = input("Ingrese el nombre del perro: ")
raza = input("Ingrese la raza del perro: ")
edad = int(input("Ingrese la edad del perro: "))
peso = float(input("Ingrese el peso del perro (en kg): "))
color = input("Ingrese el color del perro: ")
dueño = input("Ingrese el nombre del dueño del perro: ")


perro1 = Perro(nombre, raza, edad, peso, color, dueño)
perro1.registrar()
