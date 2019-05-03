import time


playerResponse = ""

def talkBoy():
    global playerResponse

    print("The boy greets you.")
    print("\"Greetings adventurer, my name is Kalesius. Why have you come to this cursed town?\"")
    time.sleep(1)
    print("""    A. To atone for my sins and slay the beast that dwells near here.
    B. Mind your business you insignificant urchin! 
    C. To find any knowledge of how to defeat the lion that plagues Nemea. 
            """)
    playerResponse = input("> ")

    if playerResponse.lower() == "a":
        option_atone()
    elif playerResponse.lower() == "b":
        option_insult()
    elif playerResponse.lower() == "c":
        option_knowledge()
    else:
        print("Use only A, B, or C")
        talkBoy()

# Option A
def option_atone():
    global playerResponse

    print("\"What sins have you committed to face such a task! No man who has sought the Nemean "
          "\nLion has come back to claim victory. Surely whoever sends you intends only that you "
          "\nmeet your death.\" ")
    time.sleep(1)
    print("""    A. These are no concerns of yours. Tell me where I may face this lion.
    B. Sins that will be bound to my soul for the rest of my life. If death is to greet me today
       then I welcome it with open arms. 
    C. King Eurystheus is a pawn of Hera. As the son of Zeus, I will not be bested by such a man.
    
    """)
    playerResponse = input("> ")

    if playerResponse.lower() == "a":
        option_lionLair()
    elif playerResponse.lower() == "b":
        option_somber()
    elif playerResponse.lower() == "c":
        option_fountain()
    else:
        print("Use only A, B, or C")
        option_atone()

# Option AA
def option_lionLair():
    print("Taken back by the harshness of your words. The boy points meagerly to the east.\n")
    print("\"The....the lion lives....in a cave....to...to the East.\"")

# Option AB
def option_somber():
    print("Taken back by the sadness of your words. The boy points meagerly to the east.\n")
    print("\"The....the lion lives....in a cave....to...to the East. But before you go, there"
          "\nare some arrows to the South-East, past an old olive tree. If you find a bow maybe "
          "\nyou can combine them and it'll help you on your quest on your quest!\"")

# Option AC and CA
def option_fountain():
    print("Taken back by the conviction and strength of your words. The boy points to the east.\n")
    print("\"The lion dwells in a cave to the East! A child of Zeus will easily be able to slay the "
          "\nbeast! Before you go, if you find a coin you can make an offering to your father for strength"
          "\nand favor at the fountain South of here!\"")

# Option B
def option_insult():
    print("With tears in his eyes, the boy backs away from you.")

# Option C
def option_knowledge():
    global playerResponse

    print("\"Oh, I know a lot about the Nemean Lion, many adventurers who try to face it brag about the"
          "\nsecrets they've discovered about it. What makes you think you can kill the monstrosity?\"")
    time.sleep(1)
    print("""    A. Zeus is my father. Failure is something I've never known.
    B. All I need is  weapon to kill the beast.
    C. If I can trap the monster, then I am sure that I can kill it.
    
    """)
    playerResponse = input("> ")

    if playerResponse.lower() == "a":
        option_fountain()
    elif playerResponse.lower() == "b":
        option_tree()
    elif playerResponse.lower() == "c":
        option_boulder()
    else:
        print("Use only A, B, or C")
        option_knowledge()

# Option CB
def option_tree():
    print("The boy thinks for a moment before giving his response")
    print("\"No one in town would part with their weapon and we don't have a blacksmith like bigger "
          "\ntowns. But maybe if you found a mighty tree you could use that as a club?\"")

# Option CC
def option_boulder():
    print("The boy thinks for a moment before giving his response")
    print("\"No adventurer has thought of trapping the lion before. They did say that there are two"
          "\nentrances to its lair however. Maybe if you find a rock big enough to cover one entrance"
          "\nyou could fight it in the cave?\"")
