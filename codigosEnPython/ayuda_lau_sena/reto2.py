compa_ABC = input("Por favor ingrese los productos de la compañia ABC: ")
compa_XYZ = input("Por favor ingrese los productos de la compañia XYZ: ")
letra = ""
ventas = input("Por favor ingrese las ventas realizadas durante la semana: ")
cont_ABC = 0
cont_XYZ = 0
for i in ventas:
    if i in compa_ABC:
        cont_ABC+=1
    if i in compa_XYZ:
        cont_XYZ+=1
    if cont_ABC == cont_XYZ:
        letra +="I"
    if cont_ABC > cont_XYZ:
        letra+="P"
    if cont_ABC < cont_XYZ:
        letra+="N"
print(letra)