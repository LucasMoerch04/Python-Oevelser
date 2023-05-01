
#Skriv et program, der sorterer en liste af tal vha. bubblesort-algoritmen.
#Skriv et program, der sorterer en liste af tal vha. mergesort-algoritmen.
#Afprøv dine sorteringsalgoritmer på lister med mange tusinde tal. Hvilken en af algoritmerne er mon hurtigst?


def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


import random
import time

# Generer en tilfældig liste af 10000 tal
lst = [random.randint(1, 100) for _ in range(10000)]

# Mål tid for bubblesort
start_time = time.time()
bubble_sort(lst)
end_time = time.time()
print("Tid for bubblesort:", end_time - start_time, "sekunder")

# Mål tid for mergesort
start_time = time.time()
merge_sort(lst)
end_time = time.time()
print("Tid for mergesort:", end_time - start_time, "sekunder")