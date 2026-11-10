TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
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

prihlasovaci_udaje = {
    "bob": "123", 
    "ann": "pass123", 
    "mike": "password123", 
    "liz": "pass123"
    }

user = input("Username: ")
password = input("Password: ")

print("---------------------------------------------------------")

if user not in prihlasovaci_udaje:
    print("Unregistered user, terminating the program...")
    exit()

if password != prihlasovaci_udaje[user]:
    print("Invalid password, terminating the program...")
    exit()

pocet_textu = len(TEXTS)

print(f"Welcome to the app, {user} we have {pocet_textu} texts to be analyzed.")

print("---------------------------------------------------------")

zvoleny_text = input(f"Enter a number btw. 1 and {pocet_textu} to select: ")

print("---------------------------------------------------------")

if not zvoleny_text.isdigit():
    print("Invalid text selection, terminating the program...")
    exit()

zvoleny_text = int(zvoleny_text)

if zvoleny_text < 1 or zvoleny_text > len(TEXTS):
    print("Invalid text selection, terminating the program...")
    exit()

list_zvoleneho_textu = TEXTS[zvoleny_text - 1].split()

pocet_slov = len(list_zvoleneho_textu)
pocet_slov_velka = 0
pocet_slov_mala = 0
pocet_slov_capslock = 0
poct_cisel = 0
soucet_cisel = 0


for slovo in list_zvoleneho_textu:
    if slovo[0].isupper() and not slovo.isupper():
        pocet_slov_velka += 1
    elif slovo.islower():
        pocet_slov_mala += 1

    if slovo.isupper():
        pocet_slov_capslock += 1

    if slovo.isnumeric():
        poct_cisel += 1
        soucet_cisel += int(slovo)

print(f"There are {pocet_slov} words in the selected text.")
print(f"There are {pocet_slov_velka} titlecase words.")
print(f"There are {pocet_slov_mala} lowercase words.")
print(f"There are {pocet_slov_capslock} uppercase words.")
print(f"There are {poct_cisel} numeric strings.")
print(f"The sum of all numbers is {soucet_cisel}.")

print("---------------------------------------------------------")
print("LEN | OCCURENCES | NR.")
print("---------------------------------------------------------")

histogram = {}

for hodnota in list_zvoleneho_textu:
    if len(hodnota.strip(",.!?;:()[]{}\"\'")) not in histogram:
        histogram[len(hodnota.strip(",.!?;:()[]{}\"\'"))] = 1
    else:
        histogram[len(hodnota.strip(",.!?;:()[]{}\"\'"))] += 1

serazeny_histogram = sorted(histogram.items())

for klic in serazeny_histogram:
    print(f"{klic[0]:<3}| {'*' * klic[1]:<20}|{klic[1]}")