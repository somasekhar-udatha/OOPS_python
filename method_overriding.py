class A:
    def show(self):
        print("in A")
class B(A):
    def show(self):
        print("in B")
a = A()
b = B()

a.show()
b.show()
