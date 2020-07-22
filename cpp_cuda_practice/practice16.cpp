#include <iostream>
using namespace std;

int main()
{
    for(int i=1; i<=30; i++){
        cout.width(3);
        cout.fill('-');
    
      
        if(i%5==0){
            cout << i << endl;
        }
        else{
            cout << i;
        }
    }

    return 0;
}