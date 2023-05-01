#Skriv en funktion, der undersøger om en given delliste af tal er indeholdt i en liste af tal. Dellisten skal optræde fra start til slut i listen. Dvs. [2,3] er en delliste af [1,2,3,4] men [1,4] er ikke.



def is_sublist(sublist, lst):
    if len(sublist) > len(lst):
        return False
    for i in range(len(lst) - len(sublist) + 1):
        if lst[i:i+len(sublist)] == sublist:
            return True
    return False


lst = [1, 2, 3, 4]
sublist1 = [2, 3]
sublist2 = [1, 4]
print(is_sublist(sublist1, lst))  
print(is_sublist(sublist2, lst))  