class Vector:
    def __init__(self, *components):
        self.components = components

    def leng(self): 
        return len(self.components) # returns number of components
    def dist(self):
        return sum(x**2 for x in self.components)*0.5
    def __add__(self, other):
        return Vector(*[x+y for x, y in zip(self.components, other.components)])
    def __sub__(self, other):
        return Vector(*[x-y for x, y in zip(self.components, other.components)])
    def __mul__(self, scalar):
        return Vector(*[x*scalar for x in self.components])
    def __truediv__(self, scalar):
        return Vector(*[x/scalar for x in self.components])
    def __lt__(self, other):
        return self.dist() < other.dist()
    def __eq__(self,other):
        return all(x == y for x, y in zip(self.components, other.components))
    
    def __repr__(self):
        return f"Vector{self.components}"
    
v1 = Vector(7, 8, 9)
v2 = Vector(6, 7, 8)
v3 = Vector(1, 2, 3, 4)
v4 = Vector(1, 2, 3, 4)

print(v1 + v2) # 7 + 6
print(v1 - v2) # 7 - 6
print(v1 * 4) # 7 * 4
print(v2 / 2) # 6 / 3
print(v3 == v4) # T or F

print(v1.leng()) 
print(v2.leng()) # will print number of components in Vector
print(v3.leng())
print(v4.leng())

