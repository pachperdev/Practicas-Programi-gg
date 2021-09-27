#include <iostream>
using namespace std;

int main()
{
    char inicial;
    int edad;
    float precio;
    cout << "Ingrese la inicial de su nombre, su edad y el valor de su bebida favorita: " << endl;
    cin >> inicial >> edad >> precio;
    cout << "Inicial: " << inicial << endl << "Edad: " << edad << endl << "Precio: " << precio;
    return 0;
}