#Skriv et program, der finder alle de store bogstaver og små bogstaver i en streng.

string = "Hej, jeg hedder Lucas. Hvad hedder du?"
string2 = "Det ved jeg faktisk ikke."
i_string = "Ingen i verden kender ikke Messi."


def uppercase_string(string):
    uppercase = []
    for i in range(len(string)):
        if string[i].isupper():
            uppercase.append(string[i])
    print("Store bogtstaver:", uppercase)
uppercase_string(string)    

def lowercase_string(string):
    lowercase = []
    for i in range(len(string)):
        if string[i].islower():
            lowercase.append(string[i])
    print("Små bogstaver:", lowercase)
lowercase_string(string)

#Skriv et program, der finder alle mellemrum
def space_string(string):
    space = 0
    for i in range(len(string)):
        if string[i] == " ":
            space += 1
    print("Antal mellemrum:", space)
space_string(string)

#Skriv et program, der undersøger hvor mange forskellige bogstaver to strenge har.
def forskellige_bogstaver(string,string2):
    bogstav = []
    for i in range(len(string)):
        if string[i] not in bogstav and string[i].isalpha():
            bogstav.append(string[i])
    for i in range(len(string2)):
        if string2[i] not in bogstav and string2[i].isalpha():
            bogstav.append(string2[i])
    print("De forskellige bogstaver:", bogstav)
forskellige_bogstaver(string,string2)

#Skriv et program, der erstatter alle bogstaver “i” med “k” i en streng.
def erstat_string(string):
    for i in range(len(string)):
        if string[i] == "i":
            string.replace("i","k")