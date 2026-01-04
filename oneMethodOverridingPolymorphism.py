class Fps:
    def __init__(self,nama_player,id):
        self.nama_player = nama_player
        self.id = id
    def press_space():
        print(f"action ---> Loncat")
class Strategi(Fps): # inheritance dari Fps / attribute diturunkan
    def press_space():
        print(f"action ---> pause")
class Rpg(Fps):# inheritance dari Fps / attribute diturunkan
    def press_space():
        print(f"action ---> particel effect")

playerFps1 = Fps("fc",123)
playerStrategi1 = Fps("duck",12243)
playerrpg1 = Fps("king",1223)

for x in(playerFps1,playerStrategi1,playerrpg1): 
    # pada bagian ini terjadi,polymorphism,dimana semua obj memanggil nama fungsi yang sama yaitu press.space,dengan perilau berbeda berbeda.
    print('\n')
    print(x.nama_player)
    print(x.id)
    x.press_space