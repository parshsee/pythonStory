from adventurelib import *
import dialogs
import time
import adventurelib

print("""
    **********************************************
    |           The Labors of Hercules           |
    |           By: Parshotan Seenanan           |
    |                                            |
    |          O                                 |
    |       ,-.|____________________             |
    |    O==+-|(>-------- --  -     .>           |
    |       `- |\"\"\"\"\"d88b\"\"\"\"\"\"\"\"\"\"\"             |
    |        | O     d8P 88b                     |
    |        |  \    88= ,=88                    |
    |        |   )   9b _. 88b                   |
    |        `._ `.   8`--'888                   |
    |         |    \--'\   `-8___                |
    |          \`-.              \\               |
    |           `. \ -       _ / <               |
    |             \ `---   ___/|_-\              |
    |              |._      _. |_-|              |
    |              \  _     _  /.-\              |
    |               | -! . !- ||   |             | 
    |               \ "| ! |" /\   |             |
    |                =oO)X(Oo=  \  /             |
    |                888888888   < \\             |
    |               d888888888b  \_/             |
    |               88888888888                  |
    **********************************************
""")                             


Room.items = Bag()

# Setting each Room
current_Room = startRoom = Room("""
    You stand at the end of a dirt road.
""")

startRoomNorth = startRoom.north = Room("""
    You are in a beautiful field.  
""")

startRoomSouth = startRoom.south = Room("""
    You are in a field of flowers.
""")

treeRoom = startRoom.east = Room("""
    You stand on top a small hill.
""")

villagerRoom = startRoom.west = Room("""
    You are in a lush forest. There is a small whimpering coming from somewhere.
""")

treeRoomSouth = treeRoom.south = Room("""
    You stand by a vast valley.
""")

deadMenRoom = treeRoom.north = Room ("""
    The stench of the dead fill your nose. Piles of rotting bodies are strewn about everywhere.
""")

fountainRoom = villagerRoom.south = Room("""
    You stand by a majestic fountain. At the top of it lies a silver lightning bolt.
""")

bowRoom = villagerRoom.north = Room("""
    You are in a small clearing. There is sits a body, brutally mauled, at the base of a tree.
""")

cityRoom = bowRoom.north = Room("""
    You are at the entrance to the small town of Cleonae. A boy stands idly by near the gate. 
""")

clawRoom = startRoomNorth.north = Room("""
    You are at what remains of a forest. There are broken branches and claw marks everywhere.
""")

deadMenRoomNorth = deadMenRoom.north = Room("""
    You are in a field covered with blood. A great war was once fought here.
""")

caveEntranceTop = deadMenRoomNorth.east = Room("""
    You stand at the crevice of a mountain.
    There is an opening to the south.
""")

caveEntranceBottom = treeRoom.east = Room("""
    You stand at the crevice of a mountain.
    There is an opening to the north.
""")

arrowRoom = caveEntranceBottom.south = Room("""
    You stand by a tree with several arrows in it. A man is hunched over beside it.
""")

lairRoom = caveEntranceBottom.north = caveEntranceTop.south = Room("""
    In the dimly lit cave, you hear ominous growling coming from behind you.
""")

fountainRoom.east = startRoomSouth
startRoomSouth.east = treeRoomSouth
treeRoomSouth.east = arrowRoom
bowRoom.east = startRoomNorth
startRoomNorth.east = deadMenRoom
cityRoom.east = clawRoom
clawRoom.east = deadMenRoomNorth

# Setting items and their locations
coin = Item('silver coin', 'coin')
bow = Item('well-worn bow', 'bow')
boulder = Item('boulder', 'gigantic boulder', 'rock')
treeLog = Item('olive tree trunk', 'log', 'mighty old olive tree', 'tree', 'trunk')
arrows = Item('bundle of arrows', 'arrows', 'bundle')
bowAndArrow = Item('bow and arrows', 'bow', 'arrows', 'arrow')

cityRoom.items = Bag({coin})
bowRoom.items = Bag({bow})
deadMenRoomNorth.items = Bag({boulder})
treeRoom.items = Bag({treeLog})
arrowRoom.items = Bag({arrows})

inventory = Bag()

name = ""
counter = 0
playerStrength = False
tigerStun = False
playerResponse = ""

while name.lower() != "Hercules".lower():
    if counter == 1:
        print("The son of Zeus would not have such a pathetic name!")
        name = input("Enter your name: ")
    else:
        name = input("Enter your name: ")
        counter = 1

print("To atone for the murder of your wife and children. You have been tasked by the Oracle"
      "\nof Delphi to pay your penance by serving under King Eurystheus. "
      "\nHis first task is to slay the Nemean Lion."
      "\nType 'help' or '?' to see a list a commands at anypoint in the adventure. \n")

@when('describe area')
def look():
    say(current_Room)
    if current_Room.items:
        for i in current_Room.items:
            say('A %s is here.' % i)
    else:
        say('There are no items here.')
    #print(current_Room.exits())


