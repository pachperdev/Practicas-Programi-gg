
from matplotlib import pyplot
import pylab as pl
import numpy as np
from math import sqrt


#print("el valor de T_ind es: " , int(T_ind))
#print("el valor del torque es: {}".format(T_ind))

print("hola, que tipo de motor desea seleccionar.")
seleccion_motor = input("1.exitacion separada, 2.derivacion, 3.serie, 4.compuesta \n")
print("su opcion seleccionada fue " + seleccion_motor)
seleccion_motor_int = int(seleccion_motor)

if seleccion_motor_int == 1:
    #ECUCIONES DEL MOTOR EN EXITACION SEPARADA 
    Ko = 2
    Rf = 50
    
    print("ingrese el voltaje en las terminales\n")
    Vt = float(input())
    print("ingrese el valor de la resistencia de armadura")
    Ra = float(input())
    print("ingrese la corriente de armadura\n")
    Ia = float(input())
    
    T_ind = Ko*Ia
    Wm = (Vt/Ko)-(Ra/(Ko**2))*(T_ind)
    If = Vt/Rf
    p_sal = T_ind * Wm
    p_ent = Vt*Ia
    n = (p_sal/p_ent)
    
    T_ind = np.linspace(0,10,10)
    Wm = (Vt/Ko)-(Ra/(Ko**2))*(T_ind)

    pyplot.figure()
    pyplot.plot(T_ind, Wm,"b")
    pyplot.title("Par-Velocidad")

    Wm = np.linspace(0,10,10)
    n = (T_ind*Wm)/(Vt*Ia)*100
    pyplot.figure()
    pyplot.plot(n, T_ind,"b")
    pyplot.title("eficiencia")

if seleccion_motor_int == 2:
    #ECUCIONES DEL MOTOR EN DERIVACION
    Ko = 2
    Rf = 50
    Ra = 0.006
    
    print("ingrese el voltaje en las terminales\n")
    Vt = float(input())
    print("ingrese el valor de la resistencia de campo\n")
    Rf = float(input())
    print("ingrese la corriente de linea\n")
    Il = float(input())
    If = Vt/Rf
    Ia = Il - If
    T_ind = Ko*Ia
    Wm = (Vt/Ko)-(Ra/(Ko**2))*(T_ind)
    Ea = Ko*Wm
    p_sal = T_ind * Wm
    p_ent = Vt*Ia
    n = (p_sal/p_ent)

    T_ind = np.linspace(0,10,10)
    Wm = (Vt/Ko)-(Ra/(Ko**2))*(T_ind)

    pyplot.figure()
    pyplot.plot(T_ind, Wm,"b")
    pyplot.title("Par-Velocidad")

    Wm = np.linspace(0,10,10)
    n = (T_ind*Wm)/(Vt*Ia)*100
    pyplot.figure()
    pyplot.plot(n, T_ind,"b")
    pyplot.title("eficiencia")
    
if seleccion_motor_int == 3:
    #ECUCIONES DEL MOTOR EN SERIE
    K = 1
    Rf = 0.06
    Ra= 0.009
    c = 1
    
    print("ingrese el voltaje en las terminales\n")
    Vt = float(input())
    print("ingrese el valor de la resistencia en serie con la armadura\n")
    Rs = float(input())
    print("ingrese la corriente de linea\n")
    Il = float(input())
    
    Ia = Il
    T_ind = K*c*Ia**2
    o = np.sqrt(c/K)*np.sqrt(T_ind)
    Wm = (Vt/np.sqrt(K*c))*(1/np.sqrt(T_ind))-(Ra+Rs/K*c)

    T_ind = np.linspace(0,10,10)
    Wm = (Vt/np.sqrt(K*c))*(1/np.sqrt(T_ind))-(Ra+Rs/K*c)

    pyplot.figure()
    pyplot.plot(T_ind, Wm,"b")
    pyplot.title("Par-Velocidad")

    Wm = np.linspace(0,10,10)
    n = (T_ind*Wm)/(Vt*Ia)*100
    pyplot.figure()
    pyplot.plot(n, T_ind,"b")
    pyplot.title("eficiencia")

if seleccion_motor_int = 4
    


