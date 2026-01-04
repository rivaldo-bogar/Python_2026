class Mobil():
    roda = 4
    def __init__(self,warna,name):
        self.warna = warna
        self.name = name

car1 = Mobil("black","Vim")
car2 = Mobil("red","Bim")
print(car1.name,car1.warna) # akses method property
print(Mobil.roda) # akses class property dengan name class
print(car1.roda) # akses class property dengan object
Mobil.roda = Mobil.roda + 8 # mengganti semua aturan roda,karena di ganti di class.
print(Mobil.roda, ' new production ')

del car1.warna # Hapus property / berlaku untuk obj itu saja,property pada object itu
print(car2.warna) # saya coba panggil,dan bisa
# print(car1.warna) # jika saya coba panggil akan error


# Hapus warna dari mobil → mobil itu bingung
# Hapus aturan pabrik → semua mobil terdampak