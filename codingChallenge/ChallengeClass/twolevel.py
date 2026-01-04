class Car():
    def __init__(self,brand):
        self.brand = brand
        self.speed = 0

    def accelerate(self):
        self.speed += 10
    
    def show_speed(self):
        return self.speed
mobil = Car("")
mobil.accelerate()
mobil.accelerate()
print(f'Kecepatan mobil saat ini : {mobil.show_speed()}')
