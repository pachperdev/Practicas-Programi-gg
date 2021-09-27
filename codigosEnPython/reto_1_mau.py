C = input("")
E = input("")
F = input("")
M = input("")
FE1 = input("")
FE2 = input("")
FE3 = input("")
FE4 = input("")
Tam = float(input(""))
Puntos = 0

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

if Puntos <= 3:
    print("sin riesgo")
    print("no aaf")
if Puntos >= 4 and Puntos <= 5:
    print("alerta Azul")
    print("no aaf")
if Puntos >= 6 and Puntos <= 7 and Tam >= 2.5: 
    print("alerta verde")
    print("aaf")
elif Puntos >= 6 and Puntos <= 7 and Tam < 2.5: 
    print("alerta verde")
    print("seguimiento")
if Puntos >= 8 and Puntos <= 12 and Tam >= 1.5: 
    print("alerta amarilla")
    print("aaf")
elif Puntos >= 8 and Puntos <= 12 and Tam < 1.5: 
    print("alerta amarilla")
    print("seguimiento")
if Puntos >= 13 and Tam >= 1: 
    print("alerta roja")
    print("aaf")
elif Puntos >= 13 and Tam < 1: 
    print("alerta roja")
    print("seguimiento")