#Skriv et program der bruger en dictionary til at rumme en filmdatabase. Dictionary skal rumme filmens titel, produktionsår, og instruktør samt en genre. Du afgør selv strukturen.

#Lav en funktion der afgør om en given film eksisterer i biblioteket fra forrige opgave.
#Lav en funktion der sletter en given film fra databasen
#Lav en funktion der tilføjer en ny film til databasen.
#Lav en funktion der opdaterer en egenskab ved en film. Dvs. instruktør, titel, genre eller produktionsår.

film_database = {
    "The Shawshank Redemption": {"instruktør": "Frank Darabont", "år": 1994, "genre": "Drama"},
    "The Godfather": {"instruktør": "Francis Ford Coppola", "år": 1972, "genre": "Kriminalitet"},
    "The Dark Knight": {"instruktør": "Christopher Nolan", "år": 2008, "genre": "Action"},
    "The Lord of the Rings: The Fellowship of the Ring": {"instruktør": "Peter Jackson", "år": 2001, "genre": "Fantasy"}
}


def film_findes(film_navn):
    """Tjek om en given film er i databasen"""
    return film_navn in film_database

def film_slet(film_navn):
    """Slet en given film fra databasen"""
    if film_findes(film_navn):
        del film_database[film_navn]
        print(f"{film_navn} blev slettet fra databasen.")
    else:
        print(f"{film_navn} findes ikke i databasen.")

def film_tilføj(film_navn, instruktør, år, genre):
    """Tilføj en ny film til databasen"""
    if not film_findes(film_navn):
        film_database[film_navn] = {"instruktør": instruktør, "år": år, "genre": genre}
        print(f"{film_navn} blev tilføjet til databasen.")
    else:
        print(f"{film_navn} findes allerede i databasen.")

def film_opdater(film_navn, egenskab, værdi):
    """Opdater en egenskab for en given film i databasen"""
    if film_findes(film_navn):
        film = film_database[film_navn]
        film[egenskab] = værdi
        print(f"{film_navn} blev opdateret med {egenskab}: {værdi}.")
    else:
        print(f"{film_navn} findes ikke i databasen.")
        
        
        
film_tilføj('The Godfather', 1972, 'Francis Ford Coppola', 'Drama')
film_tilføj('Star Wars', 1977, 'George Lucas', 'Sci-Fi')
film_tilføj('Jurassic Park', 1993, 'Steven Spielberg', 'Action')

print(film_findes('The Godfather'))
print(film_findes('The Matrix'))

print(film_slet('Star Wars'))
print(film_slet('The Matrix'))



film_opdater('The Godfather', 'instruktør', 'Martin Scorsese')
film_opdater('Star Wars', 'år', 1978)

print(film_database)        
