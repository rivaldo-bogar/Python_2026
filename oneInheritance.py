# Modifying Class Properties (Perangkap Umum ⚠)
class Game():
    jumlah_player = 5
    def __init__(self,nama,id,ranking):
        self.nama = nama
        self.id = id
        self.ranking = ranking

    def __str__(self):
        return f'{self.nama}\n{self.id}\n{self.ranking}\n'
    
class puzzel(Game): # inheritance,jadi property dan atribute semua di class Game,diwarikan ke class puzzel.
    pass
player1 = Game("Valdovip",456,"Platinum")
player2 = puzzel("Puzzel_valdovip",456,"puzzel.Platinum")

print(player1)
print('Dengan class berbeda/Inheritance : ',player2)