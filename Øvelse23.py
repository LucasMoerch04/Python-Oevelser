#Skriv et program, der på baggrund af en tekst, konstruerer en dictionary kaldt bogstav, så f.eks. bogstav[’a’] er lig med antallet af a’er i teksten, bogstav[’b’] er lig med antallet af b’er osv.

def count_letters(text):
    # Initialiser en tom dictionary
    letter_count = {}

    # Løb igennem hvert bogstav i teksten
    for letter in text:
        # Hvis bogstavet allerede er i dictionaryen, tæl én mere
        if letter in letter_count:
            letter_count[letter] += 1
        # Ellers tilføj bogstavet til dictionaryen med en startværdi på 1
        else:
            letter_count[letter] = 1

    # Returnér dictionaryen med bogstavtællingerne
    return letter_count

text = "Jeg ved ikke hvad der skal stå her"
letter_counts = count_letters(text)
print(letter_counts)