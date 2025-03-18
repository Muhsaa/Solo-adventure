import time,os,sys

def clear_terminal():
    if os.name == "nt":
        os.system("cls")

def print_slow(Text):
    for char in Text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    sys.stdout.write("\n")
    sys.stdout.flush()

#  Funktion för att visa menyn
def visa_menyn():
    print_slow("1. Starta nytt spel")
    print_slow("2. Spara spelet")
    print_slow("3. Ladda spelet")
    print_slow("4. Avsluta")

# Funktion för att starta spelet
def starta_spel():
    print_slow("Välj din karaktär:")
    print_slow("1. Krigare")
    print_slow("2. Magiker")
    print_slow("3. Tjuv")


    while True:
        karaktar_val = input("Välj en karaktär (1-3): ")
        if karaktar_val == "1":
            halsa = 120
            attack = 20
            magi = 0
            smidighet = 5
            break
        elif karaktar_val == "2":
            halsa = 80
            attack = 10
            magi = 25
            smidighet = 10
            break
        elif karaktar_val == "3":
            halsa = 100
            attack = 15
            magi = 5
            smidighet = 20
            break
        else:
            print_slow("Ogiltigt val.")

    print_slow("Du vaknar i en mörk grotta.")
    plats = "grottan"
    inventarium = []
    hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)

# Funktion för att hantera spelet
def hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet):
    if plats == "grottan":
        print_slow("Du ser två vägar framåt.")
        val = input("Vill du gå vänster (v) eller höger (h)? ")
        if val == "v":
            plats = "skattkammaren"
            print_slow("Du går vänster.")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
        elif val == "h":
            plats = "mork_gang"
            print_slow("Du går höger.")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
        else:
            print_slow("Ogiltigt val.")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
    elif plats == "skattkammaren":
        print_slow("Du hittar en skattkista! Men en goblin vaktar den.")
        val = input("Vill du slåss (s) eller gå tillbaka (g)? ")
        if val == "s":
            print_slow("Du slåss mot goblinen!")
            halsa = halsa - (20 - smidighet) # Smidighet minskar skada.
            print_slow(f"Din hälsa: {halsa}")
            if halsa <= 0:
                print_slow("Du dog!")
            else:
                print_slow("Du besegrade goblinen!")
                inventarium.append("guld")
                print_slow("Du hittade guld!")
                plats = "grottan"
                hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
        elif val == "g":
            plats = "grottan"
            print_slow("Du går tillbaka.")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
        else:
            print_slow("Ogiltigt val.")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
    elif plats == "mork_gang":
        print_slow("Du går in i en mörk gång. Du snubblar och tappar 10 hälsa.")
        halsa = halsa - 10
        print_slow(f"Din hälsa: {halsa}")
        if halsa <= 0:
            print_slow("Du dog!")
        else:
            plats = "stenbron"
            print_slow("Du hittar en stenbro.")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
    elif plats == "stenbron":
        print_slow("Du står på en smal stenbro över en avgrund. Vad gör du?")
        val = input("Gå över (ö) eller gå tillbaka (g)? ")
        if val == "ö":
            plats = "hemlig_kammare"
            print_slow("Du går över bron.")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
        elif val == "g":
            plats = "mork_gang"
            print_slow("Du går tillbaka.")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
        else:
            print_slow("Ogiltigt val.")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
    elif plats == "hemlig_kammare":
        print_slow("Du hittar en hemlig kammare med en gammal bok.")
        val = input("Läsa boken (l) eller gå tillbaka (g)? ")
        if val == "l":
            print_slow("Du läser boken och hittar en magisk formel!")
            inventarium.append("magisk_formel")
            plats = "avgrunden"
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
        elif val == "g":
            plats = "stenbron"
            print_slow("Du går tillbaka.")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
        else:
            print_slow("Ogiltigt val.")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
    elif plats == "avgrunden":
        print_slow("Du står vid en djup avgrund. Du ser en liten stig på andra sidan.")
        val = input("Använd formeln (a) eller gå tillbaka (g)? ")
        if val == "a" and "magisk_formel" in inventarium:
            plats = "utgangen"
            print_slow("Du använder formeln och skapar en tillfällig bro!")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
        elif val == "g":
            plats = "hemlig_kammare"
            print_slow("Du går tillbaka.")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
        else:
            print_slow("Ogiltigt val eller du har inte formeln.")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
    elif plats == "utgangen":
        print_slow("Du ser utgången! Du har klarat äventyret!")
        print_slow("Grattis!")
        return

# Funktion för att spara spelet
def spara_spelet(plats, halsa, inventarium, attack, magi, smidighet):
    try:
        with open("savegame.txt", "w") as fil:
            fil.write(f"{plats}\n{halsa}\n{inventarium}\n{attack}\n{magi}\n{smidighet}")
        print_slow("Spelet sparades!")
    except:
        print_slow("Kunde inte spara spelet.")

# Funktion för att ladda spelet 
def ladda_spelet():
    try:
        with open("savegame.txt", "r") as fil:
            plats = fil.readline().strip()
            halsa = int(fil.readline().strip())
            inventarium = eval(fil.readline().strip())
            attack = int(fil.readline().strip())
            magi = int(fil.readline().strip())
            smidighet = int(fil.readline().strip())
        print_slow("Spelet laddades!")
        hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
    except FileNotFoundError:
        print_slow("Ingen sparfil hittades.")
    except:
        print_slow("Kunde inte ladda spelet.")

# Huvudprogram
game_is_on= True

while game_is_on == True:
    visa_menyn()
    val = input("Välj ett alternativ: ")
    if val == "1":
        clear_terminal()
        starta_spel()
    elif val == "2":
        clear_terminal()
        spara_spelet()
    elif val == "3":
        clear_terminal()
        ladda_spelet()
    elif val == "4":
        print_slow("Du avslutade spelet.")
        break