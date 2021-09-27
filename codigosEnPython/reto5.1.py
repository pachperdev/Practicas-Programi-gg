# Reto 5
# Última Modificación 14/06/2021 6:20 PM
# Autor Yojhan David Barrios Tapias

# Función rotar Elementos para ir intercambiando elementos en las listas indice, con el fin de ordenae
def rotarElementosLista(i, j, lista) -> list:
    temporal = lista[i]
    lista[i] = lista[j]
    lista[j] = temporal
    return(lista)


# Función principal que coordina el ordenamiento de las listas
def ordenarLista(listaIndice: list, listaDatos: dict) -> list:
    intercambios = -1
    while intercambios != 0:
        intercambios = 0
        for i in range(len(listaIndice)-1):
            indiceActual = listaIndice[i]
            indiceSiguiente = listaIndice[i+1]
            datoActual = listaDatos[indiceActual]
            datoSiguiente = listaDatos[indiceSiguiente]

            if datoSiguiente > datoActual:
                listaIndice = rotarElementosLista(i, i+1, listaIndice)
                intercambios += 1
            elif datoActual == datoSiguiente and indiceSiguiente > indiceActual:
                listaIndice = rotarElementosLista(i, i+1, listaIndice)
                intercambios += 1
    return listaIndice


# Programa principal
try:
    archivo = open("./data.csv", "rt", encoding="utf-8")

    # Pedir ciudades
    ciudad = input("Dime la ciudad: ")

    # Método que me ubica en el principio (Byte 0) del archivo
    archivo.seek(0)

    # Lectura de Datos
    listaAlertas = ["sin riesgo", "alerta azul", "alerta verde", "alerta amarilla", "alerta roja"]
    conteoCiudadAlerta = {"sin riesgo": 0, "alerta azul": 0, "alerta verde": 0, "alerta amarilla": 0, "alerta roja": 0}
    listaTratamientos = ["no aaf", "seguimiento", "aaf"]
    conteoCiudadTratamiento = {"no aaf": 0, "seguimiento": 0, "aaf": 0}

    for linea in archivo:
        arregloDatos = linea.strip().split(",")
        if arregloDatos[2].upper() == ciudad.upper():
            alerta: str = arregloDatos[13]
            conteoCiudadAlerta[alerta] += 1
            tratamiento: str = arregloDatos[14]
            conteoCiudadTratamiento[tratamiento] += 1

    listaAlertas = ordenarLista(listaAlertas, conteoCiudadAlerta)
    listaTratamientos = ordenarLista(listaTratamientos, conteoCiudadTratamiento)

    print("*" * 24)
    print(ciudad.capitalize())

    for indice in listaAlertas:
        print(indice, conteoCiudadAlerta[indice])

    for indice in listaTratamientos:
        print(indice, conteoCiudadTratamiento[indice])

    archivo.close()
except FileNotFoundError:
    print("Archivo no encontrado. :'(")