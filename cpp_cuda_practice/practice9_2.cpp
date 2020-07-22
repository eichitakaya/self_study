#include <iostream>
using namespace std;

int length(char* str)
{
    int cnt = 0;
    for(int i=0; str[i]!='\0'; i++){
        cnt += 1;
    }
    return cnt;
}

int main()
{
    char str[100];
    
    cout << "文字列を入力してください．\n";

    cin >> str;

    cout << "文字列の長さは" << length(str) << "です．\n";

    return 0;
}