@when('go north', direction='north')
@when('go south', direction='south')
@when('go east', direction='east')
@when('go west', direction='west')
# @when('go north', direction='north')
# @when('go south', direction='south')
# @when('go east', direction='east')
# @when('go west', direction='west')
# @when('head north', direction='north')
# @when('head south', direction='south')
# @when('head east', direction='east')
# @when('head west', direction='west')
def go(direction):
    global current_Room, bowAndArrow
    room = current_Room.exit(direction)
    if room:
        current_Room = room
        print(f'You go {direction}.')
        look()
        if room == lairRoom:
            lionBattle()
    else:
        print("You cannot go that way.")

    if inventory.find("bow") and inventory.find("arrows"):
        inventory.take("bow")
        inventory.take("arrows")
        inventory.add(bowAndArrow)

@when('grab ITEM')
@when('pick up ITEM')
@when('take ITEM')
def take(item):
    obj = current_Room.items.take(item)
    if obj:
        say('You pick up the %s.' % obj)
        inventory.add(obj)
    else:
        say('There is no %s here.' % item)

@when('place ITEM in LOCATION')
@when('put ITEM in LOCATION')
@when('drop ITEM in LOCATION')
@when('throw ITEM in LOCATION')
@when('toss ITEM in LOCATION')
@when('place ITEM at LOCATION')
@when('put ITEM at LOCATION')
@when('drop ITEM at LOCATION')
def dropInto(item, location):
    global current_Room, fountainRoom, lairRoom, caveEntranceBottom, caveEntranceTop, playerStrength

    obj = inventory.take(item)
    if not obj:
        say('You do not have a %s.' % item)
    else:
        # If the player is in the fountain room and drops the coin in the fountain, give him strength
        if current_Room == fountainRoom and obj == coin and location.lower() == "fountain".lower():
            say('You dropped the %s in the fountain.' % obj)
            print("A bolt of lightning strikes the fountain and crackles outward, scorching the grass " 
                "\naround it. The air feels electric and you feel imbued with power.")
            playerStrength = True

        # If the playe is at either cave entrance and places the boulder at the entrance, block the entrance
        elif (current_Room == caveEntranceTop or current_Room == caveEntranceBottom) and obj == boulder and (location.lower() == "cave entrance".lower() or location.lower() == "entrance".lower()):
            say('You placed the %s at the cave entrance.' % obj)

            # If he's at the top, change lair to not have a north exit and change the top to not have a south entrance, update the current room
            if current_Room == caveEntranceTop:
                lairRoom = caveEntranceBottom.north = Room("""
                    In the dimly lit cave, you hear ominous growling.
                """)

                caveEntranceTop = deadMenRoomNorth.east = Room("""
                    You stand at the crevice of a mountain.
                    A boulder blocks the entrance.
                """)

                current_Room = caveEntranceTop

            # If he's at the bottom, change lair to not have a south exit and change the bottom to not have a north entrance, update the current room
            elif current_Room == caveEntranceBottom:
                lairRoom = caveEntranceTop.south = Room("""
                    In the dimly lit cave, you hear ominous growling.
                """)

                caveEntranceBottom = treeRoom.east = arrowRoom.north = Room("""
                    You stand at the crevice of a mountain.
                    A boulder blocks the entrance.
                """)

                current_Room = caveEntranceBottom
        else:
            say('You cannot do that.')
            inventory.add(item)

@when('inventory')
def show_inventory():
    say('You have:')
    for thing in inventory:
        say(thing)

@when('talk to boy')
@when('talk to child')
@when('talk to kid')
def talkToBoy():
    global current_Room

    if current_Room == cityRoom:
        dialogs.talkBoy()
        print("\nYou can talk to the boy multiple times by interacting with him again.")
    else:
        print("There is no kid here")

def lionBattle():
    global playerResponse

    print("As your eyes adjust to the darkness the lion pounces, pinning you to the ground."
          "\nWith a one swift motion, you kick the lion back and get on your feet. The lion"
          "\nnow stands between you and the exit.\n")
    time.sleep(1.5)
    print(" ----------------------------  Battle Mode --------------------------------")
    print("         Attack                                          Run               ")
    playerResponse = input("> ")

    if playerResponse.lower() == "Attack".lower():
        attack()
    elif playerResponse.lower() == "Run".lower():
        say("The Son of Zeus will never run from a challenge!\n")
        time.sleep(1)
        lionBattle()

