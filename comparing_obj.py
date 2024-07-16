class Computer:
    def __init__(self):
        self.name = "soma"
        self.age = 20
    def compare(self,other):
        if(self.age == other.age):
            return True
        return False 

c1 = Computer()
c2 = Computer()
if(c1.compare(c2)):
    print("They are same")
else:
    print("They are diff")
c1.age = 21

if(c1.compare(c2)):
    print("They are same")
else:
    print("They are diff")
