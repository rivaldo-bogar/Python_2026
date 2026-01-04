import os

class ValEditor:
    def __init__(self,file_name):
        file_name = str(input("masuka file name : "))
        self.file_name = file_name
        pass
    def processing_make(self):
        try:
            with open(self.file_name,"x") as Document:
                Document.write("Hello valdo")
        except FileExistsError:
            print("Nama file itu sudah ada..")
    def processing_append(self,input_tambahan):
        input_tambahan = str(input("tambah apa : "))
        self.tambah = input_tambahan
        with open(self.file_name,"a") as Document:
                Document.write(f"{self.tambah}\n")
    def processing_reading(self):
         with open(self.file_name,"r") as Document:
               print(Document.read())
user1 = ValEditor('')

Membuka_app = True
while Membuka_app == True :
    menu = str(input("(tulis,buat,tambah,baca) : "))
    menu = menu.lower()
    if menu == "buat":
        user1.processing_make()
    elif menu == "tambah":
        user1.processing_append('')
    elif menu == "baca":
        user1.processing_reading()

    else:
        print("Belum tersedia...masih pengembangan")
    
    Membuka_app = str(input("lagi??\t"))
    Membuka_app = Membuka_app.lower()
    if Membuka_app == 'iya':
        Membuka_app = True
    else:
        Membuka_app = False
print(f'terima kasih..byee')