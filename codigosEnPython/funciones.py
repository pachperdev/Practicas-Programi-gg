def moneda_a_dolar(pais, valor_dolar):
    pesos = input("Ingresa la cantidad de pesos " + pais + "\n")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares)  
    print(pesos, "pesos ",pais, "a dolares es: ",dolares, "dolares\n")
def dolar_a_moneda(pais, valor_peso_pais):
    dolares = input("Ingresa la cantidad de dolares\n")
    dolares = float(dolares)
    valorapais = dolares / valor_peso_pais
    valorapais = round(valor_peso_pais)  
    print(dolares,"dolares a pesos", pais, "son: ", valorapais,"\n")

accion = input("""¿Que acción deseas realizar?

1.Cambiar de mi moneda a Dolares 
2.Cambiar de dolares a mi moneda 
3.Ninguna \n""")
if accion == "1":
    moneda = input("""¿Cuál de las siguientes es tu moneda? 

    1.Colombiana
    2.Méxicana
    3.Argentina 
    4.nunguna \n""")
    if moneda == "1":
        moneda_a_dolar("colombianos", 3800)
    elif moneda == "2":
        moneda_a_dolar("mexicanos", 65)
    elif moneda == "3":
        moneda_a_dolar("argentinos", 24)
    elif moneda == "4":
        print("No se selecciono ninguna moneda\n")
elif accion == "2":
    moneda = input(("""¿Cuál de las siguientes es tu moneda? 
    
    1.Colombia 
    2.México 
    3.Argentina 
    4.ninguna \n"""))
    if moneda == "1":
        dolar_a_moneda("colombianos", 3800)
    elif moneda == "2":
        moneda_a_dolar("colombianos", 38)
    elif moneda == "3":
        moneda_a_dolar("colombianos", 38)
    elif moneda == "4":
        print("no se realizar su conversion\n")        
elif accion == "3":
    print("No se realizará ninguna conversión de nada! bye!C")