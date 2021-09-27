#include <iostream>
#include<math.h>


using namespace std;

int main()
{
    //area de una circunferencia y una esfera
    float pi = 3.1416;
    float radio = 2;
    float area_circun = pi*pow(radio,2);
    float area_esfera = 4*pi*pow(radio,2);

    cout << "" << endl;
    cout << "el area del circunferencia es de: " << area_circun << endl;
    cout << "" << endl;
    cout << "el area de la esfera es de: " << area_esfera << endl;

    return 0;
}