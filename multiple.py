class Parent1:
    a = 10

    def __init__(self,p):
        self.p = p

    def dis_p1(self):
        print('i am parent1')
        print(f'a:{Parent1.a},p:{self.p}')

class Parent2:
    b = 20

    def __init__(self,q):
        self.q = q

    def dis_p2(self):
        print('i am parent2')
        print(f'b:{Parent2.b},q:{self.q}')

class Parent3:
    c = 30

    def __init__(self,r):
        self.r = r

    def dis_p3(self):
        print("i am parent3") 
        print(f"c:{Parent3.c},r:{self.r}")

class Child(Parent3,Parent2,Parent1):
    d = 50

    def __init__(self,p,q,r,s):
        super().__init__(r)
        Parent1.__init__(self,p)   
        Parent2.__init__(self,q)  
        self.s = s

    def dis_c(self):
        super().dis_p3()
        self.dis_p2()
        self.dis_p1()
        print('i am child')
        print(f'd:{Child.d},s:{self.s}')     

obj = Child('P1','P2','P3','C')
obj.dis_c()                         