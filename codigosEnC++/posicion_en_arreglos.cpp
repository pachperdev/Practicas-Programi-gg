#include <iostream>
using namespace std;

void drawmap(int heropos, char gamemap[5])
{
    for (int i = 0; i < 5; i++)
    {
        if(i != heropos)
        {
            cout << gamemap[i];
            
        }else if (i = heropos)
        {
            cout << 'H';
        }

    }

}    

int main()
{
    int heropos = 2;
    char gamemap[5] = {'*','*','*','*','*'};

    drawmap(heropos,gamemap);
    return 0;
}

