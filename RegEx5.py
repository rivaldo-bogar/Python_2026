import re

tampilkan = re.findall("colou?r", "color colour colouurr")
print(f"{tampilkan}")

# ibaratnya opsional,jika ada character U tampilkan,jika tidak ada lanjut R belakang