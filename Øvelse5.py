#Lav en Basal Metabolic Rate (BMR) beregner, der fortæller hvor meget energi du forbrænder i hviletilstand i løbet af en dag (kalorier). Input er hvorvidt du er mand eller kvinder samt vægt (kg), alder (år), højde (cm) og aktivitetsniveau
#Lader brugeren indputte variablerne
køn = input("Er du mand eller kvinde:")
mand = "mand"
kvinde = "kvinde"
vægt = input("Hvor mange kg vejer du:")
alder = input("Hvor mange år er du:")
højde = input("Hvor høj er du i cm:")

print("Foretager du lidt til ingen motion, tast 1")
print("Foretager du rolig motion 1-3 gange om ugen, tast 2")
print("Foretager du moderat motion 3-5 gange om ugen, tast 3")
print("Foretager du intens motion 6-7 gange om ugen, tast 4")
print("Foretager du meget intens motion, samt et fysik job, tast 5")
aktivitetsniveau = input("Tast 1-5 afhænig af dit motionsniveau:")

#Beregner BMR afhænig af indtastet køn
if køn == mand:
    BMR = (10 * int(vægt)) + (6.25 * int(højde)) - (5 * int(alder)) + 5
else:
    BMR = (10 * int(vægt)) + (6.25 * int(højde)) - (5 * int(alder)) - 161
    
#Beregner kalorieforbrænding afhængig af aktivitetsniveau
if aktivitetsniveau == str(1):
    print("Du forbrænder i hviletilstand hver dag", BMR * 1.2, "kalorier")
elif aktivitetsniveau == str(2):
    print("Du forbrænder i hviletilstand hver dag", BMR * 1.375, "kalorier")
elif aktivitetsniveau == str(3):
    print("Du forbrænder i hviletilstand hver dag", BMR * 1.55, "kalorier")
elif aktivitetsniveau == str(4):
    print("Du forbrænder i hviletilstand hver dag", BMR * 1.725, "kalorier")
elif aktivitetsniveau == str(5):
    print("Du forbrænder i hviletilstand hver dag", BMR * 1.9, "kalorier")
else:
   print("Error")
   
#En Big Mac rummer ca 500 kalorier. Lav en omregner, der regner i Bic Macs
#Beregner antallet af Big Macs forbrændt afhængig af aktivitetsniveau
if aktivitetsniveau == str(1):
    print("Det svarer til", BMR * 1.2 / 500, "Big Macs")
elif aktivitetsniveau == str(2):
    print("Det svarer til", BMR * 1.375 / 500, "Big Macs")
elif aktivitetsniveau == str(3):
    print("Det svarer til", BMR * 1.55 / 500, "Big Macs")
elif aktivitetsniveau == str(4):
    print("Det svarer til", BMR * 1.725 / 500, "Big Macs")
elif aktivitetsniveau == str(5):
    print("Det svarer til", BMR * 1.9 / 500, "Big Macs")
else:
   print("Error")