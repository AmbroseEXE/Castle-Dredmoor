from os import system
from random import randint

gametitle="Escape from Castle Dredmoor"
system("mode 110,30")
system("title "+gametitle)

def cls():
    system('cls')
    
character_name = None
character_race = None
character_class = None
character_strength = None
character_dexterity = None
character_vitality = None
character_magic = None

cls()
print("Escape from Castle Dredmoor - an interactive adventure")

def Intro():
    print("")
    print("In this adventure, you are the leader of a mercenary company known as The Hollow Wolves, one of the finest group of adventurers in the Kingdom of Cassius. You and your crew received orders from the Adventurer's Guild to investigate and salvage the ruins of Castle Dredmoor. Eager to claim the would-be treasures of Castle Dredmoor, your compatriots went ahead of you to begin their search. However, it has been too long since you've heard from your party...")
    print("Your choices and skills will influence the outcome of this story.")
    print("")
    print("The evil wizard Malachus is holding your fellow adventurers captive as part of his dark ritual.")
    print("Do you have what it takes to save your friends from Castle Dredmoor?")
    print("")
    input("Press Enter to start...")
    
Intro()

def create_character():
    cls()
    global character_name
    character_name=input("""
    Let's begin by creating your character.
    What is your character name?

    >  """)
    global character_race
    while character_race is None:
        race_choice=input("""
        Choose your character race from the list below by entering the relevant number:
        1 - Elf
        2 - Dwarf
        3 - Human

        > """)
        if race_choice=="1":
            character_race="Elf"
        elif race_choice=="2":
            character_race="Dwarf"
        elif race_choice=="3":
            character_race="Human"
        else:
             print("Not a valid choice, try again")
    cls()
    global character_class
    while character_class is None:
        class_choice=input("""
        Choose your character class from the list below by entering the relevant number:
        1 - Warrior
        2 - Wizard
        3 - Rogue
        
        > """)
        if class_choice=="1":
            character_class="Warrior"
        elif class_choice=="2":
            character_class="Wizard"
        elif class_choice=="3":
            character_class="Rogue"
        else:
             print("Not a valid choice, try again")     
        
create_character()

def create_character_skill_sheet():
    cls()
    global character_name, character_class, character_race, character_strength, character_dexterity, character_vitality, character_magic
    print("""
    Now, Captain, let's see what you're made of shall we? You have four skills at your disposal, strength, dexterity, magic, and vitality.
    
    - Strength will be a factor in combat or any test that requires might.
    - Dexterity is an ability that will gauge your finesse and agility.
    - Magic stems from your pool of mana, enabling the ability to cast spells or inspect magical items.
    - Vitality is your life energy made manifest and each time you receive damage, your vitality dwindles. If your vitality reaches 0, it's game over.
    
    Depending on your race and class Captain, your stats will have already been provided for you. However, let's see if we can increase your skills with the roll of a die.
    
    Take a look at your base skills:
    """)
    character_strength=5
    character_magic=0
    character_dexterity=3
    character_vitality=10
    if character_race=="Elf":
        character_strength=character_strength+3
        character_magic=character_magic+6
        character_dexterity=character_dexterity+4
        character_vitality=character_vitality+2
    elif character_race=="Dwarf":
        character_strength=character_strength+5
        character_vitality=character_vitality+5
    elif character_race=="Human":
        character_strength=character_strength+1
        character_magic=character_magic+1
        character_dexterity=character_dexterity+1
        character_vitality=character_vitality+1
    if character_class=="Warrior":
        character_strength=character_strength+3
        character_vitality=character_vitality+3
    elif character_race=="Wizard":
        character_magic=character_magic+4
    elif character_class=="Rogue":
        character_dexterity=character_dexterity+4
    
    print("""
    Name:"""+character_name+
    """
    Race:"""+character_race+
    """
    Class:"""+character_class+
    """
    
    Strength:"""+str(character_strength)+
    """
    Dexterity:"""+str(character_dexterity)+
    """
    Magic:"""+str(character_magic)+
    """
    Vitality:"""+str(character_vitality)+"""
    
    """)
    input("Press Enter to continue.")
    
create_character_skill_sheet()

