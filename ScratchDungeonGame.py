
def zoo_exit():
    print(
    "You found the exit!  Congratulations.  Exit the zoo"
    )

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
            except ValueError:
                    print("That is not a valid entry. Please try again.")

sun_bear_room()
