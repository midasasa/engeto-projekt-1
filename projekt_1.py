"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Michal Soukop
email: midasasa5757@gmail.com
discord: miso5757 (engeto server: Michal S.)
"""
# list
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# slovník
register = {
    "bob":"123",
    "ann":"pass123",
    "mike":"password123",
    "liz":"pass123"
}

oddelovac = 40 * "-"

# uživatel zadá vstupy
username = input("Zadej jméno: ").lower()
password = input("Zadej heslo: ")
print(oddelovac)

# Kontrola, zda je "username" a "password" ve slovníku "register"
if username in register and register[username] == password:
    print(f"Welcome to the app, {username}.")
    print(f"We have 3 texts to be analyzed. \n{oddelovac}")
else:
    print("Unregistered user, terminating the program..")
    quit()

# uživatel zadá vstup pro výběr textu, volba 1, 2, 3.
choice = (input("Enter a number btw. 1 and 3 to select: "))

# kontrola, zda uživatelský vstup je číslo
if choice.isdigit():
    number = int(choice)
    if number in [1, 2, 3]:
        print(oddelovac)
    else:
        print("Wrong number. Must be 1, 2, 3!")
        exit()
else:
    print("You have to enter a number!")
    exit()

# výběr části textu dle uživatelskýho výběru, rozdělení na slova
words = (TEXTS[number - 1]).split()

# vytvoření prázdného slovníku, kam přijdou vyčištěná slova
cleaned_words = []

# přidání vyčištěných slov do slovníku "cleaned_words"
for word in words:
    cleaned_words.append(word.strip(".,"))

# zjištění počtu slov ve slovníku
count_words = len(cleaned_words)

# počítání.....
first_upper = 0
big_upper = 0
lower = 0
numeric_strings = 0

# iterace ve slovníku.....
for word in cleaned_words:
        if word[0].isupper():       # první písmeno velké
            first_upper += 1
        elif word.isupper():        # všechno velká písmena
            big_upper += 1
        elif word.islower():        # všechno malá písmena
            lower += 1
        elif word.isdigit():        # počet číselných řetězců
            numeric_strings += 1

# slovník pro čísla
sumof = []

# iterace ve slovníku.....
for nums in cleaned_words:
    if nums.isdigit():
        sumof.append(int(nums))


print(f"There are {count_words} words in the selected text.")   # vytiskne počet slov ve vybrané části textu
print(f"There are {first_upper} titlecase words.")              # vytiskne počet slov začínající velkým písmenem ve vybrané části textu
print(f"There are {big_upper} uppercase words.")                # vytiskne počet slov psaných vše velkým písmem ve vybrané části textu
print(f"There are {lower} lowercase words.")                    # vytiskne počet slov psaných vše malým písmem ve vybrané části textu
print(f"There are {numeric_strings} numeric strings.")          # vytiskne počet numeric string ve vybrané části textu
print(f"The sum of all the numbers {(sum(sumof))}")             # vytiskne součet čísel ve vybrané části textu

# graf hlavička
print(oddelovac, f'{"LEN":>3}|{"OCCURENCES":^18}|{"NR."}', oddelovac, sep="\n")

# slovník pro různé délky slov
occ_words = {}

# iterace přes seznam a počítá četnost každé délky slova
for word in cleaned_words:
    if len(word) not in occ_words:
        occ_words[len(word)] = 1                            # pokud není délka ve slovníku, přidá
    else:
        occ_words[len(word)] = occ_words[len(word)] + 1     # pokud už je ve slovníku, tak přičte +1

# seřazení slovníku
sort = dict(sorted(occ_words.items()))

# iterace přes slovník, tisk grafu
for key, value in sort.items():
    print(f'{key:3}|{"*" * value:<18}|{value}')