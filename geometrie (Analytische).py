class Punkt(object):
    def __init__(self,x1, x2, x3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
    def d_punkt_to_punkt(self, punkt):
        return "{:.4f}".format(((self.x1 - punkt.x1) ** 2 + (self.x2 - punkt.x2) ** 2 + (self.x3 - punkt.x3) ** 2)**0.5)

class Ebene(object):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def d_to_punkt(self, punkt):
        lot_g = Gerade([punkt.x1, punkt.x2, punkt.x3], [self.a, self.b, self.c])
        t = (self.d - self.a * punkt.x1 - self.b * punkt.x2 -self.c * punkt.x3 ) / (self.a ** 2 + self.b ** 2 + self.c ** 2)
        F = Punkt(lot_g.s[0] + lot_g.r[0] * t,lot_g.s[1] + lot_g.r[1] * t, lot_g.s[2] + lot_g.r[2] * t)
        return punkt.d_punkt_to_punkt(F)

class Gerade(object):
    def __init__(self,s, r):
        self.s = s
        self.r = r
    def d_gerade_punkt(self, punkt):
        t = (self.r[0] * (punkt.x1 - self.s[0]) + self.r[1] * (punkt.x2 - self.s[1]) + self.r[2] * (punkt.x3 - self.s[2])) / (self.r[0] ** 2 + self.r[1] ** 2 + self.r[2] ** 2)
        fuspunk = Punkt(self.s[0] + t * self.r[0], self.s[1] + t * self.r[1], self.s[2] + t * self.r[2])
        return fuspunk.d_punkt_to_punkt(punkt)


g1 = Gerade([4, 3, 3], [2, 1, -1])
p1 = Punkt(-2, -6, 2)
print(g1.d_gerade_punkt(p1))

