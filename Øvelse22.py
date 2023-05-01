#Gennemløb løn og udskriv navn og løn for hver person på en linje for sig.
#Undersøg om "Bente"findes i løn.
#Hent og udskriv kun nøgler af løn.
#Hent og udskriv kun værdierne af løn.
#Bestem gennemsnitslønnen.
#Bestem den hyppigst forekomne lønindkomst.
#Bestem mindste- og størstelønnen i løn.
#Undersøg programmatisk om der findes flere personer med samme løn.

# Opgave 1
lon = {'Niels': 85000, 'Peter': 40000, 'Jakob': 90000, 'Poul': 100000, 'Dorte': 40000}
for name, salary in lon.items():
    print(f"{name}: {salary}")

# Opgave 2
if 'Bente' in lon:
    print("Bente er med i løn.")
else:
    print("Bente er ikke med i løn.")

# Opgave 3
print(lon.keys())

# Opgave 4
print(lon.values())

# Opgave 5
average_salary = sum(lon.values()) / len(lon)
print(f"Gennemsnitslønnen er: {average_salary:.2f}")


# Opgave 6 
salary_counts = {}
for salary in lon.values():
    if salary in salary_counts:
        salary_counts[salary] += 1
    else:
        salary_counts[salary] = 1

most_common_salary = None
most_common_salary_count = 0
for salary, count in salary_counts.items():
    if count > most_common_salary_count:
        most_common_salary = salary
        most_common_salary_count = count

print(f"Den hyppigst forekomne lønindkomst er: {most_common_salary}")

# Opgave 7
min_salary = min(lon.values())
max_salary = max(lon.values())
print(f"Mindste løn er: {min_salary}")
print(f"Største løn er: {max_salary}")

# Opgave 8
salary_counts = {}
for salary in lon.values():
    if salary in salary_counts:
        salary_counts[salary] += 1
    else:
        salary_counts[salary] = 1

multiple_salaries_exist = False
for count in salary_counts.values():
    if count > 1:
        multiple_salaries_exist = True
        break

if multiple_salaries_exist:
    print("Der findes personer med samme løn.")
else:
    print("Der findes ikke personer med samme løn.")