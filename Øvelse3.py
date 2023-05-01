#Skriv et program, der generer multiplikationstabellen fra 1 til 10.

#Giver brugeren mulighed for at indtaste ønsket nummer i terminalen
tal = input("Your number:")

(count) = 0

#Printer tallet med tallene fra 1-10
while (count < 10):
    count += 1
    print(int(count) * int(tal))
    
