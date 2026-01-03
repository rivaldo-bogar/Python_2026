
import re

cek = re.findall("\d{2,4}", "123 12 12345 13 14 16334")
print(f"{cek} dengan type: {type(cek)}") # ingat regEx menghasilkan List datatype

# gunanya mencari jumlah charcter atau nilai, \d = digit {minimum,maksimal}---> minimal ambil 2 digit dan maximal 4 digit dari setiap kata (yang ada space)
