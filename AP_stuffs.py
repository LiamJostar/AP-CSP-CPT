import random
import time
Loot_type = ["Primary Weapon", "Secondary Weapon", "Currency", "Armor"]
Loot_pri = ["Sword", "Bow", "Axe", "Sythe"]
Loot_sec = ["Shield", "Dagger", "Dart", "Chakram"]
Loot_curr = ["Coins", "Gems", "Dark Dollars", "Tokens"]
Curr_amt = ["1", "2", "3", "4", "5"]
Loot_armor = ["Helm", "Chestpiece", "Greaves", "Boots"]
Rare_Sword = ["Bronze Greatsword", "Bronze Shortsword", "Bronze Longsword", "Bronze Rapier"]
Rare_Bow = ["Longbow", "Shortbow", "Strongbow", "Quickbow"]
Rare_Axe = ["Dual Axe", "Great axe", "Handaxe", "Double Handaxe"]
Rare_Sythe = ["Poison sythe", "Quicksythe", "Dual sythe", "Syckle"]
SupRare_Sword = ["Iron Greatsword", "Iron Shortsword", "Iron Longsword", "Iron Rapier"]
SupRare_Bow = ["Flarebow", "Shockbow", "Barbed Bow", "Freezebow"]
SupRare_Axe = ["Waraxe", "Shockaxe", "Flareaxe", "Freezeaxe"]
SupRare_Sythe = ["Poison Syckle", "Cursed sythe", "Circus Blade", "Dual Poison Sythe"]
Mythic_Sword = ["Nightmare Blade", "Roaring Shortsword", "Dragonscale Blade", "God's Wisdom"]
Mythic_Bow = ["Nightmare Bow", "God's Sight", "Fay Bow", "Dwarven Craft"]
Mythic_Axe = ["Nightmare Axe", "God's Rage", "Rude Buster", "Dwarven Hammer"]
Mythic_Sythe = ["Nightmare Sythe", "God's Plague", "Jevilsknife", "Reaper"]
Rare_helm = ["Leather Helm", "Bronze Helm", "Quick Helm", "Strong Helm"]
SupRare_helm = ["Iron Helm", "Flame Helm", "Spider Helm", "Shock Helm"]
Mythic_helm = ["Nightmare Helm", "Hellfire Helm", "God's Touch", "Jevilstail"]
Rare_Chestpiece = ["Leather Chestpiece", "Bronze Chestpiece", "Plate Mail", "Aluminum Chestpiece"]
SupRare_Chestpiece = ["Iron Chestpiece", "Silver Chestpiece", "Rusted Knight Chestpiece", "Tin Chestpiece"]
Mythic_Chestpiece = ["God's Fallen Knight's Chestpiece", "Nightmare Chestpiece", "Blessed Chestpiece", "The Hero's Chestpiece"]
Rare_Greaves = ["Wooden Greaves", "Leather Greaves", "Leaf Greaves", "Clay Greaves"]
SupRare_Greaves = ["Iron Greaves", "Silver Greaves", "Rusted Knight Greaves", "Tin Greaves"]
Mythic_Greaves = ["God's Fallen Knight's Greaves", "Nightmare Greaves", "Holy Greaves", "The Monarch's Greaves"]
Rare_Boots = ["Leather Boots", "Wooden Boots", "Foil Boots", "Light Weight Boots"]
SupRare_Boots = ["Herme's Boots", "Steel Boots", "Iron Boots", "Heavy Weight Boots"]
Mythic_Boots = ["TerraSpark Boots", "God's Fallen Knight's Boots", "Nightmare Boots", "The Mourner's Boots"]
Rare_Shield = ["Wooden Shield", "Aluminum Shield", "Rusted Metal Shield", "Cardboard Shield"]
SupRare_Shield = ["Iron Shield", "Silver Shield", "Steel Shield", "Fire Shield"]
Mythic_Shield = ["The Defender's Shield", "Nightmare Shield", "Heavenly Shield", "The Greiver's Shield"]
Rare_Dagger = ["Wooden Dagger", "Aluminum Dagger", "Rusty Metal Dagger"]
Rarity = ["Rare", "Rare", "Rare", "Super rare", "Super rare", "Mythical"]
Pri_roll = random.choice(Loot_pri)
Rarity_roll = random.choice(Rarity)
Loot_roll = random.choice(Loot_type)
Curr_roll = random.choice(Loot_curr)
Arm_roll = random.choice(Loot_armor)
Num_roll = random.choice(Curr_amt)
Start = input("Welcome. Are you ready to begin? ").lower
Char = input("Choose a Character:\nHuman: uses Sword\nElf:uses Bow\nDwarf:uses Axe\nOrc:uses Sythe\n").lower
Options = input("Fight\nStats\nRest\nQuit\n")
print(Start)
if Start == "y" or "Y" or "yes" or "Yes":
    print(Char)
else:
     print("Come back later")
    
if Char == "human":
     print("Welcome Human. \nAquired Wooden Sword")
elif Char == "elf":
     print("Welcome Elf.\nAquired Wooden Bow")
elif Char == "dwarf":
     print("Welcome Dwarf.\nAquired Wooden Axe")
elif Char == "orc":
     print("Welcome Orc.\nAquired Wooden Sythe")
else:
     print("not option")

Options = input("Fight\nStats\nRest\nQuit\n").lower

