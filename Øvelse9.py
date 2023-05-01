#Skriv et program der generer et Haiku digt ud fra nogle fastsatte sætninger. Der er 17 stavelser i et Haiku digt fordelt på 5-7-5 i de tre linjer.
import random

stavelser5 = ["En solnedgang dør", "Lyden af regn falder", "Blomster i skoven"]
stavelser7 = ["Over horisonten skinner", "På et gammelt orange tag", "I en skov så dyb ser jeg"]



haiku = stavelser5[round(random.uniform(0,len(stavelser5)))]+ "\n" + stavelser7[round(random.uniform(0,len(stavelser7)))]+ "\n" + stavelser5[round(random.uniform(0,len(stavelser5)))] 

print(haiku)
