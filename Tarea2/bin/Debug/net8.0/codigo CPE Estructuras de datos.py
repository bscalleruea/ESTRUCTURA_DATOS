import csv
from datetime import datetime

# Archivo para guardar los datos
FILE_NAME = "aportes_asociacion.csv"

# Cargar datos desde el archivo
def cargar_datos():
    try:
        with open(FILE_NAME, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []

# Guardar datos en el archivo
def guardar_datos(datos):
    with open(FILE_NAME, mode='w', newline='') as file:
        fieldnames = ['Nombre', 'Aporte Mensual', 'Fecha']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(datos)

# Registrar un nuevo aporte
def registrar_aporte(datos):
    nombre = input("Ingrese el nombre del miembro: ")
    monto = input("Ingrese el monto del aporte: ")
    fecha = datetime.now().strftime('%Y-%m-%d')
    datos.append({'Nombre': nombre, 'Aporte Mensual': monto, 'Fecha': fecha})
    print(f"Aporte registrado para {nombre}.")

# Mostrar resumen de aportes
def mostrar_resumen(datos):
    resumen = {}
    for registro in datos:
        nombre = registro['Nombre']
        monto = float(registro['Aporte Mensual'])
        if nombre in resumen:
            resumen[nombre] += monto
        else:
            resumen[nombre] = monto
    print("\nResumen de Aportes:")
    for nombre, total in resumen.items():
        print(f"{nombre}: ${total:.2f}")

# Menú principal
def menu():
    datos = cargar_datos()
    while True:
        print("\n--- Gestión de Aportes ---")
        print("1. Registrar Aporte")
        print("2. Mostrar Resumen de Aportes")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            registrar_aporte(datos)
            guardar_datos(datos)
        elif opcion == '2':
            mostrar_resumen(datos)
        elif opcion == '3':
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
