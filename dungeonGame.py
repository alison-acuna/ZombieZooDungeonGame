
def instructions():
    print("Welcome to the Zoo.  An infection has spread rapidly through the Zoo,"
    + " affecting all the animals.  The goal of this game is to get out of the"
    + " Zoo as quickly as possible.  Each choice you make will take you into "
    + "another section of the Zoo.  Explore that section of the Zoo and then "
    + "chose a direction to go next.  The player who escapes the Zoo by "
    + "exploring the least number of rooms wins.")
    print()

def help():
    print("To walk forward, press 'F'.  To walk into the room to the left, press "
    + " 'L'.  To walk into the room to the right, press 'R'.  To return to the "
    + "previous room, press 'B'.")
    print()

#
def decision(item):
    while True:
        try:
            user_input = input("Where would you like to go? ").lower()
            choice = item[user_input]
            if choice == "polar_bear_room":
#                print("polar")
                polar_bear_room()
            elif choice == "sun_bear_room":
#                print("sun")
                sun_bear_room()
            elif choice == "penguin_room":
#                print("penguin")
                penguin_room()
            elif choice == "monkey_room":
#                print("monkey")
                monkey_room()
            elif choice == "elephant_room":
                elephant_room()
            elif choice == "zoo_exit":
                zoo_exit()
        except:
            print("That is not a valid entry. Please try again.")

def penguin_room():
    print(
    "You are in the penguin enclosure. Penguins swim the thier tank but "
    + "something isn't right.  Their eyes are bloodshot and they are twitching "
    + "strangely.  Signs indipycate that there is a Polar Bear exhibit in front "
    + "of you and a Malaysian Sun Bear exhibit behind you.  There are no "
    + "exhibits to the left or right.")
    directions_dictionary_penguin = {
        "f" : "polar_bear_room",
        "b" : "sun_bear_room"
        }
    user_input = decision(directions_dictionary_penguin)

def polar_bear_room():
    print(
    "You enter the polar bear room.  A large paw swipes through a hole in the "
    + "glass towards your head.  You duck and start running. Run forward, back, "
    + "or to the right")
    directions_dictionary_polar = {
        "f" : "elephant_room",
        "b" : "penguin_room",
        "r" : "monkey_room"
    }
    user_input = decision(directions_dictionary_polar)

def elephant_room():
    print(
        "You run up a winding path and over an empty pen.  Ahead, there is a "
        + "large building.  You enter and look down apitheatre seating at a pen. "
        + "Five large elephants are beating their trunks bloody against the walls "
        + "of the pen.  Their eyes are wide and bloodshot and their flesh is "
        + "starting to rot and fall off. Run back?"
    )
    directions_dictionary_elephant ={
        "b" : "polar_bear_room"
    }
    user_input = decision(directions_dictionary_elephant)

def monkey_room():
    print(
    "You enter the moneky pen and the monkeys begin to shuffle towards you. "
    + "Run back to the penguin exhibit or forward?"
    )
    directions_dictionary_monkey ={
        "b" : "polar_bear_room",
        "f" : "zoo_exit"
    }
    user_input = decision(directions_dictionary_monkey)

def sun_bear_room():
    print(
    "You can't see any bears in this exhibit.  You do hear shuffling and moaning "
    + "in the background.  Run forward or back to the penguin exhibit? "
    )
    directions_dictionary_sun_bear ={
        "b" : "penguin_room",
        "f" : "zoo_exit"
    }
    user_input = decision(directions_dictionary_sun_bear)

def zoo_exit():
    print(
    "You found the exit!  Congratulations.  Exit the zoo"
    )
#    user_input = decision(directions_dictionary_exit)



instructions()
help()
penguin_room()
