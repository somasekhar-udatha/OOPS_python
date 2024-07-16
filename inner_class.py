class student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll 
        #creating object of inner class in outer class 
        self.lap = self.laptop()
        
    def show(self):
        print(self.name,self.roll)
        self.lap.show()
        
    class laptop:
        def __init__(self):
            self.brand = "HP"
            self.ram = 8 
        
        def show(self):
            print(self.brand,self.ram)

s1 = student("soma",63)
s2 = student("sekhar",36)
#s1.show()
#creating object of inner class 
lap = student.laptop()
s1.show()
