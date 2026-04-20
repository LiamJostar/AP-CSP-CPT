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
Mythic_Chestpiece = ["Fallen Knight's Chestpiece", "Nightmare Chestpiece", "God's Heart", "The Hero's Chestpiece"]
Rare_Greaves = ["Wooden Greaves", "Leather Greaves", "Leaf Greaves", "Clay Greaves"]
SupRare_Greaves = ["Iron Greaves", "Silver Greaves", "Rusted Knight Greaves", "Tin Greaves"]
Mythic_Greaves = ["Fallen Knight's Greaves", "Nightmare Greaves", "God's Speed", "The Monarch's Greaves"]
Rare_Boots = ["Leather Boots", "Wooden Boots", "Foil Boots", "Light Weight Boots"]
SupRare_Boots = ["Hermes Boots", "Steel Boots", "Iron Boots", "Heavy Weight Boots"]
Mythic_Boots = ["TerraSpark Boots", "Fallen Knight's Boots", "Nightmare Boots", "The Mourner's Boots", "God's Remorse"]
Rare_Shield = ["Wooden Shield", "Aluminum Shield", "Rusted Metal Shield", "Cardboard Shield"]
SupRare_Shield = ["Iron Shield", "Silver Shield", "Freezing Shield", "Flame Shield"]
Mythic_Shield = ["The Defender's Shield", "Nightmare Shield", "God's Word", "The Greiver's Shield"]
Rare_Dagger = ["Wooden Dagger", "Aluminum Dagger", "Rusty Metal Dagger", "Kunai"]
SupRare_Dagger = ["Flame Dagger", "Shock Dagger", "Iron Dagger", "Silver Dagger"]
Mythic_Dagger = ["God's Reprimand", "Nightmare Dagger", "Roaring Dagger", "DragonScale Dagger"]
Rare_Dart = ["Wood Dart", "Bronze-tipped Dart", "Splinter-Shot Dart", "Rusted Dart"]
SupRare_Dart = ["Flaming Dart", "Frozen Dart", "Shocking Dart", "Poison Dart"]
Mythic_Dart = ["Plagued Dart", "God's Blight", "Nightmare Dart", "Goblin Dart"]
Rare_Chakram = ["Wood Chakram", "Bronze Chakram", "Light Chakram", "Heavy Chakram"]
SupRare_Chakram = ["Flame Chakram", "Freeze Chakram", "Dual Chakrams", "Shockram"]
Mythic_Chakram = ["God's will", "Nightmare Chakram", "Hellfire Chakram", "15000 volt Shockram"]
Rarity = ["Rare"]*60 + ["Super Rare"]*30 + ["Mythic"]*10
Pri_roll = random.choice(Loot_pri)
Sec_roll = random.choice(Loot_sec)
Rarity_roll = random.choice(Rarity)
Loot_roll = random.choice(Loot_type)
Curr_roll = random.choice(Loot_curr)
Arm_roll = random.choice(Loot_armor)
Num_roll = random.choice(Curr_amt)
Start = input("Welcome. Are you prepared to enter? ").lower()

if Start == "y" or Start == "yes":
     print("You go into the Dungeon...\n")
     time.sleep(1)
     print("\nDungeon Loot RNG\nIt's time to roll")
Roll = input("Would you like to roll? ").lower()
while Roll in ["y", "yes"]:
    Loot_roll = random.choice(Loot_type)
    Pri_roll = random.choice(Loot_pri)
    Rarity_roll = random.choice(Rarity)
    Sec_roll = random.choice(Loot_sec)
    Curr_roll = random.choice(Loot_curr)
    Num_roll = random.choice(Curr_amt)
    Arm_roll = random.choice(Loot_armor)
    if Loot_roll == "Primary Weapon":
     
     if Rarity_roll == "Rare":
        if Pri_roll == "Sword":
            item = random.choice(Rare_Sword)
        elif Pri_roll == "Bow":
            item = random.choice(Rare_Bow)
        elif Pri_roll == "Axe":
            item = random.choice(Rare_Axe)
        elif Pri_roll == "Sythe":
            item = random.choice(Rare_Sythe)

     elif Rarity_roll == "Super Rare":
        if Pri_roll == "Sword":
            item = random.choice(SupRare_Sword)
        elif Pri_roll == "Bow":
            item = random.choice(SupRare_Bow)
        elif Pri_roll == "Axe":
            item = random.choice(SupRare_Axe)
        elif Pri_roll == "Sythe":
            item = random.choice(SupRare_Sythe)

     elif Rarity_roll == "Mythic":
        if Pri_roll == "Sword":
            item = random.choice(Mythic_Sword)
        elif Pri_roll == "Bow":
            item = random.choice(Mythic_Bow)
        elif Pri_roll == "Axe":
            item = random.choice(Mythic_Axe)
        elif Pri_roll == "Sythe":
            item = random.choice(Mythic_Sythe)

     print(f"You got a {Rarity_roll} {item}")
    elif Loot_roll == "Secondary Weapon":
         if Rarity_roll == "Rare":
            if Sec_roll == "Shield":
                item = random.choice(Rare_Shield)
            elif Sec_roll == "Dagger":
               item = random.choice(Rare_Dagger)
            elif Sec_roll == "Dart":
             item = random.choice(Rare_Dart)
            elif Sec_roll == "Chakram":
              item = random.choice(Rare_Chakram)

         elif Rarity_roll == "Super Rare":
            if Sec_roll == "Shield":
             item = random.choice(SupRare_Shield)
            elif Sec_roll == "Dagger":
             item = random.choice(SupRare_Dagger)
            elif Sec_roll == "Dart":
             item = random.choice(SupRare_Dart)
            elif Sec_roll == "Chakram":
             item = random.choice(SupRare_Chakram)

         elif Rarity_roll == "Mythic":
             if Sec_roll == "Shield":
              item = random.choice(Mythic_Shield)
             elif Sec_roll == "Dagger":
                 item = random.choice(Mythic_Dagger)
             elif Sec_roll == "Dart":
                  item = random.choice(Mythic_Dart)
             elif Sec_roll == "Chakram":
                 item = random.choice(Mythic_Chakram)
         print(f"You got a {Rarity_roll} {item}")
    elif Loot_roll == "Currency":
     print(f"You got {Num_roll} {Curr_roll}")
    elif Loot_roll == "Armor":
        if Rarity_roll == "Rare":
            if Arm_roll == "Helm":
                item = random.choice(Rare_helm)
            elif Arm_roll == "Chestpiece":
             item = random.choice(Rare_Chestpiece)
            elif Arm_roll == "Greaves":
             item = random.choice(Rare_Greaves)
            elif Arm_roll == "Boots":
             item = random.choice(Rare_Boots)

        elif Rarity_roll == "Super Rare":
            if Arm_roll == "Helm":
                item = random.choice(SupRare_helm)
            elif Arm_roll == "Chestpiece":
                item = random.choice(SupRare_Chestpiece)
            elif Arm_roll == "Greaves":
                item = random.choice(SupRare_Greaves)
            elif Arm_roll == "Boots":
                item = random.choice(SupRare_Boots)

        elif Rarity_roll == "Mythic":
            if Arm_roll == "Helm":
             item = random.choice(Mythic_helm)
            elif Arm_roll == "Chestpiece":
             item = random.choice(Mythic_Chestpiece)
            elif Arm_roll == "Greaves":
             item = random.choice(Mythic_Greaves)
            elif Arm_roll == "Boots":
             item = random.choice(Mythic_Boots)
        print(f"You got a {Rarity_roll} {item}")
    Roll = input("\nRoll again? ").lower()