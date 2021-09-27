C = input("")
E = input("")
F = input("")
M = input("")
FE1 = input("")
FE2 = input("")
FE3 = input("")
FE4 = input("")
Tam = float(input(""))

if  C == "C1" or C == "C2":
    cont_c = 0
elif C == "C3":
    cont_c = 2
elif C == "C4":
    cont_c = 4

if  E == "E1":
    cont_e = 0
elif E == "E2":
    cont_e = 2
elif E == "E3":
    cont_e = 4
elif E == "E4":
    cont_e = 6

if  F == "F1":
    cont_f = 0
elif F == "F2":
    cont_f = 6

if  M == "M1" or M == "M2":
    cont_m = 0
elif M == "M3":
    cont_m = 4
elif M == "M4":
    cont_m = 6

FE = int(FE1)*0 + int(FE2)*2 + int(FE3)*4 + int(FE4)*6
cont_g = cont_c + cont_e + cont_f + cont_m + FE

if cont_g <= 3:
    print("sin riesgo")
    print("no aaf")
if cont_g >= 4 and cont_g <= 5:
    print("alerta Azul")
    print("no aaf")
if cont_g >= 6 and cont_g <= 7 and Tam >= 2.5: 
    print("alerta verde")
    print("aaf")
elif cont_g >= 6 and cont_g <= 7 and Tam < 2.5: 
    print("alerta verde")
    print("seguimiento")
if cont_g >= 8 and cont_g <= 12 and Tam >= 1.5: 
    print("alerta amarilla")
    print("aaf")
elif cont_g >= 8 and cont_g <= 12 and Tam < 1.5: 
    print("alerta amarilla")
    print("seguimiento")
if cont_g >= 13 and Tam >= 1: 
    print("alerta roja")
    print("aaf")
elif cont_g >= 13 and Tam < 1: 
    print("alerta roja")
    print("seguimiento")