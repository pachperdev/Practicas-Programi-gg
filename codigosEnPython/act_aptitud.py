
from matplotlib import pyplot
import pylab as pl
import numpy as np

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
    Vt = int(input())
    print("ingrese el valor de la resistencia de armadura")
    Ra = int(input())
    print("ingrese la corriente de armadura\n")
    Ia = int(input())
    
    T_ind = Ko*Ia
    Wm = (Vt/Ko)-(Ra/(Ko**2))*(T_ind)
    If = Vt/Rf
    p_sal = T_ind * Wm
    p_ent = Vt*Ia
    n = (p_sal/p_ent)*100
    
    print("la eficiencia es de: ", n)


    def f(T_ind):
        return (Vt/Ko)-(Ra/(Ko**2))*(T_ind)

    T_ind = range(0, 20)
    pyplot.plot(T_ind, [f(i) for i in T_ind])

    #Titulo de la Grafica
    pyplot.title('Curva par - velocidad')

    #Establecemos el color de los ejes
    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")

    #Nombre de los ejes x,y
    pyplot.xlabel('T_ind')
    pyplot.ylabel('Wm')

    # Limitar los valores de los ejes.
    pyplot.ylim(0)
    pyplot.ylim(0)

    #Mostramos el gráfico.
    pyplot.show()

elif seleccion_motor_int = 2: #Derivacion

    #ECUCIONES DEL MOTOR EN DERIVACION
    Ko = 2
    Rf = 50
    
    print("ingrese el voltaje en las terminales\n")
    Vt = int(input())
    print("ingrese el valor de la resistencia de armadura")
    Ra = int(input())

    If = Vt/Rf
    
    Ia = (Vt - Ea)/(Ra)
    Wm = (Vt/Ko)-(Ra/(Ko)**2)*(T_ind)
    Ea = Ko*Wm
    T_ind = Ko*Ia
    Wm = (Vt/Ko)-(Ra/(Ko**2))*(T_ind)
    If = Vt/Rf
    p_sal = T_ind * Wm
    p_ent = Vt*Ia
    n = (p_sal/p_ent)*100
    
    print("la eficiencia es de: ", n)


    def f(T_ind):
        return (Vt/Ko)-(Ra/(Ko**2))*(T_ind)

    T_ind = range(0, 20)
    pyplot.plot(T_ind, [f(i) for i in T_ind])

    #Titulo de la Grafica
    pyplot.title('Curva par - velocidad')

    #Establecemos el color de los ejes
    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")

    #Nombre de los ejes x,y
    pyplot.xlabel('T_ind')
    pyplot.ylabel('Wm')

    # Limitar los valores de los ejes.
    pyplot.ylim(0)
    pyplot.ylim(0)

    #Mostramos el gráfico.
    pyplot.show()

    

