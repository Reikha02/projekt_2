"""
projekt_1.py: První projekt do Engeto Online Python Akademie
author: Michaela Terelya
email: michaela.terelya@gmail.com
discord: reikha.
"""

from task_template import TEXTS

# Nejdříve vložíme do programu informaci o tom, jací jsou registrovaní uživatelé
#  použíjeme slovník pro párování klíče (user) a hodnoty (password)
reg_uzivatele = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

# Nyní vytvoříme funkci, které si vyžádá od uživatele přihlašovací jméno a heslo
username = input("username: ")
password = input("password: ")

# A teď vytvoříme funkci, která vyhodnotí jestli jsou zadané přihlašovací údaje "správné" 
#   a podle toho to uživatele pustí používat program dále
if username in reg_uzivatele and reg_uzivatele[username] == password:
    print("----------------------------------------\n" +
          "Welcome to the app, " + username + "\n" +
          "We have " + str(len(TEXTS)) + " texts to be analyzed.\n" +
          "----------------------------------------")
else:
    print("unregistered user, terminating the program..")
    exit()

# Teď je potřeba zpracovat část pro možnost výběru textu
# Provedeme kontrolu, že zadávané číslo je číslem a převedemo ho na integer, abychom mohli použít srovnávací operátory.
# V případě, že zadá jiné číslo, nebo zadá cokoli jiného než číslo, tak ho program na to upozorní a vyzve k zadání správné hodnoty.
while True:
    cislo_textu = input("Enter a number btw. 1 and 3 to select: ")
    if cislo_textu.isdigit():
        cislo_textu = int(cislo_textu)
        if 1 <= cislo_textu <= 3:
            vybrany_text = TEXTS[cislo_textu - 1]
            break
        else:
            print("Input error. Please enter a number between 1 and 3.")
    else:
        print("Input error. Please enter a number.")

# Teď je potřeba napsat část kódu, která zanalyzuje vybraný uživatelem text
words = vybrany_text.split()
num_words = len(words)
num_titlecase_words = len([word for word in words if word.istitle()])
num_uppercase_words = len([word for word in words if word.isupper()])
num_lowercase_words = len([word for word in words if word.islower()])
numeric = [int(word) for word in words if word.isdigit()]
num_numeric = len(numeric)
sum_numeric = sum(numeric)
# Tahle funkce má za úkol spočítat délku slov a jejich výskyt/četnost
# A pak je uloží je do nově vytvořeného slovníku, abychom hodnoty neztratily - to potřebujeme na vytvoření sloupcového grafu na kocni
# Pro maximální přesnost jsem doplnila .strip(",."), aby se čárky a tečky při analýze textu nezapočítávaly
delka_slov = {}
for word in words:
    delka = len(word.strip(",."))
    if delka in delka_slov:
        delka_slov[delka] += 1
    else:
        delka_slov[delka] = 1

# A nakonec je potřeba zjištěné hodnoty vypsat
print("----------------------------------------")
print("There are " + str(num_words) + " words in the selected text.")
print("There are " + str(num_titlecase_words) + " titlecase words.")
print("There are " + str(num_uppercase_words) + " uppercase words.")
print("There are " + str(num_lowercase_words) + " lowercase words.")
print("There are " + str(num_numeric) + " numeric strings.")
print("The sum of all the numbers " + str(sum_numeric))
print("----------------------------------------")
print("LEN|  OCCURENCES  |NR.")
print("----------------------------------------")

for delka, pocet in sorted(delka_slov.items()):
    rada = '*' * pocet  
    print("{:2} | {:<12} | {}".format(delka, rada, pocet))