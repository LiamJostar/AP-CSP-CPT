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
rarity = ["Rare"]*60 + ["Super Rare"]*30 + ["Mythic"]*10
pri_roll = random.choice(loot_pri)
sec_roll = random.choice(loot_sec)
rarity_roll = random.choice(rarity)
loot_roll = random.choice(loot_type)
curr_roll = random.choice(loot_curr)
arm_roll = random.choice(loot_armor)
num_roll = random.choice(curr_amt)
start = input("Welcome. Are you prepared to enter? ").lower()

#def game(player name):

#get player name input 
#run= game("Jojo")

if start == "y" or start == "yes":
     print("You go into the Dungeon...\n")
     time.sleep(1)
     print("\nDungeon Loot RNG\nIt's time to roll")
else:
   print("you suck")
roll = input("Would you like to roll? ").lower()
while roll in ["y", "yes"]:
    loot_roll = random.choice(loot_type)
    pri_roll = random.choice(loot_pri)
    rarity_roll = random.choice(rarity)
    sec_roll = random.choice(loot_sec)
    curr_roll = random.choice(loot_curr)
    num_roll = random.choice(curr_amt)
    arm_roll = random.choice(loot_armor)
    if loot_roll == "Primary Weapon":
     
     if rarity_roll == "Rare":
        if pri_roll == "Sword":
            item = random.choice(rare_Sword)
        elif pri_roll == "Bow":
            item = random.choice(rare_Bow)
        elif pri_roll == "Axe":
            item = random.choice(rare_Axe)
        elif pri_roll == "Sythe":
            item = random.choice(rare_Sythe)

     elif rarity_roll == "Super Rare":
        if pri_roll == "Sword":
            item = random.choice(supRare_Sword)
        elif pri_roll == "Bow":
            item = random.choice(supRare_Bow)
        elif pri_roll == "Axe":
            item = random.choice(supRare_Axe)
        elif pri_roll == "Sythe":
            item = random.choice(supRare_Sythe)

     elif rarity_roll == "pythic":
        if pri_roll == "Sword":
            item = random.choice(mythic_Sword)
        elif pri_roll == "Bow":
            item = random.choice(mythic_Bow)
        elif pri_roll == "Axe":
            item = random.choice(mythic_Axe)
        elif pri_roll == "Sythe":
            item = random.choice(mythic_Sythe)

     print(f"You got a {rarity_roll} {item}")
    elif loot_roll == "Secondary Weapon":
         if rarity_roll == "Rare":
            if sec_roll == "Shield":
                item = random.choice(rare_Shield)
            elif sec_roll == "Dagger":
               item = random.choice(rare_Dagger)
            elif sec_roll == "Dart":
             item = random.choice(rare_Dart)
            elif sec_roll == "Chakram":
              item = random.choice(rare_Chakram)

         elif rarity_roll == "Super Rare":
            if sec_roll == "Shield":
             item = random.choice(supRare_Shield)
            elif sec_roll == "Dagger":
             item = random.choice(supRare_Dagger)
            elif sec_roll == "Dart":
             item = random.choice(supRare_Dart)
            elif sec_roll == "Chakram":
             item = random.choice(supRare_Chakram)

         elif rarity_roll == "Mythic":
             if sec_roll == "Shield":
              item = random.choice(mythic_Shield)
             elif sec_roll == "Dagger":
                 item = random.choice(mythic_Dagger)
             elif sec_roll == "Dart":
                  item = random.choice(mythic_Dart)
             elif sec_roll == "Chakram":
                 item = random.choice(mythic_Chakram)
         print(f"You got a {rarity_roll} {item}")
    elif loot_roll == "Currency":
     print(f"You got {num_roll} {curr_roll}")
    elif loot_roll == "Armor":
        if rarity_roll == "Rare":
            if arm_roll == "Helm":
                item = random.choice(rare_helm)
            elif arm_roll == "Chestpiece":
             item = random.choice(rare_Chestpiece)
            elif arm_roll == "Greaves":
             item = random.choice(rare_Greaves)
            elif arm_roll == "Boots":
             item = random.choice(rare_Boots)

        elif rarity_roll == "Super Rare":
            if arm_roll == "Helm":
                item = random.choice(supRare_helm)
            elif arm_roll == "Chestpiece":
                item = random.choice(supRare_Chestpiece)
            elif arm_roll == "Greaves":
                item = random.choice(supRare_Greaves)
            elif arm_roll == "Boots":
                item = random.choice(supRare_Boots)

        elif rarity_roll == "Mythic":
            if arm_roll == "Helm":
             item = random.choice(mythic_helm)
            elif arm_roll == "Chestpiece":
             item = random.choice(mythic_Chestpiece)
            elif arm_roll == "Greaves":
             item = random.choice(mythic_Greaves)
            elif arm_roll == "Boots":
             item = random.choice(mythic_Boots)
        print(f"You got a {rarity_roll} {item}")
    Roll = input("\nRoll again? ").lower()

