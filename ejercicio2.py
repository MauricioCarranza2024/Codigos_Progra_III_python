# EJERCICIO 2 DEL TALLER DE REPASO, TAREA PROGRAMACION III
# MAURICIO CARRANZA - SMTR059023

class Articulo:
    def __init__(self, tipo, descripcion, precio_compra):
        self.tipo = tipo
        self.descripcion = descripcion
        self.precio_compra = precio_compra
        self.marca = "HOJITAS" if tipo == "cuaderno" else "RAYAS"
        self.precio_venta = self.precio_compra * 1.30

    def mostrar_info(self):
        print(f"\nTipo: {self.tipo}")
        print(f"Descripción: {self.descripcion}")
        print(f"Marca: {self.marca}")
        print(f"Precio de Compra: ${self.precio_compra:.2f}")
        print(f"Precio de Venta: ${self.precio_venta:.2f}")


cuaderno1 = Articulo("cuaderno", "50 hojas", 0.80)
cuaderno2 = Articulo("cuaderno", "100 hojas", 1.00)

lapiz1 = Articulo("lapiz", "Grafito", 0.40)
lapiz2 = Articulo("lapiz", "Colores", 0.60)


print("\n***CUADERNOS***")
cuaderno1.mostrar_info()
cuaderno2.mostrar_info()

print("\n***LAPIZ***")
lapiz1.mostrar_info()
lapiz2.mostrar_info()