if Options == "fight":
     print("\nEntered dungeon")
     time.sleep(1)
     print("\n.")
     time.sleep(1)
     print("\n.")
     time.sleep(1)
     print("\nA Slime appears, Green in color, an angry look in its eyes.")
     time.sleep(0.35)
     UI = input("1. Primary Attack\n2. Secondary Attack\n3. Block\n4. Run Away\n")
     print(UI)
elif Options == "stats":
     print("ATK: 5\nDEF: 5\nSPD: 3\nWeapon: Wooden Sword")
     time.sleep(7.5)
     print(Options)








if Loot_roll == "Weapon":
 if Pri_roll == "Sword" and Rarity_roll == "Rare":
    print("You Got: ", random.choice(Rare_Sword))
 elif Pri_roll  == "Bow" and Rarity_roll == "Rare":
     print("You got: ", random.choice(Rare_Bow))
 elif Pri_roll  == "Axe" and Rarity_roll == "Rare":
        print("You got: ", random.choice(Rare_Axe))
 elif Pri_roll  == "Sythe" and Rarity_roll == "Rare":
        print("You got: ", random.choice(Rare_Sythe))
 elif Pri_roll == "Sword" and Rarity_roll == "Super rare":
        print("You Got: ", random.choice(SupRare_Sword))
 elif Pri_roll  == "Bow" and Rarity_roll == "Super rare":
        print("You got: ", random.choice(SupRare_Bow))
 elif Pri_roll  == "Axe" and Rarity_roll == "Super rare":
        print("You got: ", random.choice(SupRare_Axe))
 elif Pri_roll  == "Sythe" and Rarity_roll == "Super rare":
        print("You got: ", random.choice(SupRare_Sythe))
 elif Pri_roll == "Sword" and Rarity_roll == "Mythic":
        print("Congratulations! You got: ", random.choice(Mythic_Sword))
 elif Pri_roll  == "Bow" and Rarity_roll == "Mythic":
        print("Congratulations! You got: ", random.choice(Mythic_Bow))
 elif Pri_roll  == "Axe" and Rarity_roll == "Mythic":
        print("Congratulations! You got: ", random.choice(Mythic_Axe))
 elif Pri_roll  == "Sythe" and Rarity_roll == "Mythic":
        print("Congratulations! You got: ", random.choice(Mythic_Sythe))
elif Loot_roll == "Currency":
 if Curr_roll == "Coins":
        if Num_roll == "1":
            print("You got 1 coin! ")
        elif  Num_roll == "2":
            print("You got 2 coins! ")
        elif  Num_roll == "3":
            print("You got 3 coins! ")
        elif  Num_roll == "4":
            print("You got 4 coins! ")
        elif  Num_roll == "5":
            print("You got 5 coins! ")
elif Curr_roll == "Gems":
        if Num_roll == "1":
            print("You got 1 gem! ")
        elif  Num_roll == "2":
            print("You got 2 gems! ")
        elif  Num_roll == "3":
            print("You got 3 gems! ")
        elif  Num_roll == "4":
            print("You got 4 gems! ")
        elif  Num_roll == "5":
            print("You got 5 gems! ")
elif Curr_roll == "Dark Dollars":
        if Num_roll == "1":
            print("You got 1 Dark Dollar! ")
        elif  Num_roll == "2":
            print("You got 2 Dark Dollars! ")
        elif  Num_roll == "3":
            print("You got 3 Dark Dollars! ")
        elif  Num_roll == "4":
            print("You got 4 Dark Dollars! ")
        elif  Num_roll == "5":
            print("You got 5 Dark Dollars! ")
elif Curr_roll == "Tokens":
        if Num_roll == "1":
            print("You got 1 Token! ")
        elif  Num_roll == "2":
            print("You got 2 Tokens! ")
        elif  Num_roll == "3":
            print("You got 3 Tokens! ")
        elif  Num_roll == "4":
            print("You got 4 Tokens! ")
        elif  Num_roll == "5":
            print("You got 5 Tokens! ")
elif Loot_type == "Armor":
    if Arm_roll == "Helm" and Rarity_roll == "Rare":
        print("You got: ", random.choice(Rare_helm)) 
    elif Arm_roll == "Helm" and Rarity_roll == "Super Rare":
        print("You got: ", random.choice(SupRare_helm))
    elif Arm_roll == "Helm" and Rarity_roll == "Mythic":
        print("You got: ", random.choice(Mythic_helm))
    elif Arm_roll == "Chestpiece" and Rarity_roll == "Rare":
        print("You got: ", random.choice(Rare_Chestpiece))
    elif Arm_roll == "Chestpiece" and Rarity_roll == "Super Rare":
        print("You got: ", random.choice(SupRare_Chestpiece))
    elif Arm_roll == "Chestpiece" and Rarity_roll == "Mythic":
        print("You got: ", random.choice(Mythic_Chestpiece))
    elif Arm_roll == "Greaves" and Rarity_roll == "Rare":
        print("You got: ", random.choice(Rare_Greaves))
    elif Arm_roll == "Greaves" and Rarity_roll == "Super Rare":
        print("You got: ", random.choice(SupRare_Greaves))
    elif Arm_roll == "Greaves" and Rarity_roll == "Mythic":
        print("You got: ", random.choice(Mythic_Greaves))