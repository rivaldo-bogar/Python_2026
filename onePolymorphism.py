class Game:
    
    def __init__(self,nama):
        self.nama = nama
    #@saticmethod # dipakai kalau pada operasikan rumus,yang tidak berkaitan dengan pemanggilan data dari obj itu sendiri,yang ada di __init__.ibratnya,calculator umum,tanpa tau nama data kita.
    def train_polymorphism(self): # rekomendasi 90% gemini,pakai self
        #ini contoh function polymorphism,function yang sama tapi dengan perilaku berbeda : hitung string,hitung jumlah list,hitung set.
        data1 = len("Rivaldo") # str
        data2 = len([2,3,4]) # List
        data3 = len({4,2,2}) # Set
        # user_input = input(str("Input data number : "))
        print(f'\n yang ditampilkan = {data2}')
obj = Game("test")

obj.train_polymorphism()