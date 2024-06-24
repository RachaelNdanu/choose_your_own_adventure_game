name = input("What is your name? ")
print ("Welcome", name, "to this adventure!")

answer = input("You are on a dirty road, it has come to an end and you can go left or right.which way would you like to go? ").lower()

if answer == "left":
    answer = input("You came to a river , you can walk around it or swim across it. Type walk to walk around or swim to swim across it: ")
    if answer == "swim":
        print("You swam across and were eaten by an alligator")
    elif answer == "walk":
        print("you walked for many miles, ran out of water and lost the game")
    else:
        print('Not a valid point. You lose')


elif answer == "right":
    answer = input("You came to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back)? ")
    if answer == "back":
        print("You go back and then get hit by a bus and lose")
    elif answer == "cross":
        answer = input("You cross the bridge and meen a stranger.Do you talk to them (yes/no)?")
        if answer == "yes":
            print("You talk to the stranger, they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore stranger, sranger gets offended . You lose!")
        else:
             print('Not a valid point. You lose')

    else:
        print('Not a valid point. You lose')


else:
    print('Not a valid option. You lose')


print("Thank you for trying" , name)