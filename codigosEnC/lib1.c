#include <stdio.h>
#include <math.h>

int x;
float result;

int main()
{

    printf("ingrese el valor de x: ");
    scanf("%d", &x);
    printf("el valor de x es: %d \n", x);
    result = sin(x);
    printf("el valor del coseno de x es: %f\n", result);
    return 0;
}