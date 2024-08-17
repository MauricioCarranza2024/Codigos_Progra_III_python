#EJERCICIO PROPIO USANDO POO, TAREA PROGRAMACION III
# MAURICIO CARRANZA - SMTR059023

#EXPLICACION BREVE DE LO QUE TRATA EL EJERCICIO
"""
en este ejercicio me base en el ambito de una empresa que busca a nuevos empleados y los agrega,
cada empleado tiene un nombre, apellidos, edad, departamento, salario y un ID. Que son ingresados
por teclado y luego los muestra en pantalla. Tambien utilice Programación Orientada a Objetos (POO), 
con su respectiva implementación e instanciación, espero y todo me salga bien y asi tener una excelente nota
FELIZ DIA!!!
"""

class Empleado:
    def __init__(self, nombre, apellidos, edad, departamento, salario, id_empleado):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__edad = edad
        self.__departamento = departamento
        self.__salario = salario
        self.__id_empleado = id_empleado

    def mostrar_informacion(self):
        print(f"\nNombre: {self.__nombre}")
        print(f"Apellidos: {self.__apellidos}")
        print(f"Edad: {self.__edad} años")
        print(f"Departamento: {self.__departamento}")
        print(f"Salario: ${self.__salario:.2f} dolares")
        print(f"ID de Empleado: {self.__id_empleado}")
        print()

def obtener_datos_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    apellidos = input("Ingrese los apellidos del empleado: ")
    edad = int(input("Ingrese la edad del empleado: "))
    departamento = input("Ingrese el departamento del empleado: ")
    salario = float(input("Ingrese el salario del empleado: "))
    id_empleado = input("Ingrese el ID del empleado: ")
    return nombre, apellidos, edad, departamento, salario, id_empleado

def agregar_empleados():
    lista_empleados = []
    while True:
        datos = obtener_datos_empleado()
        nuevo_empleado = Empleado(*datos)
        lista_empleados.append(nuevo_empleado)


        agregar_otro = input("El empleado sea registrado con exito ¿Desea agregar otro empleado? (s/n): ")
        if agregar_otro.lower() != 's':
            break

    return lista_empleados

def mostrar_empleados(lista_empleados):
    print("\nInformación de los empleados registrados:")
    for empleado in lista_empleados:
        empleado.mostrar_informacion()

def main():
    lista_empleados = agregar_empleados()
    mostrar_empleados(lista_empleados)

if __name__ == "__main__":
    main()
