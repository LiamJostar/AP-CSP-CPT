import random
Loot_type = ["Primary Weapon", "Secondary Weapon", "Currency", "Armor"]
Loot_pri = ["Sword", "Bow", "Axe", "Sythe"]
Loot_sec = ["Shield", "Dagger", "Dart", "Chakram"]
Loot_curr = ["Coins", "Gems", "Dark Dollars", "Tokens"]
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


