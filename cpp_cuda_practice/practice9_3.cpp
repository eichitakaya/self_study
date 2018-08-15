#include <iostream>
using namespace std;

int count(char str[], char ch)
{
    int cnt = 0;
    for(int i=0; str[i]!='\0'; i++){
        if(str[i] == ch){
            cnt += 1;
        }
    }
    return cnt;
}

int main()
{
    char str[100];
    char ch;

    cout << "文字列を入力してください．\n";

    cin >> str;

    cout << "文字列から探す文字を入力してください．\n";

    cin >> ch;

    cout << str << "の中に" << ch << "は全部で" << count(str, ch) << "個あります．\n";

    return 0;
}