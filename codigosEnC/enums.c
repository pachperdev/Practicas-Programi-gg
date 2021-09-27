#include <stdio.h>

enum weekDays
{
  Monday,
  Tuesday,
  Wednesday,
  Thursday,
  Friday,
  Saturday,
  Sunday
}; /* Es como una lista. pero también se le pueden 
  asignar valores a las variables de la lista. si no se hace, por defecto será 
  “constante1 = 0, constante2 = 1, constante3 = 2” y así … */

int main()
{
  enum weekDays today;
  today = Sunday;
  printf("DAY %d", today); /* colocamos "/d", por que queremos de salida un valor entero. pero solo lo ponemos justo antes de nustra 
     variable a mostrar */
  return 0;
}