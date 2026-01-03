import cowsay
val = None
user = input("enter what ever : ")
print(f"nilai : {val} type : {type(val)}")
print(f"{bool(None)}")
if user is not None:
    print("Nilainya tersedia")
else:
    print("Itu = None")

# Akan bertype Nonetype
def testing():
    nil = 2

nil = testing()
print(nil)

# cowsay.cow("Hello valdo")