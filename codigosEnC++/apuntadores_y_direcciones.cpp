#include <iostream>

using namespace std;

int main()
{
    string dir = "CRA 10d #14-12";

    string* apuntardordir;
    apuntardordir = &dir;
    
    *apuntardordir = "CAMBIO DE DIR";

    cout << dir << endl;
    cout << apuntardordir << endl;
    cout << *apuntardordir << endl;

    return 0;
} 