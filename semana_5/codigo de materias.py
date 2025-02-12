<<<<<<< HEAD
# Lista de asignaturas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Diccionario para almacenar las notas
notas = {}

# Solicitar al usuario las notas de cada asignatura
for asignatura in asignaturas:
    while True:
        try:
            nota = float(input(f"Introduce la nota que has sacado en {asignatura}: "))
            if 0 <= nota <= 10:
                notas[asignatura] = nota
                break
            else:
                print("La nota debe estar entre 0 y 10. Intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce un número válido.")

# Mostrar las asignaturas y las notas
for asignatura, nota in notas.items():
    print(f"En {asignatura} has sacado {nota}.")
=======
# Lista de asignaturas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Diccionario para almacenar las notas
notas = {}

# Solicitar al usuario las notas de cada asignatura
for asignatura in asignaturas:
    while True:
        try:
            nota = float(input(f"Introduce la nota que has sacado en {asignatura}: "))
            if 0 <= nota <= 10:
                notas[asignatura] = nota
                break
            else:
                print("La nota debe estar entre 0 y 10. Intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce un número válido.")

# Mostrar las asignaturas y las notas
for asignatura, nota in notas.items():
    print(f"En {asignatura} has sacado {nota}.")
>>>>>>> ae0dba841896ccb2cf31293c6a1127d470dc59a7
