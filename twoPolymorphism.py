class Arena_hacking:
   
    def speak(self):
        return "Blackhat"
class Arena_Learning:
   
    def speak(self):
        return "White Hacker"
 
obj = [Arena_hacking(),Arena_Learning()]

for object in obj:
    print(f'{object.speak()}')