def attack():
    global counter, playerResponse

    #items = ['olive tree trunk', 'log', 'mighty old olive tree', 'tree', 'trunk', 'bow and arrows', 'bow', 'arrows', 'arrow']

    print("Attack with: ")

    for item in inventory:
        if str(item) == "olive tree trunk" or str(item) == "bow and arrows":
            print(str(counter) + ". " + str(item))
            counter += 1
    print(str(counter) + ". Fist")
    counter = 1
    playerResponse = input("> ")

    #playerResponse.lower() in items
    if inventory.find(playerResponse) or playerResponse.lower() == "Fist".lower():
        if inventory.find(playerResponse) == arrows:
            print("You have no bow to use it with")
            attack()
        elif inventory.find(playerResponse) == bow:
            print("You have no arrows")
            attack()
        elif inventory.find(playerResponse) == boulder or inventory.find(playerResponse) == coin:
            print("That is not a valid choice. Please type a chosen item name.")
            attack()
        else:
            attackWithItemOne(playerResponse)
    else:
        print("That is not a valid choice. Please type the item name.")
        time.sleep(1)
        attack()

def attackWithItemOne(itemName):
    global tigerStun, playerStrength

    obj = inventory.take(itemName)
    #print(obj)

    # Attack with bow and arrow --- Fail
    if obj == bowAndArrow:
        print("You ready the bow and let loose several terrifying shots right at the beast."
              "\nThe arrows bounce off the lions hide and clatters to the ground around it."
              "\nWhile you are suprised, it uses the opportunity to attack and its claws rip"
              "\nthrough your throat.")
        print("As you start to lose consciousness, you think maybe you should read up on the "
              "\nNemean Lion")
        quit()
    # Attack with tree trunk --- Succeed
    elif obj == treeLog:
        print("With a heavy swing you smash the tree trunk into the face of the lion."
              "\nIt stumbles around, clearly dazed from your strike")
        tigerStun = True
        attackAgain()
    # Attack with Fist --- Not Stunned --- Fail
    else:
        if not playerStrength:
            print("You charge at the lion and ready yourself to deliver a mighty blow. However as"
                  "\nyou are about to throw the punch, the lion leaps overheaded and claws at your"
                  "\nface. A chunk of flesh from your chin to hair is ripped off as you collapse to"
                  "\nthe ground. With your last thoughts, you think punching wasn't your best idea.")
            quit()
        else:
            print("You charge at the lion and ready yourself to deliver a mighty blow, knowing that the "
                  "power and favor of Zeus courses through your veins. However as you are about to throw "
                  "\nthe punch, the lion leaps overheaded and claws at your face. A chunk of flesh from "
                  "\nyour chin to hair is ripped off as you collapse to the ground. With your last thoughts, "
                  "\nyou think punching wasn't your best idea.")
            quit()

def attackAgain():
    global counter, playerResponse

    print("You use this opportunity to strike again.")
    print("Attack with: ")

    for item in inventory:
        if str(item) == "bow and arrows":
            print(str(counter) + ". " + str(item))
            counter += 1
    print(str(counter) + ". Fist")
    counter = 1
    playerResponse = input("> ")

    # playerResponse.lower() in items
    if inventory.find(playerResponse) or playerResponse.lower() == "Fist".lower():
        if inventory.find(playerResponse) == arrows:
            print("You have no bow to use it with")
            attackAgain()
        elif inventory.find(playerResponse) == bow:
            print("You have no arrows")
            attackAgain()
        elif inventory.find(playerResponse) == boulder or inventory.find(playerResponse) == coin:
            print("That is not a valid choice. Please type a chosen item name.")
            attackAgain()
        else:
            attackWithItemTwo(playerResponse)
    else:
        print("That is not a valid choice. Please type the item name.")
        time.sleep(1)
        attack()

def attackWithItemTwo(itemName):
    global playerStrength

    obj = inventory.take(itemName)

    if obj == bowAndArrow:
        print("You ready the bow and let loose several terrifying shots right at the beast."
              "\nThe arrows bounce off the lions hide and clatters to the ground around it."
              "\nWhile you are suprised, it uses the opportunity to attack and its claws rip"
              "\nthrough your throat.")
        print("As you start to lose consciousness, you think maybe you should read up on the "
              "\nNemean Lion")
        quit()
    else:
        if not playerStrength:
            print("You charge the animal while it is still dazed and let loose a fury of blows. "
                  "\nHowever each hit fails to hurt the creature as regains its senses and looks "
                  "\nyou in the eye. Before you are ripped apart, you think that if you had had the"
                  "\nstrength and favor of Zeus, you would've easily killed it.")
            quit()
        else:
            print("You leap atop the beast while it is still dazed and smash its head downward. After"
                  "\nseveral more blows, you wrap your arms around its neck and begin to squeeze the"
                  "\nlife out of your once terrifying foe. With a strong pull, you hear a resounding"
                  "\ncrack as the animal lays limb beneath you. \n")
            time.sleep(2)
            victoryMessage()

def victoryMessage():
    print("You have successfully completed Labor 1 of Hercules 12 Labors!")
    print("""
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"\"\"\"\"\"\"`
    """)

def no_command_matches(command):
    """Called when a command is not understood."""
    print("I don't understand '%s'. Try typing 'help' or '?' for a list of available commands.\n"
          "Remember, they must be typed exactly like it is shown, with capitalized words replaced \n"
          "with the respective names. " % command)

adventurelib.no_command_matches = no_command_matches

look()
start()
