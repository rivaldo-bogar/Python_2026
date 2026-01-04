class Latihan():
    def __init__(self,answer):
        self.answer = answer
        print('run')
    def Check(self):
        if not self.answer:
            self.answer = True
            print('Self answer : ', self.answer)
        else: 
            print('Self Answer : ',self.answer)

obj = Latihan(False)
obj.Check()
obj.Check()

      