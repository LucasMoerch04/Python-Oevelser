#LIX-beregner

text = "Musa is a hoe. Han er dog samtidig en flink mand."

#Finder antallet af ord
ord = text.split()
O = len(ord)


#finder antallet af punktummer
P = text.count(".")


#Finder antal ord over 6 bogstaver
L = 0

for i in ord:
    letters = len(i)
    if len(i) >= 6:
      L += 1 

#Printer LIX-tal
print(O/P + L * 100 / O)

