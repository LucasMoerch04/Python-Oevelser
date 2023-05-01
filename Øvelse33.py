import random

#1. function finds biggest number of three arguments
def biggestnumber(a,b,c):
    numbers = [a,b,c]
    biggest_number = max(numbers)
    print("The biggest number of the three is", biggest_number)

biggestnumber(27,49,78)

#2. function sums all numbers given
def sumaftal(*tal):
    tal = [*tal]
    Sum = sum(tal)
    print("The sum of the given numbers are", Sum)
    
sumaftal(5,7,5,8,100,7,)
    
#3. function shuffles the list in random order
def listorder(*numbers):
    listofnumbers = [*numbers]
    random.shuffle(listofnumbers)
    print("The list in a random order", listofnumbers)
    
listorder(6,9,1,7,4)
    
#4. function tells if given number is in given interval
def numinterval(number,lownumber, highnumber):
    if number > lownumber and number < highnumber:
        print(f"{number} er inde for det givne interval")
    else:
        print(number,"er ikke inde for det givne interval")
    
numinterval(10,5,15)
    

    
   