def modify_skills():
    cls()
    global character_strength, character_dexterity, character_vitality
    print("To modify your skills, roll a six-sided die for each of your skills, and the result will be applied to them")
    input("Press Enter to roll for Strength")
    roll=randint(1,6)
    print("You rolled: "+str(roll))
    character_strength = character_strength + roll
    input("Press Enter to roll for Dexterity")
    roll=randint(1,6)
    print("You rolled: "+str(roll))
    character_dexterity = character_dexterity + roll
    input("Press Enter to roll for Vitality")
    roll=randint(1,6)
    character_vitality = character_vitality + roll
    print("You rolled: "+str(roll))
    input("Press Enter to continue...")
    cls()
    print("""
    You're all set, Captain!
    Here are your results:

    Name:"""+character_name+
    """
    Race:"""+character_race+
    """
    Class:"""+character_class+
    """
    
    Strength:"""+str(character_strength)+
    """
    Dexterity:"""+str(character_dexterity)+
    """
    Magic:"""+str(character_magic)+
    """
    Vitality:"""+str(character_vitality)+"""

    """)
    input("Press Enter if you dare to start your mission...")

modify_skills()

def Scene_1():
    cls()
    choice = None  
    while choice is None:
        user_input=input("""
    You have entered the Castle Dungeons.. 
    It is dark, however thankfully your torch is lit and you can see up to 20 feet away from you.
    The stone walls are damp, the smell of rats and orcs is strong. 
    You walk down a narrow corridor, until you reach a thick stone wall.

    The corridor continues on the left, and on the right.

    What do you do?

    1 - Turn left
    2 - Turn right    
    > """)
        if user_input=="1" or user_input=="turn left":
            choice="1"
            Scene_2()
        elif user_input=="2" or user_input=="turn right":
            choice="2"
            Scene_3()
        else:
            print("""
            Not a valid choice, type a number or "turn left" / "turn right"
            """)

def Scene_2():
    cls()
    choice = None
    while choice is None:
        user_input=input("""
    From the darkness behind you.. you hear a strange noise.

    What do you do?

    1 - Continue walking
    2 - Stop to listen

    > """)
        if user_input=="1" or user_input=="continue":
            choice="1"
            combat()
        elif user_input=="2" or user_input=="stop":
            choice="2"
            skill_check()
        else:
            print("""
            Not a valid choice, type a number or "continue" / "stop"
            """)
            
def Scene_3():
    cls()
    choice = None
    while choice is None:
        user_input=input("""
    From the darkness ahead of you.. you hear a strange noise.

    What do you do?

    1 - Continue walking
    2 - Stop to listen

    > """)
        if user_input=="1" or user_input=="continue":
            choice="1"
            combat()
        elif user_input=="2" or user_input=="stop":
            choice="2"
            skill_check()
        else:
            print("""
            Not a valid choice, type a number or - "continue" / "stop"
            """)
            
def skill_check():
    cls()
    print("A giant rock falls from the ceiling, roll a die to see if you can dodge it.. or you will be crushed by it!")
    roll=randint(1,6)
    print("You rolled: "+str(roll))
    if roll+character_dexterity > 10:
        print ("""
        You dodge the stone and survive! Danger is not over though..
        The strange noise in the darkness continues, and it feels a lot closer now..""")
        input("Press Enter to continue...")
        combat()
    else:
        print("You are smashed by the rock.. You die. The game is over.")
        input("Press Enter to exit the game.")

def combat():
    cls()
    global character_vitality
    print("A horrible orc attacks you!")
    input("Press Enter to fight...")
    orc = [10, 14]
    while orc[1] > 0 or character_vitality > 0: 
        char_roll=randint(1,6)
        print("You rolled: "+str(char_roll))
        monst_roll=randint(1,6)
        print("The monster rolled: "+str(monst_roll))
        if char_roll+character_strength >= monst_roll+orc[0]:
            print("You hit the monster!")
            orc[1] = orc[1] - randint(1,6)
        else: 
            print("The monster hits you!")
            character_vitality = character_vitality - randint (1,6)
    if character_vitality > 0:
        print("You defeated the orc, congratulations!")
        input("Press Enter to exit the game")
    else:
        print("You died... and your friends will never be freed...")
        input("Press Enter to exit the game")



Scene_1()