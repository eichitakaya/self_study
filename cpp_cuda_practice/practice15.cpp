#include <iostream>
using namespace std;

class Point{
    private:
        int x;
        int y;
    public:
        Point(int a=0, int b=0){x=a; y=b;}
        void show(){cout<< "x :" << x << " y :" << y << "\n";}
        void setX(int a){x=a;}
        void setY(int b){y=b;}
        Point operator--();
        Point operator--(int d);
        friend Point operator-(Point p1, Point p2);
        friend Point operator-(Point p, int a);
        friend Point operator-(int a, Point p);
};

//Pointクラスメンバ関数の定義
Point Point::operator--()
{
    x--;
    y--;
    return *this;
}
Point Point::operator--(int d)
{
    Point p = *this;
    x--;
    y--;
    return p;
}

//フレンド関数の定義
Point operator-(Point p1, Point p2)
{
    Point tmp;
    tmp.x = p1.x - p2.x;
    tmp.y = p1.y - p2.y;
    return tmp;
}
Point operator-(Point p, int a)
{
    Point tmp;
    tmp.x = p.x - a;
    tmp.y = p.y - a;
    return tmp;
}
Point operator-(int a, Point p)
{
    Point tmp;
    tmp.x = a - p.x;
    tmp.y = a - p.y;
    return tmp;
}

int main()
{
    Point p1(1, 2);
    Point p2(3, 6);
    
    p1--;

    p1.show();
    return 0;
}