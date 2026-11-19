class Grand:
    a = 10

    def __init__(self,p):
        self.p = p

    def dis_G(self):
        print(f"a:{Grand.a},p:{self.p}")

class Parent(Grand):
    b = 20

    def __init__(self, p,q):
        super().__init__(p)  
        self.q = q

    def dis_P(self):
        super().dis_G()
        print(f"b:{Parent.b},q:{self.q}")

class Child(Parent):
    c = 30

    def __init__(self, p, q,r):
        super().__init__(p, q)
        self.r = r
    
    def dis_C(self):
        super().dis_P()
        print(f"c:{Child.c},r:{self.r}") 

    # def change(self,new_r):
    #     self.r = new_r    

    # def update(self,new_c):
    #     Child.c = new_c

obj = Child("Grand","Parent","Child")
