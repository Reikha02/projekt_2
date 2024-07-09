"""
projekt_1.py: První projekt do Engeto Online Python Akademie
author: Michaela Terelya
email: michaela.terelya@gmail.com
discord: reikha.
"""

from task_template import TEXTS

# Vložíme do programu informaci o registrovaných uživatelech
reg_uzivatele = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

# Vyžádáme si od uživatele přihlašovací jméno a heslo
username = input("username: ")
password = input("password: ")

# Vyhodnocení zadávaných přihlašovací údajů 
if username in reg_uzivatele and reg_uzivatele[username] == password:
    print("----------------------------------------")
    print(f"Welcome to the app, {username}")
    print(f"We have {len(TEXTS)} texts to be analyzed.")
    print("----------------------------------------")
else:
    print("Unregistered user, terminating the program...")
    exit()

# Možnost výběru textu s kontrolou, jestli je zadávané číslo je číslem a jestli odpovídá rozsahu odstupných textů.
while True:
    cislo_textu = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
    if cislo_textu.isdigit():
        cislo_textu = int(cislo_textu)
        if 1 <= cislo_textu <= len(TEXTS):
            vybrany_text = TEXTS[cislo_textu - 1]
            break
        else:
            print(f"Input error. Please enter a number between 1 and {len(TEXTS)}.")
    else:
        print("Input error. Please enter a number.")

# Analýza vybraného uživatelem textu
words = vybrany_text.split()
num_words = len(words)
num_titlecase_words = 0
num_uppercase_words = 0
num_lowercase_words = 0
numeric = []

# Očištění slov a jejich analýza
ocistena_slova = [word.strip(",.!?:;") for word in words]

for ocistene_slovo in ocistena_slova:
    if ocistene_slovo[0].istitle():
        num_titlecase_words += 1
    if ocistene_slovo.isupper() and ocistene_slovo.isalpha():
        num_uppercase_words += 1
    if ocistene_slovo.islower() and ocistene_slovo.isalpha():
        num_lowercase_words += 1
    if ocistene_slovo.isdigit():
        numeric.append(int(ocistene_slovo))

num_numeric = len(numeric)
sum_numeric = sum(numeric)

# Výpočet délky slov a uložení hodnot pro jejich následující zracování
delka_slov = {}
for ocistene_slovo in ocistena_slova:
    delka = len(ocistene_slovo)
    if delka in delka_slov:
        delka_slov[delka] += 1
    else:
        delka_slov[delka] = 1

# Výpis zjištěných hodnot
print("----------------------------------------")
print(f"There are {num_words} words in the selected text.")
print(f"There are {num_titlecase_words} titlecase words.")
print(f"There are {num_uppercase_words} uppercase words.")
print(f"There are {num_lowercase_words} lowercase words.")
print(f"There are {num_numeric} numeric strings.")
print(f"The sum of all the numbers {sum_numeric}")
print("----------------------------------------")
print("LEN|  OCCURRENCES  |NR.")
print("----------------------------------------")

for delka, pocet in sorted(delka_slov.items()):
    rada = '*' * pocet  
    print(f"{delka:2} | {rada:<12} | {pocet}")