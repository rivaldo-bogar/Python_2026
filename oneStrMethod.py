# Modifying Class Properties (Perangkap Umum ⚠)
class Game():
    jumlah_player = 5
    def __init__(self,nama,id,ranking):
        self.nama = nama
        self.id = id
        self.ranking = ranking

    def __str__(self):
        return f'{self.nama}\n{self.id}\n{self.ranking}\n'

player1 = Game("Valdovip",456,"Platinum")

print(player1)