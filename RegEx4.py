import re

try:
    lowtext = "my name knme neee kldme nkke abtie ne nbbbbe nne nbbe"
    mytext = """The blaze at Le Constellation in Crans-Montana on New Year's Eve injured 119 other people, officials have said. With many of the injured identified, families now face an agonising wait for information about those still missing."""
    show = re.findall("nb+e",lowtext) # b+ artinya = character b harus minimal ada 1
    print(f"{show}")

except: 
    print("Sepertinya ada yang error..")
