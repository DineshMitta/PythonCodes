
from getpass import getpass as get_input

exit = " "
while exit != "no":
    
    print("Epic battle of 🪨  📃  ✂️ ")
    print()
    print("Select your move (R, P or S)")

    P1_choice = get_input("Player 1 : ")
    P2_choice = get_input("Player 2 :")

    #P1_choice = input("Player 1 : ")
    #P2_choice = input("Player 2 :")

    if P1_choice in ("R", "r"):
        if P2_choice in ("R", "r"):
            print("________DRAW________")
            print("Oh You both chose Rock!!")
        elif P2_choice in ("P", "p"):
            print("!! Player 2 won !!")
            print("Player 2 wrapped the player 1 rock with paper")
        elif P2_choice in ("S", "s"):
            print("!! Plater 1 won !!")
            print("Player 2 Scissors got smashed by Player 1 Rocks")
        else:
            print("Invalid Choice!! By Player 2")

    elif P1_choice in ("P", "p"):
        if P2_choice in ("R", "r"):
            print("!! Player 1 won !!")
            print("Player 1 wrapped the player 2 rock with paper")
        elif P2_choice in ("P", "p"):
            print("________DRAW________")
            print("Oh You both chose Paper!!")
        elif P2_choice in ("S", "s"):
            print("!! Player 2 won !!")
            print("Player 1 Paper is cut into pieces by Player 2 Scissors")
        else:
            print("Invalid Choice!! By Player 2")

    elif P1_choice in ("S", "s"):
        if P2_choice in ("R", "r"):
            print("!! Player 2 won !!")
            print("Player 1 Scissors got smashed by Player 2 Rocks")
        elif P2_choice in ("P", "p"):
            print("!! Player 1 won !!")
            print("Player 2 Paper is cut into pieces by Player 1 Scissors")
        elif P2_choice in ("S", "s"):
            print("________DRAW________")
            print("Oh You both chose Scissors!!")
        else:
            print("Invalid Choice!! By Player 2")
    
    else:
        print("Invalid Choice!! By Player 1")


    exit = input("Play : ")
    print()