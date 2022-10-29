import math
import numbers
class complex_numb():
    def __init__(self,x=0, y=0):
        self.set(x,y)
    def set(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, z2):
        if isinstance(z2, numbers.Number):
            a = self.x + z2
            b = self.y
            return str(a)+' + i*'+str(b)
        a = self.x + z2.x
        b = self.y + z2.y
        return str(a)+' + i*'+str(b)
    def __radd__(self, z2):
        if isinstance(z2, numbers.Number):
            a = self.x + z2
            b = self.y
            return str(a)+' + i*'+str(b)
        a = self.x + z2.x
        b = self.y + z2.y
        return str(a)+' + i*'+str(b)
    def __sub__(self, z2):
        if isinstance(z2, numbers.Number):
            a = self.x - z2
            b = self.y
            return str(a)+' + i*'+str(b)
        a = self.x - z2.x
        b = self.y - z2.y
        return str(a)+' + i*'+str(b)
    def __rsub__(self, z2):
        if isinstance(z2, numbers.Number):
            a = -self.x + z2
            b = self.y
            return str(a)+' + i*'+str(b)
        a = -self.x + z2.x
        b = -self.y + z2.y
        return str(a)+' + i*'+str(b)
    def __mul__(self, z2):
        if isinstance(z2, numbers.Number):
            a = self.x * z2
            b = self.y * z2
            return str(a)+' + i*'+str(b)
        a = self.x * z2.x - self.y * z2.y
        b = self.y * z2.x + z2.y * self.x
        return str(a)+' + i*'+str(b)
    def __rmul__(self, z2):
        if isinstance(z2, numbers.Number):
            a = self.x * z2
            b = self.y * z2
            return str(a)+' + i*'+str(b)
        a = self.x * z2.x - self.y * z2.y
        b = self.y * z2.x + z2.y * self.x
        return str(a)+' + i*'+str(b)
    def __floordiv__(self,z2):
        if isinstance(z2, numbers.Number):
            a = self.x / z2
            b = self.y / z2
            return str(a)+' + i*'+str(b)
        a = (self.x * z2.x + self.y * z2.y) / (z2.x ** 2 + z2.y ** 2)
        b = (self.y * z2.x - self.x * z2.y) / (z2.x ** 2 + z2.y ** 2)
        return str(a)+' + i*'+str(b)
    def __rfloordiv__(self,z2):
        if isinstance(z2, numbers.Number):
            a = z2 / self.x
            b = z2 / self.y
            return str(a)+' + i*'+str(b)
        a = (self.x * z2.x + self.y * z2.y) / (self.x ** 2 + self.y ** 2)
        b = (-self.y * z2.x + self.x * z2.y) / (self.x ** 2 + self.y ** 2)
        return str(a)+' + i*'+str(b)

        return str(a)+' + i*'+str(b)
    def __str__(self):
        if self.y > 0:
            return str(self.x)+' + i*'+str(self.y)
        if self.y < 0:
            return str(self.x)+' - i*'+str(-1*self.y)
        return str(self.x)

    def __eq__(self, z2):
        if isinstance(z2, numbers.Number):
            return self.x == z2 and self.y == 0
        return self.x == z2.x and self.y == z2.y

    def __abs__(self):
        return (self.x**2 + self.y**2)**(0.5)

    def __getitem__(self, key):
        if key == 0:
            return self.x
        if key == 1:
            return self.y

    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
            return
        if key == 1:
            self.y = value

print('Введите комплексное число z1 в виде чисел x y через пробел, где z = x + iy:')
try:
    x1, y1 = map(float,input().split())
except ValueError:
    print('Я ж сказала ввести два числа через пробел... перезапусти программу')
print('Введите комплексное число z2 в том же виде:')
try:
    x2, y2 = map(float,input().split())
except ValueError:
    print('Калькулятор создан для чисел, поэтому введи их пж пж')
print('введите операцию, которую хотите совершить над числами:')
operator = input()
z1 = complex_numb (x1, y1)
z2 = complex_numb (x2, y2)
if operator == '+':
    print ('z1 + z2 =', z1+z2)
elif operator == '-':
    print ('z1 - z2 =', z1-z2)
elif operator == 'abs':
    print('Модуль z1:', abs(z1))
    print('Модуль z2:', abs(z2))
elif operator == '*':
    print ('z1 * z2 =', z1*z2)
elif operator == '/':
    try:
        print ('z1 / z2 =', z1//z2)
    except ZeroDivisionError:
        print('Делить на ноль разрешено только Господу')
try:
    if operator not in ("+", "-", '/', '*', 'abs'):
        raise TypeError
except TypeError:
    print('таких операций нет (по крайней мере в моём субъективном мире)')