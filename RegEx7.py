import re

import re

try:
    lowtext = "my name knme neee kldme nkke abtie nbbe"
    mytext = """The blaze at Le Constellation in Crans-Montana on New Year's Eve injured 119 other people, officials have said. With many of the injured identified, families now face an agonising wait for information about those still missing."""
    show = re.findall("[ank]",lowtext)
    print(f"{show}")

except: 
    print("Sepertinya ada yang error..")

# RegEx = [ank] ---> mencari pilihan karakter [ank] setiap kata ada gak huruf ank,dibaca dari kiri ke kanan, jika dari 3 chracter itu ada muncul di awal,tampilkan terlebih dahulu.