contador = 0
puntaje = 0 
suma_tam = 0
promedio = 0
sin_riesgo = 0
alerta_azul = 0
alerta_verde = 0
alerta_amarilla = 0
alerta_roja = 0
cont_no_aaf = 0 
cont_seg = 0
cont_aaf = 0
fe1 = 0
fe2 = 0 
fe3 = 0 
fe4 = 0

cod_composicion = []
cod_ecogenicidad = []
cod_forma = []
cod_margenes = []
cod_fe1 = []
cod_fe2 = []
cod_fe3 = []
cod_fe4 = []
tamaño = []

cant_pac = int(input())

while contador < cant_pac:
    datos = input()
    datos_divididos = datos.split()

    cod_composicion.append(datos_divididos[0])
    
    if cod_composicion[contador] == "C3":
        puntaje += 2
    elif cod_composicion[contador] == "C4":
        puntaje += 4

    cod_ecogenicidad.append(datos_divididos[1])

    if cod_ecogenicidad[contador] == "E2":
        puntaje += 2
    elif cod_ecogenicidad[contador] == "E3":
        puntaje += 4
    elif cod_ecogenicidad[contador] == "E4":
        puntaje += 6

    cod_forma.append(datos_divididos[2])

    if cod_forma[contador] == "F2":
        puntaje += 6

    cod_margenes.append(datos_divididos[3])

    if cod_margenes[contador] == "M3":
        puntaje += 4
    elif cod_margenes[contador] == "M4":
        puntaje += 6

    cod_fe1.append(int(datos_divididos[4]))
    cod_fe2.append(int(datos_divididos[5]))
    cod_fe3.append(int(datos_divididos[6]))
    cod_fe4.append(int(datos_divididos[7]))

    if cod_fe2[contador] == 1:
        fe2 = 2
    if cod_fe3[contador] == 1:
        fe3 = 4
    if cod_fe4[contador] == 1:
        fe4 = 6

    puntaje += fe1 + fe2 + fe3 + fe4

    tamaño.append(float(datos_divididos[8]))

    if puntaje >= 0 and puntaje <= 3:
        sin_riesgo += 1
        cont_no_aaf += 1
    elif puntaje >= 4 and puntaje <= 5:
        alerta_azul += 1
        cont_no_aaf += 1
    elif puntaje >= 6 and puntaje <= 7:
        alerta_verde += 1
        if tamaño[contador] >= 2.5:
            cont_aaf += 1
        else:
            cont_seg += 1
    elif puntaje >= 8 and puntaje <= 12:
        alerta_amarilla += 1
        if tamaño[contador] >= 1.5:
            cont_aaf += 1
        else:
            cont_seg += 1
    elif puntaje >= 13:
        alerta_roja += 1
        if tamaño[contador] >= 1:
            cont_aaf += 1
        else:
            cont_seg += 1

    suma_tam += tamaño[contador]
    puntaje = 0
    fe1 = 0
    fe2 = 0
    fe3 = 0
    fe4 = 0
    contador += 1

promedio = suma_tam / cant_pac

print(sin_riesgo, alerta_azul, alerta_verde, alerta_amarilla, alerta_roja)
print(f"{promedio:.2f}")
print(cont_no_aaf, cont_seg, cont_aaf)