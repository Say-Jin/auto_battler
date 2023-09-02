def random_rpg():

    import random
    dice_roll = random.randint(1, 12)

    hit_point_value = random.randint(1, 300)
    hit_point_value_crit = 2 * hit_point_value
        ##https://www.reddit.com/r/d100/comments/8jmo2x/list_of_
        # 100_random_monsters_cr_going_up/
    creature_list = ["Bandit", "Kobold", "Cultist",
    "Tribal Warrior", "Flying Snake", "Giant Rat", 
    "Giant Weasel", "Flumph", "Blood Hawk", "Giant Crab", 
    "Acolyte", "Boar", "Bullywug", "Drow", "Goblin", "Grimlock", 
    "Kenku", "Skeleton", "Winged Kobold", "Zombie", 
    "Cockatrice", "Deep Gnome", "Crocodile", "Gnoll", 
    "Hobgoblin", "Lizardfolk", "Orc", "Satyr", "Thug", 
    "Worg", "Animated Armor", "Bugbear", "Death Dog", 
    "Dryad", "Duergar", "Ghoul", "Giant Hyena", "Goblin Boss", 
    "Hippogriff", "Imp", "Bandit Captain", "Berserker", 
    "Carrion Crawler", "Centaur", "Cult Fanatic", "Griffon", 
    "Intellect Devourer", "Mimic", "Ogre", "Spined Devil", "Oro", 
    "Pentadrone", "Rhinoceros", "Sea Hag", "Swarm Of Poisonous Snakes",
     "Wererat", "Lizardfolk Shaman", "Grick", "Gibbering Mouther",
      "Ghast", "Basilisk", "Bearded Devil", "Bugbear Chief", 
      "Doppelganger", "Displacer Beast", "Grell", 
      "Hobgoblin Captain", "Minotaur", "Manticore", "Faze Spider", 
      "Banshee", "Chuul", "Elephant", "Ghost", "Flameskull", 
      "Helmed Horror", "Succubus", "Incubus", "Lamia", "Wereboar", 
      "Air Elemental", "Beholder Zombie", "Bulette", 
      "Flesh Golem", "Drow Elite Warrior", "Gladiator", "Gorgon", 
      "Revenant", "Umber Hulk", "Fire Elemental", "Hobgoblin Warlord", 
      "Mind Flayer", "Frost Giant", "Treant", "Guardian Naga", 
      "Horned Devil", "Archmage", "White Dragon", "Ice Devil", 
      "Death Tyrant"]
    random_creature = random.choice(creature_list)

    possibilities = ["Yes", "No"]

    ##response = random.choice(possibilities)
   


    print("Greetings, would you like to roll the die?")
    response = input("Yes or No: ")
    if response == "Yes" or response == "yes":
        print("The die shows: " + str(dice_roll))

        if dice_roll <= 3:
                print("And it's a miss.")
                print("No damage feller.")
                input("Would you like to roll again? Get me out or continue: ")
        elif dice_roll <= 7:
                print("It's a hit.")
                print("You did " + str(hit_point_value) + " damage " + "to a " + 
                random_creature + "!")
        elif dice_roll <=12:
                print("Critical hit!")
                print("You did " + str(hit_point_value_crit) + " damage " + "to a " + 
                random_creature + "!")
        else:
                print("Error")
    else:
        print("No die, ight cool.")
        updated_response = input("Are you sure? Get me out or continue? ")
        if updated_response == "continue" or updated_response == "Continue":
                return random_rpg()
        else:
                return None
random_rpg()
