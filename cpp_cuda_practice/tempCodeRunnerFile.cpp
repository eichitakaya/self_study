#include <iostream>
using namespace std;

int main()
{
    for(int i=1; i<=30; i++){
        if(i<10){
            cout.width(3);
            cout.fill('-');
        }
        else{
            cout.width(2);
            cout.fill('-');
        }
        cout << i;
    }

    return 0;
}