#Denne opgave træner dig i simpel brug af lister. Prøv at undgå at bruge eksisterende funktioner.
#Byt om på rækkefølgen i en liste. Så sidste element er det første.
#Sammenkæd to lister.
#Givet en liste af tal returner de kvadreret tal.
#Sammenkæd to lister af strenge, så første element i den første liste og første element i den anden liste konkatineres/sættes sammmen så de er første element i den nye liste.
#Givet to lister af tal og af samme længde. Iterer over dem, så første element i den ene liste og første element i den anden printes på samme linje osv.
#Fjern tomme strenge i en liste af strenge.
#Givet en liste med flere værdier af 20. Find dem men kun erstat den sidste med 200.


def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

def concatenate_lists(lst1, lst2):
    concatenated_lst = lst1 + lst2
    return concatenated_lst

def square_numbers(lst):
    squared_lst = []
    for num in lst:
        squared_lst.append(num**2)
    return squared_lst

def concatenate_strings(lst1, lst2):
    concatenated_lst = [lst1[0] + lst2[0]]
    return concatenated_lst

def iterate_lists(lst1, lst2):
    for i in range(len(lst1)):
        print(lst1[i], lst2[i])

def remove_empty_strings(lst):
    cleaned_lst = []
    for string in lst:
        if string != "":
            cleaned_lst.append(string)
    return cleaned_lst

def replace_twenty(lst):
    for i in range(len(lst)):
        if lst[i] == 20:
            if i == len(lst) - 1:
                lst[i] = 200
    return lst

lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]
lst3 = [1, 2, 3, 4, 5]
lst4 = ["hej", "med", "dig"]
lst5 = [10, 20, 30, 40, 50]
lst6 = ["", "hej", "", "med", "", "dig"]
lst7 = [20, 20, 20, 200, 20]

print(reverse_list(lst1)) # output: [5, 4, 3, 2, 1]
print(concatenate_lists(lst1, lst2)) # output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(square_numbers(lst3)) # output: [1, 4, 9, 16, 25]
print(concatenate_strings(lst4, lst4)) # output: ["hejhej"]
iterate_lists(lst1, lst2) # output: 1 6, 2 7, 3 8, 4 9, 5 10
print(remove_empty_strings(lst6)) # output: ["hej", "med", "dig"]
print
