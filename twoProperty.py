# Modifying Class Properties (Perangkap Umum ⚠)
class Game():
    jumlah_player = 5
    def __init__(self,nama,id,ranking):
        self.nama = nama
        self.id = id
        self.ranking = ranking

    def info_player(self):
        print(f'{self.nama}\n{self.id}\n{self.ranking}\n')

player1 = Game("Valdovip",456,"Platinum")
player2 = Game("Vargar",426,"Premium")

print(player1.info_player())
# Modify property class
player1.jumlah_player = 10 # anehhh,tidak,hanya berlaku ke obj itu sendiri,tidak direcomendasi dari gemini
print(player1.jumlah_player)
Game.jumlah_player = 15 # cara yang benar untuk ganti class property
print(player1.jumlah_player)

# bisa juga kita tambahkan property baru di class agar bisa dipakai oleh semua object.contoh dibawah ini
Game.agePlayer = 18
print(Game.agePlayer)
print('object : ',player1.agePlayer)
