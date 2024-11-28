class arithmetic:
    def __init__(self,a,b,c):
        self.n1=a
        self.n2=b
        self.n3=c
    def add(self):
        print(f"{self.n1}+{self.n2}+{self.n3} is={self.n1+self.n2+self.n3}")
    def sub(self):
        print(f"{self.n1}-{self.n2}-{self.n3} is={self.n1-self.n2-self.n3}")
    def mul(self):
        print(f"{self.n1}*{self.n2}*{self.n3} is={self.n1*self.n2*self.n3}")
    def div(self):
        print(f"{self.n1}/{self.n2}/{self.n3} is={self.n1/self.n2/self.n3}")
a=int(input("enter the value for a:"))
b=int(input("enter the value for b:"))
c=int(input("enter the value for c:"))
arith=arithmetic(a,b,c)
arith.add()
arith.sub()
arith.mul()
arith.div()
