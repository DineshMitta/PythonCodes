while True :

    print("wher do u want to go : ")
    direction = input("> ")

    if direction == "left":
        print("aww u feel into a trap")
        break
    elif direction == "right":
        continue
    else:
        print("yay u won the game")
        exit()
print("the game is over u failed ")