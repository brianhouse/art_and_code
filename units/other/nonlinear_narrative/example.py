# assign starting values for global variables 
seen_ghost = False
has_key = False


def intro():
    global first_name
    print("Welcome to the house!")
    print("What is your name?")
    first_name = raw_input("> ")
    print("Nice to meet you, " + first_name)
    living_room()


def living_room():
    global first_name
    print("You are in the living room.")
    print("A passageway leads to the kitchen, and a door goes to the hallway.")
    print("What do you want to do, " + first_name + "?")
    response = raw_input("> ").lower()
    if "kitchen" in response or "passageway" in response:
        kitchen()
    elif "door" in response or "hallway" in response:
        hallway()
    else:
        print("You can't do that!")
        living_room()


def bedroom():
    global has_key
    print("You are in the bedroom.")
    print("A door leads back to the hallway.")
    print("There is a large locked chest of drawers here.")
    response = raw_input("> ").lower()
    if "hallway" in response:
        hallway()
    elif ("open" in response or "chest" in response or "drawers" in response) and has_key == False:
        print("You can't open the chest of drawers without a key.")
        bedroom()
    elif "chest" in response and has_key == True:
        chest()
    else:
        print("You can't do that!")
        bedroom()


def chest():
    global first_name
    print("You are looking in the chest of drawers.")
    print("Inside, a note says: \"I'm watching you, " + first_name + ".\"")
    print("You die of fright!")
    exit()  # ends the program


def hallway():
    print("You are in the hallway.")
    print("Doors lead to the bedroom, to the bathroom, and to the living room.")
    response = raw_input("> ").lower()
    if "bedroom" in response:
        bedroom()
    elif "bathroom" in response:
        bathroom()
    elif "living" in response:
        living_room()
    else:
        print("You can't do that!")
        hallway()


def bathroom():
    global has_key
    print("You are in the bathroom.")
    print("The only exit is to the hallway.")
    if has_key == False:
        print("There is a key here.")
    response = raw_input("> ").lower()
    if "hallway" in response:
        hallway()
    elif "key" in response:
        print("You take the key.")
        has_key = True
        bathroom()
    else:
        print("You can't do that!")
        bathroom()


def kitchen():
    global seen_ghost
    print("You are in the kitchen.")
    print("A passageway leads back to the living room.")
    if seen_ghost == False:
        print("There is a strange light glowing here and the faint image of an old man.")
        seen_ghost = True
    response = raw_input("> ").lower()
    if "living" in response:
        living_room()
    else:
        print("You can't do that!")
        kitchen()


intro()
