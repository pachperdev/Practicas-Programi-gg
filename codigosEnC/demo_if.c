#include <stdio.h>

int main()
{
    if (0)
    {
        printf("el valor es falso");
    }
    else if (1)
    {
        printf("el valor es verdadero \n"); // De esta manera damos un salto de linea.
    }

    int n = 20;

    if (n > 10 && n < 20)
        printf("el numero es mayor que diez, pero menor que 20");
    else if (n == 10)
        printf("el numero es diez");
    else if (n > 20)
        printf("el numero es mayor que veinte");
    else if (n < 10 && n >= 0)
        printf("el numero esta en el rango de 0 a 9");
    else
        printf("ERROR no quiero numeros negativos");
    return 0;
}