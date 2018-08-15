#include <iostream>
using namespace std;


//クラスの宣言
class Point{
    private:
        int x;
        int y;
    public:
        void setX(int a);
        void setY(int b);
        int getX();
        int getY();
};

//Pointクラスメンバ関数の定義
void Point::setX(int a)
{
    if(a >= 0 && a <=10){
        x = a;
    }
    else{
        cout << a << "は条件を満たしていません！\n";
    }
}

void Point::setY(int b)
{
    if(b >=0 && b <=10){
        y = b;
    }
    else{
        cout << b << "は条件を満たしていません！\n";
    }
}

int Point::getX()
{
    return x;
}

int Point::getY()
{
    return y;
}

int main()
{
    Point point1;
    
    int x;
    int y;

    cout << "X座標を入力してください\n";
    cin >> x;
    cout << "Y座標を入力してください\n";
    cin >> y;

    point1.setX(x);
    point1.setY(y);

    cout << "座標は(" << point1.getX() << ", " << point1.getY() << ")です．\n";
}