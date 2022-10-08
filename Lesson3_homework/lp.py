import math
class complex_numb():
    def __init__(self,x=0, y=0):
        self.set(x,y)
    def set(self, x, y):
        self.x = x
        self.y = y
    def __plus__(self, z2):
        a = self.x + z2.x
        b = self.y + z2.y
        return a,b
    def __minus__(self, z2):
        a = self.x - z2.x
        b = self.y - z2.y
        return a,b
    def __mult__(self, z2):
        a = self.x * z2.x - self.y * z2.y
        b = self.y * z2.x + z2.y * self.x
        return a, b
    def __delim__(self,z2):
        a = (self.x * z2.x + self.y * z2.y) / (z2.x**2 + z2.y**2)
        b = (self.y * z2.x - self.x * z2.y) / (z2.x**2 + z2.y**2)
        return a, b
    def get_v_exp(self):
        self.r = math.sqrt(( self.x**2 ) + ( self.y**2 ))
        if self.x == 0:
            if self.y > 0:
                self.phi = math.pi / 2
            else:
                self.phi = -math.pi / 2
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
        return a,b
z1 = complex_numb (5, 3)
z2 = complex_numb (9, 4)
print( 'Ответы представлены в виде пары точек (x,y), где z = x+iy' )
print('summa =', z1.__plus__(z2))
print('raznost =', z1.__minus__(z2))
print('umnozhenie =', z1.__mult__(z2))
print('delenie =' ,z1.__delim__(z2))
print ('(r, phi) = ' , z1.get_v_exp())
print ('algebr. chislo', z1.get_iz_exp())




