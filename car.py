class car:
    def __init__(self,model,color):
        self.model = model
        self.color = color
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount

    def brake(self,amount):
        self.speed -= amount

    def get_speed(self):
        print(self.speed)

a = car('똥차','갈색')
a.accelerate(100)
a.brake(50)
a.get_speed()