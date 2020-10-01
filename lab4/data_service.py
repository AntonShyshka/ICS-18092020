from dataclasses import dataclass

code = [103, 104, 105, 106, 109, 111]
name = ["1 англійський фунт стерлінг", "10 бельгійських франків", "1 німецька марка", "1 голандський гульден", "1 канадський доллар", "1 доллар США"]

@dataclass
class dovidnik:
   code:int
   name:str
   year:int


data_array = [dovidnik(103, "1 англійський фунт стерлінг"), dovidnik(104,"10 бельгійських франків"), dovidnik(105,"1 німецька марка"), dovidnik(106, "1 голандський гульден"), dovidnik(109,"1 канадський долар"), dovidnik(111,"1 доллар США")]

def printdovidnik(dovidnik):
    print("Код валюти: {code}, Найменування валюти: {name}, Рік: {year}" .format(code = dovidnik.code, name = dovidnik.name, year = dovidnik.name))

for data in data_array:
    printdovidnik(data)
