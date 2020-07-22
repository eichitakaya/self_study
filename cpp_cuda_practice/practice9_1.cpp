#include <iostream>
using namespace std;

int max(int x[], int num)
{
    for(int s=0; s<num-1; s++){
        for(int t=s+1; t<num; t++){
            if(x[t] > x[s]){
                int tmp = x[t];
                x[t] = x[s];
                x[s] = tmp;
            }
        }
    }
    return x[0];
}

int main()
{
    const int num = 5;
    int test[num];

    cout << "テストの点数を入力してください\n";

    for(int i=0; i<num; i++){
        cin >> test[i];
    }
    
    cout << "最高点は" << max(test, num) << "点です\n";
    
    return 0;
}