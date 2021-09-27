#include <iostream>
#include <conio.h>
using namespace std;
int suma(int,int);
int resta(int,int);
int multiplicacion(int,int);
int division(int,int);
int main() {
	
	int a = 0, b = 0, ope = 0;
	char seg;
	do{
		system("cls");
		cout<<"\t===Calculadora Aritmetica==="<<endl;
		cout<<"\t _____________________"<<endl;
		cout<<"\t|  _________________  |"<<endl;
		cout<<"\t| | ALLAM        0. | |"<<endl;
		cout<<"\t| |_________________| |"<<endl;
		cout<<"\t|  ___ ___ ___   ___  |"<<endl;
		cout<<"\t| | 7 | 8 | 9 | | + | |"<<endl;
		cout<<"\t| |___|___|___| |___| |"<<endl;
		cout<<"\t| | 4 | 5 | 6 | | - | |"<<endl;
		cout<<"\t| |___|___|___| |___| |"<<endl;
		cout<<"\t| | 1 | 2 | 3 | | x | |"<<endl;
		cout<<"\t| |___|___|___| |___| |"<<endl;
		cout<<"\t| | . | 0 | = | | / | |"<<endl;
		cout<<"\t| |___|___|___| |___| |"<<endl;
		cout<<"\t|_____________________|"<<endl;
		cout<<"\nMenu de Operaciones:"<<endl;
		cout<<"\n\t1. Suma.\n\t2. Resta.\n\t3. Multiplicacion.\n\t4. Division."<<endl;
		cout<<"\nElija una opcion: ";
		cin>>ope;
		switch(ope){
		case 1:
			cout<<"\nSuma de numeros:"<<endl;
			cout<<"\n\tValor de A: ";
			cin>>a;
			cout<<"\tValor de B: ";
			cin>>b;
			cout<<"\tResultado: "<<suma(a,b);
			break;
		case 2:
			cout<<"\nResta de numeros:"<<endl;
			cout<<"\n\tValor de A: ";
			cin>>a;
			cout<<"\tValor de B: ";
			cin>>b;
			cout<<"\tResultado: "<<resta(a,b);
			break;
		case 3:
			cout<<"Multiplicacion de numeros:"<<endl;
			cout<<"\n\tValor de A: ";
			cin>>a;
			cout<<"\tValor de B: ";
			cin>>b;
			cout<<"\tResultado: "<<multiplicacion(a,b);
			break;
		case 4:
			cout<<"\nDivision de numeros:"<<endl;
			cout<<"\n\tValor de A: ";
			cin>>a;
			cout<<"\tValor de B: ";
			cin>>b;
			if(b == 0){
				cout<<"La division entre 0, no esta definida."<<endl;
			}else{
				cout<<"\tResultado: "<<division(a,b);
			}
			break;
		default:
			cout<<"Opcion no valida!!! :("<<endl;
		}
		cout<<"\n\nDesea realizar otra operacion? (S/N): ";
		cin>>seg;
	} while(seg == 'S' || seg == 's');
	cout<<"Gracias por usar la calculadora!!! :)"<<endl;
	return 0;
}
int suma(int a, int b){
	return a + b;
}
int resta(int a, int b){
	return a - b;
}
int multiplicacion(int a, int b){
	return a * b;
}
int division(int a, int b){
	return a / b;
}