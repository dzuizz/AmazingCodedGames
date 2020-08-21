import time
import random
import pygame
# shop can only be opened in pygame

def time_pause(string):
    print(string)
    time.sleep(1)

def use(this):
    if this in valuables:
        for key, value in valuables.items:
            if key == this:
                value = True
            else:
                value = False
    else:
        valuables[this]= weapons.get(this)

def game():
    time_pause("Welcome to AdventureLand!")
    time_pause("Explore the nation, get weapons and money, and even buy weapons!")

    while True:
        time_pause("In front of you is a house.")
        time_pause("On your right is a dark cave.")
        time_pause("On your left is a factory.")
        time_pause("Behind you is a pathway.")
        time_pause("In your hand, you hold your trusty, but not very effective dagger")
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
            time_pause("He asked")
        elif ans == 2:
            time_pause("")
        elif ans == 3:
            time_pause("")
        elif ans == 4:
            time_pause("")

# shop weapons = {name: [boolean, [strength, price]]}
# weapons = {name: [boolean, strength]} and armor
shopWeapons = {

    "oldDagger": [True, [10, 0]],
    "enchantedDagger": [False, [25, 25]],
    "kunaiKnife": [False, [50, 75]],
    "ironSword": [False, [100, 100]],
    "goldSword": [False, [250, 210]],
    "diamondSword": [False, [500, 500]],
    "enchantedDiamondSword": [False, [100000, 10000]],
    }
weapons = {

    "swordOfOgoroth": [False, 1200]
    }

# shop armors = {name : [boolean, [armor, price]]}
shopArmorsUse = {
    "bronzeTunicOfImminentWarlords" : [True, [10, 0]],
    "bronzeVestOfBlessedLands" : [False, [25, 25]],
    "batteplateOfFadedKings" : [False, [50, 100]],
    "greatPlateOfDistantBloodlust" : [False, [100, 1000]],
    "thunderForgedChainArmor" : [False, [250, 5000]],
    "engravedChestguardOfInception" : [False, [500, 10000]],
    "mjolnirPoweredAssaultArmor" : [False, [1000, 100000]]

    }
enemy_hp = 0
hp = 100
money = 100
armorHp = 0
strength = 10
valuables = {}
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
