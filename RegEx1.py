import re
show = re.findall("a..c", "allc a-c aXc")
# ['abc', 'a-c', 'aXc']
print(show)

# Maksud dari code ini, menggunakan a.c artinya '.' --> apapun di antara huruf awal a dan akhir c akan di ambil,dalam artian 1 huruf, karena . = 1