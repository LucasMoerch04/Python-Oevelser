#Lav et tekstbaseret “Hang-man” spil

life_counter = 0
counter = 0
answer = "Football"
line = []
word = str(answer.lower())

for i in word:
    line.append("_")
print(" ".join(line))

choice = input("Choose a letter: ")


def guess(choice):
    
    if choice in word:
        print("Correct")
        wordtemp = word.replace(choice,"")
        print(wordtemp)
        choice = input("Choose a letter: ").lower()
        guess(choice)
    else:
        print("Wrong! Try again")   
        guess(choice) 
    
        
    if not str(wordtemp):
        print("You guessed it! The word is " + answer)

guess(choice)