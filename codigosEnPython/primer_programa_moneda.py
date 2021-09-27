# Acción a realizar
accion = int(input("""¿Que acción deseas realizar? 

1.Cambiar de mi moneda a Dolares 
2.Cambiar de dolares a mi moneda 
3.Ninguna \n"""))

if accion == 1:
    #Pedir moneda al usuario
    moneda = input("¿Cuál de las siguientes es tu moneda? 1.Colombia 2.México 3.Argentina 4.nunguna")
    moneda = int(moneda)
    if moneda == 1:
        colombia = input("Ingresa la cantidad de pesos colombianos ")
        colombia = float(colombia)
        r_c = colombia * 0.0013
        r_c = round(r_c,2)
        print("De pesos COLOMBIANOS a dolares es: " + str(r_c))
    elif moneda == 2:
        mexico = input("Ingresa la cantidad de pesos mexicanos ")  
        mexico = float(mexico)
        r_m = mexico * 0.044
        r_m = round(r_m,2)
        print("De pesos MEXICANOS a dolares es: " + str(r_m))
    elif moneda == 3:
        argentina = input("Ingresa la cantidad de pesos argentinos ")
        argentina = float(argentina)
        r_a = argentina * 0.014
        r_a = round(r_a,2)
        print("De pesos ARGENTINOS a dolares es: " + str(r_a))
    elif moneda == 4:
        argentina = input("Ingresa la cantidad de pesos peruaanos ")
        argentina = float(argentina)
        r_a = argentina * 0.014
        r_a = round(r_a,2)
        print("De pesos ARGENTINOS a dolares es: " + str(r_a))
        
elif accion == 2:
    #Pedir moneda al usuario
    moneda = input("¿Cuál de las siguientes es tu moneda? 1.Colombia 2.México 3.Argentina 4.peru 5.ninguna ")
    moneda = int(moneda)
    if moneda == 1:
        colombia = input("Ingresa la cantidad de dolares: ")
        colombia = float(colombia)
        r_c = colombia * 3724.01000
        r_c = round(r_c,2)
        print("De DOLARES a pesos COLOMBIANOS: " + str(r_c))
    elif moneda == 2:
        mexico = input("Ingresa la cantidad de dolares: ")  
        mexico = float(mexico)
        r_m = mexico * 21.94500
        r_m = round(r_m,2)
        print("De DOLARES a pesos MEXICANOS: " + str(r_m))
    elif moneda == 3:
        argentina = input("Ingresa la cantidad de dolares: ")
        argentina = float(argentina)
        r_a = argentina * 72.13500
        r_a = round(r_a,2)
        print("De DOLARES a pesos ARGENTINOS: " + str(r_a))
    elif moneda == 4:
        peru = input("Ingresa la cantidad de dolares: ")
        peru = float(peru)
        r_p = peru * 34.13500
        r_p = round(r_p,2)
        print("De DOLARES a pesos Peruanos: " + str(r_p))
    elif moneda == 5:
        print("no se realizar su conversion")
elif accion == 3:
    print("No se realizará ninguna conversión de nada! bye!")