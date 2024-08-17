#EJERCICIO 4 DEL TALLER DE REPASO, TAREA PROGRAMACION III
# MAURICIO CARRANZA - SMTR059023

class Dispositivos:
    def __init__(self, tipo, modelo, pantalla, almacenamiento, procesador, ram, precio_compra):
        self.tipo = tipo
        self.marca = "PHR"  
        self.modelo = modelo
        self.pantalla = pantalla
        self.almacenamiento = almacenamiento
        self.procesador = procesador
        self.ram = ram
        self.precio_compra = precio_compra
        self.precio_venta = self._calcular_precio_venta()
        self.origen = "Importado" 

    def _calcular_precio_venta(self):

        return self.precio_compra * 1.7

    def mostrar_informacion(self):
       
        print(f"\nTipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Pantalla: {self.pantalla} pulgadas")
        print(f"Almacenamiento: {self.almacenamiento} GB")
        print(f"Procesador: {self.procesador}")
        print(f"RAM: {self.ram} GB")
        print(f"Precio de Compra: ${self.precio_compra:.2f}")
        print(f"Precio de Venta: ${self.precio_venta:.2f}")
        print(f"Origen: {self.origen}")

# Crear una lista de dispositivos electrónicos
def crear_dispositivos():
    dispositivos = [
        Dispositivos("Celular", "X1", 6.5, 128, "Snapdragon 888", 8, 300.0),
        Dispositivos("Tablet", "Samsung Galaxi Tab S9", 11, 128, "Qualcomm Snapdragon 8 Gen 2", 8, 480.0),
        Dispositivos("Portátil", "Laptop ASUS ROG Zephyrus G14", 15.6, 512, "Rizen 7", 16, 1000.0)
    ]
    return dispositivos

# Mostrar información de todos los dispositivos
def mostrar_dispositivos(dispositivos):
    for dispositivo in dispositivos:
        dispositivo.mostrar_informacion()

# Ejecución del código
if __name__ == "__main__":
    dispositivos = crear_dispositivos()
    mostrar_dispositivos(dispositivos)

