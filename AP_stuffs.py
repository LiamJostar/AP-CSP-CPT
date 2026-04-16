import random
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
Rarity = ["Rare", "Rare", "Rare", "Super rare", "Super rare", "Mythical"]
Pri_roll = random.choice(Loot_pri)
Rarity_roll = random.choice(Rarity)
Loot_roll = random.choice(Loot_type)
Curr_roll = random.choice(Loot_curr)
Arm_roll = random.choice(Loot_armor)
Num_roll = random.choice(Curr_amt)
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
