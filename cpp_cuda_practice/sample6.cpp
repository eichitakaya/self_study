#include <iostream>
using namespace std;

void buy(int* pX1, int* pX2, int a)
{
    *pX1 += a;
    *pX2 += a;
}
int main()
{
    int x1;
    int x2;
    int a;
    int* pX1;
    int* pX2;

    pX1 = &x1;
    pX2 = &x2;

    cout << "2科目分の点数を入力してください．\n";
    cin >> x1;
    cin >> x2;
    cout << "加算する点数を入力してください．\n";
    cin >> a;
    buy(pX1, pX2, a);
    cout << a << "点加算しましたので\n" ;
    cout << "科目1は" << x1 << "点となりました\n";
    cout << "科目2は" << x2 << "点となりました\n";

}