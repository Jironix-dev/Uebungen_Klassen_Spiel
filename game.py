#Name: Kevin Dietrich
#Datum: 03.03.2026
#Projekt: Übungen zu Klassen

from player import Player

Hulk = Player("Hulk", 5)
Flash = Player("Flash", 3)

Flash.health = 13
print(f"Flash Health = {Flash.health}")
print(f"Hulk Health = {Hulk.health}")

while True:
    Flash.hurt(Hulk.strength)
    print(f"Flash received {Hulk.strength} Damage, the new Health is {Flash.health}")

    if Hulk.is_dead() == True:
        print("Hulk died")
        break
    elif Flash.is_dead() == True:
        print("Flash died")
        break
    
    Hulk.hurt(Flash.strength)
    print(f"Hulk received {Flash.strength} Damage, the new Health is {Hulk.health}")

    if Hulk.is_dead() == True:
        print("Hulk died")
        break
    elif Flash.is_dead() == True:
        print("Flash died")
        break