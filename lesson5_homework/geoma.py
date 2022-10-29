class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get1(self):
        return self._x

    def get2(self):
        return self._y

    def set1(self, x):
        self._x = x

    def set2(self, y):
        self._y = y
def rasstoyanie(A1, A2):
    return ((A2.get1() - A1.get1()) ** 2+(A2.get2() - A1.get2()) ** 2 ) ** 0.5
class Forma:
    def __init__(self, type = '0'):
        self._type = type

    def __str__(self):
        return ('Тип фигуры: ' + str(self._type) + ", S = " + str(self.area()) + ", P = " +  str(self.perimeter())+'.')

class four_angle (Forma):
    def __init__(self, point1, point2, point3, point4, type="Quadrangle"):
        super().__init__(type)
        self._point1 = point1
        self._point2 = point2
        self._point3 = point3
        self._point4 = point4
        self._a1a2 = rasstoyanie(self._point1, self._point2)
        self._a2a3 = rasstoyanie(self._point2, self._point3)
    def perimeter(self):
        return (self._a1a2 + self._a2a3)*2


class circle(Forma):
    def __init__(self, radius, centre, type = "circle"):
        super().__init__(type)
        self._radius = radius
        self._centre = centre

    def area(self):
        import math
        return rasstoyanie(self._centre, self._radius) ** 2 * math.pi

    def perimeter(self):
        import math
        return 2 * rasstoyanie(self._centre, self._radius) *math.pi
class triangle(Forma):
    def __init__(self, point1 ,point2 ,point3, type="triangle"):
        super().__init__(type)
        self._point1 = point1
        self._point2 = point2
        self._a1a2 = rasstoyanie(self._point1, self._point2)
        self._point3 = point3
        self._b1b2 = rasstoyanie(self._point2, self._point3)
        self._c1c2 = rasstoyanie(self._point1, self._point3)

    def perimeter(self):
        P_tr=self._a1a2 + self._b1b2 + self._c1c2
        return P_tr

    def area(self):
        # по формуле Герона
        ro = self.perimeter() / 2
        S_tr = (ro * (ro - self._a1a2) * (ro - self._b1b2) * (ro - self._c1c2)) ** 0.5
        return S_tr
class rectangle(four_angle):
    def __init__(self, point1, point2, point3, point4, type="rectangle"):
        super().__init__(point1, point2, point3, point4, type)
    def area(self):
        S_rec= self._a1a2 * self._a2a3
        return S_rec
class rhombus(four_angle):
    def __init__(self, point1, point2, point3, point4, type="rhombus"):
        super().__init__(point1, point2, point3, point4,type)
    def area(self):
        S_rh = rasstoyanie(self._point1, self._point3) * rasstoyanie(self._point2, self._point4)/2
        return S_rh

class square(rectangle):
    def __init__(self, point1, point2, point3, point4, type="square"):
        super().__init__(point1, point2, point3, point4, type)


okr = circle(Point(0,0), Point(0,8))
sq = square (Point(0,0), Point(0,8), Point(8,8), Point(8,0))
print(okr, sq)