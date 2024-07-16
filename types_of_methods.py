class student:
    school = "riddhi"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def avg(self): # instance method: used to work with instance variables and we use self key word
        return (self.m1+self.m2+self.m3)/3 
    
    def get_m1(self): # accessor method
        print(self.m1)
        
    def set_m1(self,value): # mutator method
        self.m1 = value
    
    @classmethod #we use decorator for class methods
    def get_school_name(cls): #class method: works with class variables and uses cls keyword
        return cls.school
    
    @staticmethod # decorator for static method
    def info(): # no keywords like self,cls are used as it is not used to work with instance or class variables
        print("this is student class")
    
s1 = student(42,37,35)
s2 = student(41,41,28)
s1.get_m1()
s2.get_m1()
s1.set_m1(24)
s1.get_m1()
print(student.get_school_name())
student.info()
