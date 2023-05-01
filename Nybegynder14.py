from operator import truediv


list = [2,6,9,12,5,56,33,21,77]



def search(list, find):
    for i in range(len(list)):
        if list[i] == find:
            return True
        return False

search(list,7)
