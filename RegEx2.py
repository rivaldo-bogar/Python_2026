import re

try:
    mytext = """The blaze at Le Constellation in Crans-Montana on New Year's Eve injured 119 other people, officials have said. With many of the injured identified, families now face an agonising wait for information about those still missing."""
    show = re.findall("^The",mytext)
    show_endtext = re.findall("missing.$",mytext)
    print(f"{show_endtext}")

except: 
    print("Sepertinya ada yang error..")

# arti RegEx = ^ ----> harus berawal dari itu,jadi text diawal kata The kalau bukan itu,tidak ditemukan (sesuai variabel/data)
# arti RegEx = $ ----> harus di akhiri dengan kata itu,jadi kalau ada sebuah variabel,akhirannya harus $missing. (sesuai variabel/data)