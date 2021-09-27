print("ingresar valor de primera nota")
primeranota = float(input())
print("primeranota=",primeranota)
print("ingresar valor de segunda nota")
segundanota = float(input())
print("segundanota=",segundanota)
valordeop=(primeranota+segundanota)
final=(valordeop/2)
print("su nota final es: ",final)

if final > 3 and final < 4:
    print("felicidades pero puedes mejorar")
elif final >= 4:
    print("felicidades, vas por el camino del exito")
elif final < 3:
    print("perdiste puedes hacerlo mejor la proxima")