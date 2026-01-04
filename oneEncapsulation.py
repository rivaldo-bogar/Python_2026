class MyBank:
    def __init__(self,nama):
      self.__saldo = 0
      self.nama = nama
    @property
    def transaksi(self):
       return self.__saldo

    @transaksi.setter
    def transaksi(self,input_userNominal):   
        if input_userNominal > 0:
              self.__saldo += input_userNominal
              print(f"deposit anda sukses sebanyak {input_userNominal}")
        else:
               print("Maaf masukan nominal dengan benar")

   
       
user1 = MyBank('valdo')

try:   
    input_user = int(input("masukan jumlah saldo : "))
    user1.transaksi = input_user
    print(f"Hello {user1.nama} saldo anda sekarang : {user1.transaksi}")
except ValueError:
    print("!!Harap memasukan angka..")

