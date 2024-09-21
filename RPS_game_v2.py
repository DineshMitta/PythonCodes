from getpass import getpass as get_input

p1_points, p2_points,rounds = 0 , 0, 0
while True :

 
    if p1_points == 2 and p2_points != 2:
        print("____________________",end="")
        print("!! Plater 1 won !!",end="")
        print("____________________")
        exit()
    
    if p2_points == 2 and p1_points != 2:
        print("____________________",end="")
        print("!! Plater 2 won !!",end="")
        print("____________________")
        exit()
    elif p1_points == 2 and  p2_points == 2 :
        print("_____________________________",end="")
        print("both got 2 points its a draw",end="")
        print("_____________________________")
        exit()
    
    
    if rounds ==  3:
        print(p1_points, p2_points)
        exit()

    print()
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
            p1_points+=1
            p2_points+=1
        elif P2_choice in ("P", "p"):
            print("!! Player 2 won !!")
            print("Player 2 wrapped the player 1 rock with paper")
            p2_points+=1
        elif P2_choice in ("S", "s"):
            print("!! Plater 1 won !!")
            print("Player 2 Scissors got smashed by Player 1 Rocks")
            p1_points+=1
        else:
            print("Invalid Choice!! By Player 2")

    elif P1_choice in ("P", "p"):
        if P2_choice in ("R", "r"):
            print("!! Player 1 won !!")
            print("Player 1 wrapped the player 2 rock with paper")
            p1_points+=1
        elif P2_choice in ("P", "p"):
            print("________DRAW________")
            print("Oh You both chose Paper!!")
            p1_points+=1
            p2_points+=1
        elif P2_choice in ("S", "s"):
            print("!! Player 2 won !!")
            print("Player 1 Paper is cut into pieces by Player 2 Scissors")
            p2_points+=1
        else:
            print("Invalid Choice!! By Player 2")

    elif P1_choice in ("S", "s"):
        if P2_choice in ("R", "r"):
            print("!! Player 2 won !!")
            print("Player 1 Scissors got smashed by Player 2 Rocks")
            p2_points+=1
        elif P2_choice in ("P", "p"):
            print("!! Player 1 won !!")
            print("Player 2 Paper is cut into pieces by Player 1 Scissors")
            p1_points+=1
        elif P2_choice in ("S", "s"):
            print("________DRAW________")
            print("Oh You both chose Scissors!!")
            p1_points+=1
            p2_points+=1
        else:
            print("Invalid Choice!! By Player 2")
    else:
        print("Invalid Choice!! By Player 1")
    rounds += 1

 

