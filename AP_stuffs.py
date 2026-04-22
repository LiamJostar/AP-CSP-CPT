import random
import time
loot_type = ["Primary Weapon", "Secondary Weapon", "Currency", "Armor"]
loot_pri = ["Sword", "Bow", "Axe", "Sythe"]
loot_sec = ["Shield", "Dagger", "Dart", "Chakram"]
loot_curr = ["Coins", "Gems", "Dark Dollars", "Tokens"]
curr_amt = ["1", "2", "3", "4", "5"]
loot_armor = ["Helm", "Chestpiece", "Greaves", "Boots"]
rare_Sword = ["Bronze Greatsword", "Bronze Shortsword", "Bronze Longsword", "Bronze Rapier"]
rare_Bow = ["Longbow", "Shortbow", "Strongbow", "Quickbow"]
rare_Axe = ["Dual Axe", "Great axe", "Handaxe", "Double Handaxe"]
rare_Sythe = ["Poison sythe", "Quicksythe", "Dual sythe", "Syckle"]
supRare_Sword = ["Iron Greatsword", "Iron Shortsword", "Iron Longsword", "Iron Rapier"]
supRare_Bow = ["Flarebow", "Shockbow", "Barbed Bow", "Freezebow"]
supRare_Axe = ["Waraxe", "Shockaxe", "Flareaxe", "Freezeaxe"]
supRare_Sythe = ["Poison Syckle", "Cursed sythe", "Circus Blade", "Dual Poison Sythe"]
mythic_Sword = ["Nightmare Blade", "Roaring Shortsword", "Dragonscale Blade", "God's Wisdom"]
mythic_Bow = ["Nightmare Bow", "God's Sight", "Fay Bow", "Dwarven Craft"]
mythic_Axe = ["Nightmare Axe", "God's Rage", "Rude Buster", "Dwarven Hammer"]
mythic_Sythe = ["Nightmare Sythe", "God's Plague", "Jevilsknife", "Reaper"]
rare_helm = ["Leather Helm", "Bronze Helm", "Quick Helm", "Strong Helm"]
supRare_helm = ["Iron Helm", "Flame Helm", "Spider Helm", "Shock Helm"]
mythic_helm = ["Nightmare Helm", "Hellfire Helm", "God's Touch", "Jevilstail"]
rare_Chestpiece = ["Leather Chestpiece", "Bronze Chestpiece", "Plate Mail", "Aluminum Chestpiece"]
supRare_Chestpiece = ["Iron Chestpiece", "Silver Chestpiece", "Rusted Knight Chestpiece", "Tin Chestpiece"]
mythic_Chestpiece = ["Fallen Knight's Chestpiece", "Nightmare Chestpiece", "God's Heart", "The Hero's Chestpiece"]
rare_Greaves = ["Wooden Greaves", "Leather Greaves", "Leaf Greaves", "Clay Greaves"]
supRare_Greaves = ["Iron Greaves", "Silver Greaves", "Rusted Knight Greaves", "Tin Greaves"]
mythic_Greaves = ["Fallen Knight's Greaves", "Nightmare Greaves", "God's Speed", "The Monarch's Greaves"]
rare_Boots = ["Leather Boots", "Wooden Boots", "Foil Boots", "Light Weight Boots"]
supRare_Boots = ["Hermes Boots", "Steel Boots", "Iron Boots", "Heavy Weight Boots"]
mythic_Boots = ["TerraSpark Boots", "Fallen Knight's Boots", "Nightmare Boots", "The Mourner's Boots", "God's Remorse"]
rare_Shield = ["Wooden Shield", "Aluminum Shield", "Rusted Metal Shield", "Cardboard Shield"]
supRare_Shield = ["Iron Shield", "Silver Shield", "Freezing Shield", "Flame Shield"]
mythic_Shield = ["The Defender's Shield", "Nightmare Shield", "God's Word", "The Greiver's Shield"]
rare_Dagger = ["Wooden Dagger", "Aluminum Dagger", "Rusty Metal Dagger", "Kunai"]
supRare_Dagger = ["Flame Dagger", "Shock Dagger", "Iron Dagger", "Silver Dagger"]
mythic_Dagger = ["God's Reprimand", "Nightmare Dagger", "Roaring Dagger", "DragonScale Dagger"]
rare_Dart = ["Wood Dart", "Bronze-tipped Dart", "Splinter-Shot Dart", "Rusted Dart"]
supRare_Dart = ["Flaming Dart", "Frozen Dart", "Shocking Dart", "Poison Dart"]
mythic_Dart = ["Plagued Dart", "God's Blight", "Nightmare Dart", "Goblin Dart"]
rare_Chakram = ["Wood Chakram", "Bronze Chakram", "Light Chakram", "Heavy Chakram"]
supRare_Chakram = ["Flame Chakram", "Freeze Chakram", "Dual Chakrams", "Shockram"]
mythic_Chakram = ["God's will", "Nightmare Chakram", "Hellfire Chakram", "15000 volt Shockram"]
rarity_pool = ["Rare"]*60 + ["Super Rare"]*30 + ["Mythic"]*10
pri_roll = random.choice(loot_pri)
sec_roll = random.choice(loot_sec)
rarity_roll = random.choice(rarity_pool)
loot_roll = random.choice(loot_type)
curr_roll = random.choice(loot_curr)
arm_roll = random.choice(loot_armor)
num_roll = random.choice(curr_amt)
def roll_for_loot():
    loot_category = random.choice(loot_type)
    rarity_roll = random.choice(rarity_pool)
    item = "Nothing Found"

    if loot_category == "Currency":
        num = random.choice(curr_amt)
        curr = random.choice(loot_curr)
        return f"You got {num} {curr}!"

    elif loot_category == "Primary Weapon":
        pri = random.choice(loot_pri)
        if rarity_roll == "Rare":
            if pri == "Sword": item = random.choice(rare_Sword)
            elif pri == "Bow": item = random.choice(rare_Bow)
            elif pri == "Axe": item = random.choice(rare_Axe)
            elif pri == "Sythe": item = random.choice(rare_Sythe)
        elif rarity_roll == "Super Rare":
            if pri == "Sword": item = random.choice(supRare_Sword)
            elif pri == "Bow": item = random.choice(supRare_Bow)
            elif pri == "Axe": item = random.choice(supRare_Axe)
            elif pri == "Sythe": item = random.choice(supRare_Sythe)
        elif rarity_roll == "Mythic":
            if pri == "Sword": item = random.choice(mythic_Sword)
            elif pri == "Bow": item = random.choice(mythic_Bow)
            elif pri == "Axe": item = random.choice(mythic_Axe)
            elif pri == "Sythe": item = random.choice(mythic_Sythe)

    elif loot_category == "Secondary Weapon":
        sec = random.choice(loot_sec)
        if rarity_roll == "Rare":
            if sec == "Shield": item = random.choice(rare_Shield)
            elif sec == "Dagger": item = random.choice(rare_Dagger)
            elif sec == "Dart": item = random.choice(rare_Dart)
            elif sec == "Chakram": item = random.choice(rare_Chakram)
        elif rarity_roll == "Super Rare":
            if sec == "Shield": item = random.choice(supRare_Shield)
            elif sec == "Dagger": item = random.choice(supRare_Dagger)
            elif sec == "Dart": item = random.choice(supRare_Dart)
            elif sec == "Chakram": item = random.choice(supRare_Chakram)
        elif rarity_roll == "Mythic":
            if sec == "Shield": item = random.choice(mythic_Shield)
            elif sec == "Dagger": item = random.choice(mythic_Dagger)
            elif sec == "Dart": item = random.choice(mythic_Dart)
            elif sec == "Chakram": item = random.choice(mythic_Chakram)

    elif loot_category == "Armor":
        arm = random.choice(loot_armor)
        if rarity_roll == "Rare":
            if arm == "Helm": item = random.choice(rare_helm)
            elif arm == "Chestpiece": item = random.choice(rare_Chestpiece)
            elif arm == "Greaves": item = random.choice(rare_Greaves)
            elif arm == "Boots": item = random.choice(rare_Boots)
        elif rarity_roll == "Super Rare":
            if arm == "Helm": item = random.choice(supRare_helm)
            elif arm == "Chestpiece": item = random.choice(supRare_Chestpiece)
            elif arm == "Greaves": item = random.choice(supRare_Greaves)
            elif arm == "Boots": item = random.choice(supRare_Boots)
        elif rarity_roll == "Mythic":
            if arm == "Helm": item = random.choice(mythic_helm)
            elif arm == "Chestpiece": item = random.choice(mythic_Chestpiece)
            elif arm == "Greaves": item = random.choice(mythic_Greaves)
            elif arm == "Boots": item = random.choice(mythic_Boots)

    return f"You got a {rarity_roll} {item}!"

start = input("Welcome. Are you prepared to enter? (y/n) ").lower()

if start in ["y", "yes"]:
    print("You go into the Dungeon...\n")
    time.sleep(1)
    print("Dungeon Loot RNG")
    print("It's time to roll!")
    
    roll = input("\nWould you like to roll? (y/n) ").lower()
    while roll in ["y", "yes"]:
        result = roll_for_loot()
        print("-" * 20)
        print(result)
        print("-" * 20)
        
        roll = input("Roll again? (y/n) ").lower()
    
    print("Thanks for playing!")


roll_for_loot()
