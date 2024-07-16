class cars:
    wheels = 4
    def __init__(self):
        self.name = "BMW"
        self.mil = 10 

c1 = cars()
c2 = cars()
c1.mil = 8
print(c1.name,c1.mil,c1.wheels)
print(c1.name,c1.mil,cars.wheels)
cars.wheels = 5
print(c1.name,c1.mil,c1.wheels)
print(c1.name,c1.mil,cars.wheels)
