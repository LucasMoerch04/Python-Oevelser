#Herunder nogle simple opgaver om brugen af strenge. Lav så mange du kan nå. Det er god træning og prøv at undgå at bruge prædefinerede metoder.
#Skriv en funktion der beregner længden af en streng.
#Skriv en funktion der beregner antallet af karakterer i en streng.
#Skriv en funktion der tager en sætning i form af en streng og splitter den op, så du får en liste af ord.
#Skriv en funktion, der kan indsætte et bogstav på et bestemt index og returnere den nye streng.
#Skriv en funktion, der tager en liste af strenge og finder den længste.
#Skriv en funktion, der fjerner det i'te element i en ikke tom streng.
#Skriv to funktioner. En der krypterer en streng og en anden der dekrypterer. Du bestemmer selv krypteringsmetoden. Den må gerne være meget simpel.


def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count

def count_chars(s):
    count = 0
    for char in s:
        count += 1
    return count

def split_sentence(s):
    words = []
    current_word = ""
    for char in s:
        if char == " ":
            words.append(current_word)
            current_word = ""
        else:
            current_word += char
    words.append(current_word)
    return words

def insert_char(s, char, index):
    new_s = ""
    for i in range(len(s)):
        if i == index:
            new_s += char
        new_s += s[i]
    return new_s

def longest_string(strings):
    longest = ""
    for s in strings:
        if len(s) > len(longest):
            longest = s
    return longest

def remove_char(s, index):
    new_s = ""
    for i in range(len(s)):
        if i != index:
            new_s += s[i]
    return new_s

def encrypt(s):
    new_s = ""
    for char in s:
        new_s += chr(ord(char) + 1)
    return new_s

def decrypt(s):
    new_s = ""
    for char in s:
        new_s += chr(ord(char) - 1)
    return new_s



