# Funktion för att visa menyn
def visa_menyn():
    print("1. Starta nytt spel")
    print("2. Spara spelet")
    print("3. Ladda spelet")
    print("4. Avsluta")

# Funktion för att starta spelet
def starta_spel():
    print("Välj din karaktär:")
    print("1. Krigare")
    print("2. Magiker")
    print("3. Tjuv")

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
            print("Ogiltigt val.")

    print("Du vaknar i en mörk grotta.")
    plats = "grottan"
    inventarium = []
    hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)

# Funktion för att hantera spelet
def hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet):
    if plats == "grottan":
        print("Du ser två vägar framåt.")
        val = input("Vill du gå vänster (v) eller höger (h)? ")
        if val == "v":
            plats = "skattkammaren"
            print("Du går vänster.")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
        elif val == "h":
            plats = "mork_gang"
            print("Du går höger.")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
        else:
            print("Ogiltigt val.")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
    elif plats == "skattkammaren":
        print("Du hittar en skattkista! Men en goblin vaktar den.")
        val = input("Vill du slåss (s) eller gå tillbaka (g)? ")
        if val == "s":
            print("Du slåss mot goblinen!")
            halsa = halsa - (20 - smidighet) # Smidighet minskar skada.
            print(f"Din hälsa: {halsa}")
            if halsa <= 0:
                print("Du dog!")
            else:
                print("Du besegrade goblinen!")
                inventarium.append("guld")
                print("Du hittade guld!")
                plats = "grottan"
                hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
        elif val == "g":
            plats = "grottan"
            print("Du går tillbaka.")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
        else:
            print("Ogiltigt val.")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
    elif plats == "mork_gang":
        print("Du går in i en mörk gång. Du snubblar och tappar 10 hälsa.")
        halsa = halsa - 10
        print(f"Din hälsa: {halsa}")
        if halsa <= 0:
            print("Du dog!")
        else:
            plats = "stenbron"
            print("Du hittar en stenbro.")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
    elif plats == "stenbron":
        print("Du står på en smal stenbro över en avgrund. Vad gör du?")
        val = input("Gå över (ö) eller gå tillbaka (g)? ")
        if val == "ö":
            plats = "hemlig_kammare"
            print("Du går över bron.")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
        elif val == "g":
            plats = "mork_gang"
            print("Du går tillbaka.")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
        else:
            print("Ogiltigt val.")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
    elif plats == "hemlig_kammare":
        print("Du hittar en hemlig kammare med en gammal bok.")
        val = input("Läsa boken (l) eller gå tillbaka (g)? ")
        if val == "l":
            print("Du läser boken och hittar en magisk formel!")
            inventarium.append("magisk_formel")
            plats = "avgrunden"
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
        elif val == "g":
            plats = "stenbron"
            print("Du går tillbaka.")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
        else:
            print("Ogiltigt val.")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
    elif plats == "avgrunden":
        print("Du står vid en djup avgrund. Du ser en liten stig på andra sidan.")
        val = input("Använd formeln (a) eller gå tillbaka (g)? ")
        if val == "a" and "magisk_formel" in inventarium:
            plats = "utgangen"
            print("Du använder formeln och skapar en tillfällig bro!")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
        elif val == "g":
            plats = "hemlig_kammare"
            print("Du går tillbaka.")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
        else:
            print("Ogiltigt val eller du har inte formeln.")
            hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
    elif plats == "utgangen":
        print("Du ser utgången! Du har klarat äventyret!")
        print("Grattis!")
        return

# Funktion för att spara spelet
def spara_spelet(plats, halsa, inventarium, attack, magi, smidighet):
    try:
        with open("savegame.txt", "w") as fil:
            fil.write(f"{plats}\n{halsa}\n{inventarium}\n{attack}\n{magi}\n{smidighet}")
        print("Spelet sparades!")
    except:
        print("Kunde inte spara spelet.")

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
        print("Spelet laddades!")
        hantera_spelet(plats, halsa, inventarium, attack, magi, smidighet)
    except FileNotFoundError:
        print("Ingen sparfil hittades.")
    except:
        print("Kunde inte ladda spelet.")

# Huvudprogram
while True:
    visa_menyn()
    val = input("Välj ett alternativ: ")
    if val == "1":
        starta_spel()
    elif val == "2":
        spara_spelet()
    elif val == "3":
        ladda_spelet()
    elif val == "4":
        print("Du avslutade spelet.")
        break
        