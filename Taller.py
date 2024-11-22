########################################################################
# Maria Luisa Londoño Moncada
# 21/11/2024
# Seguimiento 2

# Solución
# Caso 1: Lista de Listas
notas = [
    ["Calculo", 3.5, 2.5, 1.5],
    ["Química", 2.5, 3.0, 5.0],
    ["Deporte", 2.4, 2.0, 2.2],
    ["Lógica", 1.5, 4.0, 4.5]
]

# 1.1 Calcular la nota final de cada materia (30%, 30% y 40%),
# y agregar el valor a los datos
def c11_final():
    for materia in notas:
        # Calculamos el promedio ponderado
        final = materia[1] * 0.3 + materia[2] * 0.3 + materia[3] * 0.4
        materia.append(round(final, 2))

# 1.2 Calcular el promedio de las notas del Estudiante
def c12_promedio():
    total = 0
    for materia in notas:
        total += materia[-1]
    promedio = total / len(notas)
    return round(promedio, 2)

# Llamar funciones, y mostrar Resultados
c11_final()
print("Caso 1 - Lista de Listas:")
for materia in notas:
    print(materia)
print("Promedio general:", c12_promedio())

########################################################################
# Caso 2: Diccionario de Listas
notas = {
    "Calculo": [3.5, 2.5, 1.5],
    "Química": [2.5, 3.0, 5.0],
    "Deporte": [2.4, 2.0, 2.2],
    "Lógica": [1.5, 4.0, 4.5]
}

# 2.1 Calcular la nota final de cada materia (30%, 30% y 40%),
# y agregar el valor a los datos
def c21_final():
    for materia, calificaciones in notas.items():
        final = calificaciones[0] * 0.3 + calificaciones[1] * 0.3 + calificaciones[2] * 0.4
        calificaciones.append(round(final, 2))

# 2.2 Calcular el promedio de las notas del Estudiante
def c22_promedio():
    total = 0
    for calificaciones in notas.values():
        total += calificaciones[-1]
    promedio = total / len(notas)
    return round(promedio, 2)

# Llamar funciones, y mostrar Resultados
c21_final()
print("\nCaso 2 - Diccionario de Listas:")
for materia, calificaciones in notas.items():
    print(materia, calificaciones)
print("Promedio general:", c22_promedio())

########################################################################
# Caso 3: Diccionario de Diccionarios
notas = {
    "Calculo": {"pp": 3.5, "sp": 2.5, "tp": 1.5},
    "Química": {"pp": 2.5, "sp": 3.0, "tp": 5.0},
    "Deporte": {"pp": 2.4, "sp": 2.0, "tp": 2.2},
    "Lógica": {"pp": 1.5, "sp": 4.0, "tp": 4.5}
}

# 3.1 Calcular la nota final de cada materia (30%, 30% y 40%),
# y agregar el valor a los datos
def c31_final():
    for materia, parciales in notas.items():
        final = parciales["pp"] * 0.3 + parciales["sp"] * 0.3 + parciales["tp"] * 0.4
        parciales["final"] = round(final, 2)

# 3.2 Calcular el promedio de las notas del Estudiante
def c32_promedio():
    total = 0
    for parciales in notas.values():
        total += parciales["final"]
    promedio = total / len(notas)
    return round(promedio, 2)

# Llamar funciones, y mostrar Resultados
c31_final()
print("\nCaso 3 - Diccionario de Diccionarios:")
for materia, parciales in notas.items():
    print(materia, parciales)
print("Promedio general:", c32_promedio())
