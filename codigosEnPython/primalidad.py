# def es_primo(numero):
#     contador = 0

#     for i in range(1, numero + 1):
#         if i == 1 or i == numero:
#             continue
#         if numero % i == 0:
#             contador += 1
#     if contador == 0:
#         return True
#     else:
#         return False


# def run():
#     numero = int(input('Escribe un numero: '))
#     if es_primo(numero):
#         print('Es primo')
#     else:
#         print('No es primo')


# if __name__ == '__main__':
#     run()


def es_primo(numero):
    factorial = 1
    for i in range(1,numero):
        factorial=factorial*i
    if  ( factorial + 1 ) % numero == 0: # Por teorema de wilson.
        return "Es primo"
    else:
        return "No es primo"
    

def run():
    numero = int(input("Escriba el numero >>:"))
    respuesta = es_primo(numero)
    print(respuesta)


if __name__ == "__main__":
    run()