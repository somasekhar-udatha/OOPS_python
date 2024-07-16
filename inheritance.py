class A:
    def feature1(self):
        print("feature 1 working")
    def feature2(self):
        print("feature 2 working")
class B(A): #single inheritance
    def feature3(self):
        print("feature 3 working")
    def feature4(self):
        print("feature 4 working")
class C(B): #multi level inhertanvce
    def feature5(self):
        print("feature 5 working")
class D:
    def feature6(self):
        print("feature 6 working")
class E(A,D): #multiple inheritance
    pass
    

a1 = A()
b1 = B()

b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4() 
print()
c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
print()
e = E()
e.feature1()
e.feature2()
e.feature6()
