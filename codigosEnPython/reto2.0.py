numeroPacientes = int(input("Ingresa el número de pacientes: "))
contador = 1
cantidadAlertaAzul = 0
cantidadAlertaAmarilla = 0
cantidadAaf = 0
cantidadNoAaf = 0
cantidadSeguimiento = 0
sumaTamaño = 0
while contador <= numeroPacientes:
    composicion = input("Escoge una opcion digitando su codigo: ")
    ecogenicidad = input("Escoge una opcion digitando su codigo: ")
    forma = input("Escoge una opcion digitando su codigo: ")
    margen = input("Escoge una opcion digitando su codigo: ")
    fe1 = int(input("FE1. Ninguno o grandes artefactos en cola de cometa: "))
    fe2 = int(input("FE2. Macrocalcificaciones: "))
    fe3 = int(input("FE3. Calcificaciones perifericas (borde): "))
    fe4 = int(input("FE4. Focos ecogenicos punteados: "))
    tamaño = float(input("Determine el tamaño del nodulo: "))
    sumaTamaño = sumaTamaño + tamaño
    puntaje = 0
    if composicion == "C3":
        puntaje = puntaje + 2
    elif composicion == "C4":
        puntaje = puntaje + 4
    if ecogenicidad == "E2":
        puntaje = puntaje + 2
    elif ecogenicidad == "E3":
        puntaje = puntaje + 4
    elif ecogenicidad == "E4":
        puntaje = puntaje + 6
    if forma == "F2":
        puntaje = puntaje + 6
    if margen == "M3":
        puntaje = puntaje + 4
    elif margen == "M4":
        puntaje = puntaje + 6
    if fe2 == 1:
        puntaje = puntaje + 2
    if fe3 == 1:
        puntaje = puntaje + 4
    if fe4 == 1:
        puntaje = puntaje + 6
    contador += 1
    # Mostrar resultados
    if puntaje >= 0 and puntaje <= 3:
        cantidadNoAaf += 1
    elif puntaje >= 4 and puntaje <= 5:
        cantidadAlertaAzul += 1
        cantidadNoAaf += 1
    elif puntaje >= 6 and puntaje <= 7:
        if tamaño >= 2.5:
            cantidadAaf += 1
        else:
            cantidadSeguimiento += 1
    elif puntaje >= 8 and puntaje <= 12:
        if tamaño >= 1.5:
            cantidadAlertaAmarilla += 1
            cantidadAaf += 1
        else:
            cantidadAlertaAmarilla += 1
            cantidadSeguimiento += 1
    elif puntaje >= 13:
        if tamaño >= 1:
            cantidadAaf += 1
        else:
            cantidadSeguimiento += 1
# Hallar promedio
promedioTamaño = sumaTamaño / numeroPacientes
# Imprimir resultados
print("alerta azul", cantidadAlertaAzul)
print("alerta amarilla", cantidadAlertaAmarilla)
print("{0:.2f}".format(promedioTamaño))
print("No aaf", cantidadNoAaf)
print("Seguimiento", cantidadSeguimiento)
print("aaf", cantidadAaf)