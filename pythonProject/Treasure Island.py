#prints header
print("Welcome to Treasure Island\n")
print("Your mission is to find the treasure\n")
print("You are at a cross road. Where do you want to go?")
#stores input for first "if" block
way1 = input("Type 'left' or 'right'")
if way1 == "left":
    print("You have come to a lake. There is an island in the middle of the lake.\n")
    #stores second input in second "if block"
    lake = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    if lake == "wait":
        print("You arrive at the island unharmed.\n")
        colour = input("There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        if colour == "red":
            print("Burned by fire. Game over")
        elif colour == "blue":
            print("Eaten by beasts")
        elif colour == "yellow":
            print("You win")
    else:
        print("Attacked by trout. Game over")
else:
    print("fall into a hole. game over")


