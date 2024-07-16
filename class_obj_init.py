class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
    
    def config(self):
        print("config is: ",self.cpu,self.ram)
a = '8'
print(type(a))
comp1 = Computer("i7",16)
comp2 = Computer("ryzen",8)
print(type(comp1))
Computer.config(comp1)
comp2.config()
