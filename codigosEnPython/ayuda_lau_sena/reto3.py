entrada = input().split(" ")
letras = []
numeros = []
count = 1
largo = len(entrada)
i = 0

while(i<largo): 
    if i+1< largo:
        if entrada[i]==entrada[i+1]:
            count+=1      
        else:
            letras.append(entrada[i])
            numeros.append(str(count))
            count=1
    else:
        letras.append(entrada[i])
        numeros.append(str(count))
    i+=1
print(' '.join(letras))
print(' '.join(numeros))