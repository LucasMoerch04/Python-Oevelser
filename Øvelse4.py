#Skriv et program, der finder det mindste hele tal n så n*n er større end 12000. 

#Sætter en variabel som jeg ved fuldender while-condition
n = 0

#Printer først når n*n er større end 1200
while (n*n < 12000):
    n += 1
    if n*n > 12000:
        print("Det mindste hele tal som gør at n*n er større end 12000 er:", n)
    

# Skriv dernæst et program, der finder det største hele tal n, så n*n*n er mindre 12000.

#Sætter en variabel som jeg ved fuldender while-condition
t = 100

#Printer først når t*t*t er mindre end 12000
while (t*t*t > 12000):
    t -= 1
    if t*t*t < 12000:
        print("Det største hele tal som gør at t*t*t er mindre end 12000 er:", t)
