#create a class 2d vector and use it to create another class 3d vector

class C2dVec :
    def __init__(self , i , j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class C3dVec(C2dVec):
    def __init__(self , i , j , k):
        super().__init__(i,j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
        
v2d = C2dVec(1,3)
v3d = C3dVec(1,4,9)
print(v2d)
print(v3d)
    