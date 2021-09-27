#include <stdio.h>

int main()
{

    int actual, cumple, edad;
    actual = 2021;

    printf("en que año naciste? \n");
    scanf(" %d", &cumple);
    if (actual < cumple)
    {
        printf("vienes del futuro \n ");
    }
    else
    {
        edad = actual - cumple;
        printf("tienes %d años \n", edad);
        if (cumple % 4 == 0)
        {
            printf("tu año de nacimiento es bisiesto \n");
        }
    }
    return 0;
}