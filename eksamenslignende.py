#1.	JavaScript-funktioner er kodestrukture, der kan tage input i form af parametre, udføre en opgave og returnere en værdi. Funktioner kan defineres på forskellige måder, og en funktion kan tage et vilkårligt antal parametre og returnere en værdi af enhver type.


#2.	Koden definerer tre funktioner: setup(), draw(), og drawTarget(xloc, yloc, size, num).
#setup() funktionen definerer et canvas med størrelsen 720 x 400, sætter baggrunden til en mørk farve, og slår stroke og loop fra.
#draw() funktionen kalder tre gange drawTarget() funktionen, med forskellige koordinater og størrelser som input.
#drawTarget(xloc, yloc, size, num) funktionen tegner en skive, der repræsenterer en skydeskive, på canvas ved at tegne flere cirkler med gradvist mindre størrelser og forskellige farver. Funktionen tager fire parametre som input: xloc og yloc angiver positionen for midtpunktet af skiven, size angiver diameteren på den største cirkel i skiven, og num angiver antallet af cirkler i skiven.
#Variablen grayvalues beregner mængden af gråfarvevariation, der kræves for hvert trin i skydeskiven, og variablen steps beregner størrelsen af hver cirkel i skiven. Derefter bruges en for-løkke til at tegne cirklerne ved hjælp af fill() og ellipse() funktionerne, hvor farven på cirklen ændres gradvist i gråtoner i hver iteration af loopet. Resultatet er tre skydeskiver med forskellig størrelse, antal af cirkler og farveskala, der bliver tegnet på canvas.

#3. 

def print_numbers(is_even = False, n=10):
    numbers = []
    if is_even:
        numbers = [x for x in range(0, n+1, 2)]
    else:
        numbers = [x for x in range(1, n+1, 2)]
    print(" ".join(str(x) for x in numbers))

# Test af funktionen
print_numbers(True, 20) # udskriver 0 2 4 6 8 10
print_numbers(False, 15) # udskriver 1 3 5 7 9
print_numbers() # udskriver 1 3 5 7 9 (standardværdi for n er 10)


#4. 


import random
import turtle



def draw_random_circles():
    n=input("Skriv et naturligt tal: ")
    turtle.Screen()
    turtle.speed('fastest')
    for i in range(int(n)):
        # Vælg en tilfældig radius mellem 10 og 100 pixels
        radius = random.randint(10, 100)
        # Vælg tilfældige x- og y-koordinater indenfor skærmens grænser
        x = random.randint(-turtle.window_width()//2, turtle.window_width()//2)
        y = random.randint(-turtle.window_height()//2, turtle.window_height()//2)
        # Tegn cirklen med den valgte radius og position
        turtle.penup()
        turtle.goto(x, y-radius)
        turtle.pendown()
        turtle.circle(radius)
        #turtle.hideturtle()

# Test af funktionen
draw_random_circles()

turtle.done()



