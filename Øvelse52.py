#Skriv et program der ganger hver tal i liste med 4.
#Skriv et program, der adderer 6 til hver tal i listen
#Skriv et program, der kvadrerer alle tallene i en liste
#Skriv et program, der laver alle bogstaver til versaler i en streng
#Givet to lister. Find ud af hvor mange forskellige elementer de to lister har.
#Skriv et program der tager kvadratroden af de første fibonacci tal og viser denne liste.
#Skriv et program, der summer en liste af tal
#Skriv et program, der returnerer alle de tal som er lige i en liste af hele tal.
#Skriv et program, der tager to lister af tal hvor tallene i den ene liste opløftes i tallene i den anden.
#Skriv et program, der generer listen af de første n primtal.


def multiply_by_4(lst):
    return [num * 4 for num in lst]


def add_6(lst):
    return [num + 6 for num in lst]


def square_list(lst):
    return [num ** 2 for num in lst]

def make_uppercase(string):
    return string.upper()


def count_unique_elements(lst1, lst2):
    return len(set(lst1 + lst2))


from math import sqrt

def fibonacci_squares(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return [sqrt(num) for num in fib[:n]]


def sum_list(lst):
    return sum(lst)


def even_numbers(lst):
    return [num for num in lst if num % 2 == 0]


def power_lists(lst1, lst2):
    return [num1 ** num2 for num1, num2 in zip(lst1, lst2)]


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def first_n_primes(n):
    primes = []
    i = 2
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes










