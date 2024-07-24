"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Michaela Terelya
email: michaela.terelya@gmail.com
discord: reikha.
"""


import random
import time

def vytvorit_tajne_cislo() -> str:
    cisla = list('123456789')
    random.shuffle(cisla)
    tajne_cislo = cisla[:4]
    return ''.join(tajne_cislo)

def get_bulls_and_cows(tajne: str, odhad: str) -> tuple[int, int]:
    bulls = sum(t == o for t, o in zip(tajne, odhad))
    cows = sum(o in tajne for o in odhad) - bulls
    return bulls, cows

def vhodny_odhad(odhad: str) -> bool:
    if len(odhad) != 4:
        return False
    if not odhad.isdigit():
        return False
    if len(set(odhad)) != 4:
        return False
    if odhad[0] == '0':
        return False
    return True

def vyhodnoceni_odhadu(bulls: int, cows: int) -> str:
    bulls_text = "bull" if bulls == 1 else "bulls"
    cows_text = "cow" if cows == 1 else "cows"
    return f"{bulls} {bulls_text}, {cows} {cows_text}"


def game() -> None:
    print(f"""
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
""")
    
    tajne_cislo = vytvorit_tajne_cislo()
    pokusy = 0
    zacatek_hry = time.time()

    while True:
        odhad = input("Enter a number: ")
        if not vhodny_odhad(odhad):
            print("Invalid guess. Make sure it's a 4-digit number with unique digits and doesn't start with 0.")
            continue

        pokusy += 1
        bulls, cows = get_bulls_and_cows(tajne_cislo, odhad)
        if bulls == 4:
            konec_hry = time.time()
            celkovy_cas = konec_hry - zacatek_hry
            print(f"Correct, you've guessed the right number in {pokusy} guesses!")
            if pokusy <= 5:
                hodnoceni = "awesome, you are a star"
            elif pokusy <= 10:
                hodnoceni = "average, you should train some more"
            else:
                hodnoceni = "not so good but cheer up and try again"
            print(f"That's {hodnoceni}!")
            print(f"It took you {celkovy_cas:.2f} seconds to guess the number.")
            break
        else:
            print(vyhodnoceni_odhadu(bulls, cows))
            print("-----------------------------------------------")

if __name__ == "__main__":
    game()