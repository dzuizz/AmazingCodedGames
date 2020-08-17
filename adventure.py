import time
import random
import pygame
# shop can only be opened in pygame

def time_pause(string):
    print(string)
    time.sleep(1)

def use(this):
    if this in shopWeapons:
        for i in range()

def game():
    time_pause("Welcome to AdventureLand!")
    time_pause("Explore the nation, get weapons and money, and even buy weapons!")
    while True:
        time_pause("In front of you is a house.")
        time_pause("On your right is a dark cave.")
        time_pause("On your left is a factory.")
        time_pause("Behind you is a pathway.")
        time_pause("In your hand, you hold")
        print("House - 1")
        print("Cave - 2")
        print("Factory - 3")
        print("Pathway - 4")
        ans = int(input("where do you choose to go?"))
        while ans not in options:
            ans = int(input("where do you choose to go?"))
        if ans == 1:
            time_pause("You head cautiously towards the house...")
            time_pause("You open the door.")
            time_pause("An old man appeared out of the house.")
            time_pause("You introduced yourself and the man gave you a room to aid throughout your journey!")
        elif ans == 2:
            time_pause("")
        elif ans == 3:
            time_pause("")
        elif ans == 4:
            time_pause("")

# shop weapons = [strength, price]
old_dagger = [10, 0]
enchanted_dagger = [25, 25]
kunai_knife = [50, 1000]
iron_sword = [100, 5700]
gold_sword = [250, 10000]
diamond_sword = [500, 100000]
enchanted_diamond_sword = [1000, 123456789]
shopWeaponsUse = {

    "old_dagger" : True,
    "enchanted_dagger" : False,
    "kunai_knife" : False,
    "iron_sword" : False,
    "gold_sword" : False,
    "diamond_sword" : False,
    "enchanted_diamond_sword" : False

    }
shopWeapons = [
    old_dagger,
    enchanted_dagger,
    kunai_knife,
    iron_sword,
    gold_sword,
    diamond_sword,
    enchanted_diamond_sword
    ]

# shop armors = [armor, price]
bronzeTunicOfImminentWarlords = [10, 0]
bronzeVestOfBlessedLands = [25, 25]
batteplateOfFadedKings = [50, 100]
greatPlateOfDistantBloodlust = [100, 1000]
thunderForgedChainArmor = [250, 5000]
engravedChestguardOfInception = [500, 10000]
mjolnirPoweredAssaultArmor =[1000, 100000]
shopArmors = [

    bronzeTunicOfImminentWarlords,
    bronzeVestOfBlessedLands,
    batteplateOfFadedKings,
    greatPlateOfDistantBloodlust,
    thunderForgedChainArmor,
    engravedChestguardOfInception,
    mjolnirPoweredAssaultArmor

    ]

# superpowers (can only be gotten, not bought)


enemy_hp = 0
hp = 100
money = 100
armorHp = 0
strength = 10
valuables = []
options = [1, 2, 3, 4]

# main code
#pygame.init()

#display_width = 800
#display_height = 600

#gameDisplay = pygame.display.set_mode((800, 600))
#pygame.display.set_caption('AdventureLand')

#black = (0, 0, 0)
#white = (255, 255, 255)

#clock = pygame.time.Clock()


game()
