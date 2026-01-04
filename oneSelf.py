class Latihan():
    def __init__(myObject,name): # nama self bisa diganti,tapi tidak disarankan..(chatGPT dan gemini,karena akan membingungkan bagi developer lain.)
        myObject.name = name
    def show_text(named):
        print(f'Hello my name is {named.name}')

obj1 = Latihan("valdo")
obj1.show_text()
# jadi self itu berada di method dalam class,jika hanya method saja,dan ada parameter awal,itu bukan self,melainkan parameter.
    
#self itu merujuk pada obj itu sendiri,dalam artian self = saya
#self.melihat() = saya.melihat()