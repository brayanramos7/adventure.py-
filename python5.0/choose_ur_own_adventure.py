name = input("Type your name: ")
print ("Welcome",  name, "to the adventure!")

answer  = input ("You are on a dark road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input ("You come to a lake. There is an island in the middle of the lake. Type wait to wait for a boat. Type swim to swim across. ").lower()

    if answer  == "wait":
        print("You waited for the boat and it did not come. Game over!")
    
    elif answer == "swim":
        print("You swam across and were eaten by an alligator. Game over!")

    else:
        print ("Not a valid option. Game over!")

elif answer == "right":
    answer = input ("You come to a house. There is a door to the front and a door to the back. Which door would you like to go through (front/back)? ").lower()

    if answer == "front":
        print ("You were killed by a fungus zombie who was waiting for you. Game over!")
    elif answer == "back":
        answer = input("A random person saved yuo. Do you talk to them (yes/no)? ").lower()

        if answer == "yes":
            print ("Well done that person will help you to make it alive. GOOD LUCK!")
        elif answer == "no":
            print("You should have talked to  them now you will die alone. GAME OVER!")
    else :
        print ("Not a valid option. Game over!")
else:
    print ("Not a valid option. Game over!")

print ("Thanks for playing", name, "!")



