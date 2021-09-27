cantidadAlertaAzul = 0
cantidadAlertaAmarilla = 0
cantidadAaf = 0
cantidadNoAaf = 0
cantidadSeguimiento = 0
promedioTam = 0
Tam = 0
sumaTam = 0
Puntos = 0
Numero_pacientes = float(input(""))
pacientes = Numero_pacientes 

while Numero_pacientes > 0:
    C = input("")
    E = input("")
    F = input("")
    M = input("")
    FE1 = input("")
    FE2 = input("")
    FE3 = input("")
    FE4 = input("")
    Tam = float(input(""))
    sumaTam = sumaTam + Tam

    if  C == "C1" or C == "C2":
        Puntos = Puntos + 0
    elif C == "C3":
        Puntos = Puntos + 2
    elif C == "C4":
        Puntos = Puntos + 4

    if  E == "E1":
        Puntos = Puntos + 0
    elif E == "E2":
        Puntos = Puntos + 2
    elif E == "E3":
        Puntos = Puntos + 4
    elif E == "E4":
        Puntos = Puntos + 6

    if  F == "F1":
        Puntos = Puntos + 0
    elif F == "F2":
        Puntos = Puntos + 6

    if  M == "M1" or M == "M2":
        Puntos = Puntos + 0
    elif M == "M3":
        Puntos = Puntos + 4
    elif M == "M4":
        Puntos = Puntos + 6

    Puntos = Puntos + int(FE1)*0 + int(FE2)*2 + int(FE3)*4 + int(FE4)*6

    if Puntos >= 0 and Puntos <= 3:
        cantidadNoAaf += 1
    elif Puntos >= 4 and Puntos <= 5:
        cantidadAlertaAzul += 1
        cantidadNoAaf += 1
    elif Puntos >= 6 and Puntos <= 7:
        if Tam >= 2.5:
            cantidadAaf += 1
        else:
            cantidadSeguimiento += 1
    elif Puntos >= 8 and Puntos <= 12:
        if Tam >= 1.5:
            cantidadAlertaAmarilla += 1
            cantidadAaf += 1
        else:
            cantidadAlertaAmarilla += 1
            cantidadSeguimiento += 1
    elif Puntos >= 13:
        if Tam >= 1:
            cantidadAaf += 1
        else:
            cantidadSeguimiento += 1

    Numero_pacientes = Numero_pacientes - 1

promedioTam = sumaTam / pacientes
print("alerta azul", cantidadAlertaAzul)
print("alerta amarilla", cantidadAlertaAmarilla)
print("{0:.2f}".format(promedioTam))
print("No aaf", cantidadNoAaf)
print("Seguimiento", cantidadSeguimiento)
print("aaf", cantidadAaf)   