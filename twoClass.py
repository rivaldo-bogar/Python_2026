class Player():
    def __init__(self,name,id):
        self.name = name
        self.id = id
        pass

p1 = Player("Valdo",423)
p2 = Player("Bogar",123)
print(f'Name : {p1.name}\nId : {p1.id}\n')
print(f'Name : {p2.name}\nId : {p2.id}\n')