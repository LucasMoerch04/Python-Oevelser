#Skriv et program der konstruerer 3 tekst variabler, som rummer teksterne “Der var engang”, “ en mand som” og “boede i en spand. Spanden var af ler”.

first = "Der var engang"
second = " en mand som"
third = " boede i en spand. Spanden var af ler"

#Printer sammenkædning
print(first + second + third)

#Printer længder af sætninger
print("Længden af første sætning:", len(first))
print("længden af anden sætning:", len(second))
print("længden af trejde sætning:" , len(third))

#Gør så den ikke tæller mellemrum som bogstaver
def andet_bogstav():
    first_um = first.replace(" ","")
    second_um = second.replace(" ","")
    third_um = third.replace(" ","")
    
    #Printer andet bogstav i hver sætning
    print("Andet bogstav i først sætning:", first_um[1])
    print("Andet bogstav i anden sætning:", second_um[1])
    print("Andet bogstav i tredje sætning:", third_um[1])

andet_bogstav()

#Fortæller om to af sætningerne er ens
if first == second or first == third or second == third:
    print("To af sætningerne er ens")
else:
    print("Ingen af sætningerne er ens")
    
#Printer den sammenhængende sætning i versaler
print(first.upper(), second.upper(), third.upper())
   
#Laver første sætningen om til en delstreng 
print(first[0:7])

#Fjerner mellemrum og printer første bogstav i første sætninge, anden bogstav i anden sætning osv.
def mix():
    first_um = first.replace(" ","")
    second_um = second.replace(" ","")
    third_um = third.replace(" ","")

    done = first_um[0] + second_um[1] + third_um[2]
    print(done)
    
mix()

combined = first + second + third
print("Bogstavet 'e' forekommer:", combined.count("e"), "gange")
