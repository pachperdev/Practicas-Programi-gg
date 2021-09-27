import random

def run():
    numero_aleatorio = random.randint(1,10)
    vidarestante = 3
    print("Tienes", vidarestante, "oportunidades para adivinar un numero del 1 a 10")
    while 0 < vidarestante:
        elegido = int(input('Ingrese un numero: '))
        if elegido != numero_aleatorio:
            print("No has acertado")
            if elegido > numero_aleatorio:
                print('El numero es menor')
            elif elegido < numero_aleatorio:
                print('El numero es mayor')
            vidarestante = vidarestante - 1
            print('Te quedan', vidarestante, 'vidas restantes\n')
            if vidarestante == 0:
                print('El numero era el:', numero_aleatorio,',', 'Suerte la proxima\n')
        if elegido == numero_aleatorio:
            print("Ganaste, eres el mejor crack\n")
            vidarestante = 0


if __name__ == '__main__':
    run()