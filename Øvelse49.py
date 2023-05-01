#Lav først to lister bestående af byer og deres respektive postnumre, så de til hinanden tilhørende værdier står på de samme pladser i de respektive lister. Brug zip() og list() funktionerne til at lave en sammenkædet liste af tupler fra de to lister. Print den sammenkædet liste.
#Brug zip og dict funktioner til at lave en dictionary der har key-value fra de to lister i punkt 1.
#Brug zip, list og sorted funktioner til at lave en sorteret liste af tupler fra 1.
#Lav to lister af lister med lige mange lister i hver. Brug zip til at sammenkæde de enkelte lister i de to lister.
#Brug en for løkke, enumerate funktionen til at printe to ens-længdede lister der består af hhv. navne og aldre, så vi får : 0 navn alder, 1 navn alder, osv.
#Prøv at bruge zip på at sammenkæde mindst tre lister bestående af by, postnr og byens population.
#Overvej selv et tilfælde hvor det kan være smart at bruge zip-funktionen


byer = ["København", "Aarhus", "Odense"]
postnumre = [1000, 8000, 5000]

sammenkædet = list(zip(byer, postnumre))
print(sammenkædet)


byer = ["København", "Aarhus", "Odense"]
postnumre = [1000, 8000, 5000]

byer_dict = dict(zip(byer, postnumre))
print(byer_dict)




byer = ["København", "Aarhus", "Odense"]
postnumre = [1000, 8000, 5000]

sammenkædet = list(zip(byer, postnumre))
sammenkædet_sorted = sorted(sammenkædet)

print(sammenkædet_sorted)



liste1 = [[1, 2], [3, 4], [5, 6]]
liste2 = [["a", "b"], ["c", "d"], ["e", "f"]]

sammenkædet = list(zip(liste1, liste2))
print(sammenkædet)


navne = ["Jens", "Peter", "Mette"]
alder = [30, 40, 50]

for index, navn in enumerate(navne):
    print(index, navn, alder[index])



by = ["København", "Aarhus", "Odense"]
postnr = [1000, 8000, 5000]
befolkning = [1000000, 300000, 200000]

sammenkædet = list(zip(by, postnr, befolkning))
print(sammenkædet)


#Zip-funktionen er særligt smart, når man skal arbejde med data, der er opdelt i to eller flere lister, hvor man ønsker at sammenkæde de tilhørende værdier. Det kan eksempelvis være i forbindelse med databehandling, hvor man arbejder med store datasæt.



