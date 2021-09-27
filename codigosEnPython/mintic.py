x = 3
y = 9
z = 5

if(y % x == 0):
    if(y >= z):
        x = x * x
    else :
        z = z * z
else:
    if(z >= x):
        if(y >= z):
            y = y * y
    else:
        z = z * z
if(y % x == 0):
    x = x + 3
else:
    y = y * 2

print("x = ", x)
print("y = ", y)
print("z = ", z)           