#include <iostream>
using namespace std;

int main()
{
    int matrix[5][3] = 
    {
        {0,0,0,},
        {0,0,0,},
        {0,0,0,},
        {0,0,0,},
        {0,0,0,}
    };

    for(int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cout << matrix[i][j];
        };

        cout << endl;
    };   

    return 0;
}