azucar = int(input("ingresa número: "))
harina = azucar * 2 + 4
mantequilla = (azucar + harina) // 5

print(azucar, harina, mantequilla)

if mantequilla >= 1 and mantequilla <= 20:
    print("uno")
elif mantequilla >= 21 and mantequilla <= 30:
    print("dos")
elif mantequilla >= 31 and mantequilla <= 50:
    print("tres")
elif mantequilla > 50:
    print("cuatro")