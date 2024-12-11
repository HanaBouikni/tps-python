from dataclasses import dataclass

@dataclass
class Ville:
    name:str
    population:int

villes=[]

while True:
    Ville_name=str(input("input the name of citys: "))

    if(Ville_name=='stop'):
        break
    city=Ville(name= Ville_name ,population=len(Ville_name)*1000000)
    villes.append(city)

villes.sort(key=lambda city: city.population, reverse=True)

for city in villes:
    print(city)

