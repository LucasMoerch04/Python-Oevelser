#Undersøg om en given tekststreng (string variable) udgør et validt CPR-NR. Bemærk valid betyder bare, at den overholder dag, måned og år format samt at alle 10 tegn er tal.

#Bruger indtaster cpr-nr
cpr = input("Angiv CPR-NR:")

#Gør så CPR-NR kan være både med og uden bindestreg
cpr.split
cpr = cpr.replace("-","")


#Opdeler
dd = cpr[0:2]
mm = cpr[2:4]
yy = cpr[4:6]
end = cpr[6:10]


#Konvertere lists til strings
dd = [str(int) for int in dd]
dd_string = "".join(dd)

mm = [str(int) for int in mm]
mm_string = "".join(mm)

yy = [str(int) for int in yy]
yy_string = "".join(yy)

end = [str(int) for int in end]
end_string = "".join(end)


#Printer Succes hvis alle faktorer er valide
if int(dd_string) < 32 and int(mm_string) < 13 and int(yy_string) < 100 and int(end_string) < 10000 and cpr.isnumeric():
    print("SUCCES - CPR-NR er validt")
else:
    print("FEJL - CPR er ikke validt")

