#ALGORITMO QUE COMPRUEBA SI EL VALOR INGRESADO ES UN ENTERO O NO.

print("ingrese un numero")
numero = float(input())

if numero%1 == 0:
    print("el valor ingresado si es numero entero\n")  
elif numero%1 != 0:
    print("el numero no es un entero\n")

