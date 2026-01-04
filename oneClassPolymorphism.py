class vehicle:
    def running(self):
        print('kendaraan bergerak')
class boat(vehicle):# inheritance/pewarisan
    def running(self):# class polymorphism
        print('speeboat segera berangkat')
class motor(vehicle):# inheritance/pewarisan
    def running(self): # class polymorphism
        print('motor gass..')

obj = [vehicle(),boat(),motor()]
vehicle = [boat(),motor()] # bisa juga seperti ini.
for x in obj:
    x.running()