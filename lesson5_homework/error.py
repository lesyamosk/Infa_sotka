import math
import numbers
class complex_numb():
    def __init__(self,x=0, y=0):
        self.set(x,y)
    def set(self, x, y):
        if isinstance(x, numbers.Number) and isinstance(y, numbers.Number):
            self.x = x
            self.y = y
        else:
            raise ValueError
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
    def get_v_exp(self):
        self.r = math.sqrt(( self.x**2 ) + ( self.y**2 ))
        if self.x == 0:
            raise Exception ('его нельзя перевести, лол. Введи что-то другое')
        elif self.x > 0:
            self.phi = math.atan(self.y / self.x)
        elif self.x < 0:
            if self.y >= 0:
                self.phi = math.pi + math.atan(self.y / self.x)
            else:
                self.phi = -math.pi + math.atan(self.y / self.x)
        return self.r, self.phi
    def get_iz_exp(self):
        a = self.r*math.cos(self.phi)
        b = self.r*math.sin(self.phi)
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
        else:
            raise ValueError

    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
            return
        if key == 1:
            self.y = value
        else:
            raise ValueError


z1 = complex_numb (5, 3)
z2 = complex_numb (9, 4)

print(1.9 + z1)
print( z1==1 )
print(abs(z1))
print(3*z1)
print(z1*0.7)
print(z2)
print(z1+z2)
print(z1-z2)
print(z1*z2)
print(z1//z2)
