class A:
    def display(self):
        print("dispaly from A class")

class B(A):
    def display(self):
        print("dispaly from B class")

class C:
    def show(self):
        print("I am C class")

class D(B,C):
    super.__init__()
    def display(self):
        print("I am Hybird class name D")

d1 = D()
A.display(self=D)
d1.display()
print(D.mro())