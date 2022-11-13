maxRow = 2
maxColumn = 2

def computerGame(array):
    pass

def localGame(array):
    turn = 1
    score = ["O","X"]
    current_player = ""
    win = False
    while win is False:
        current_player = score[turn%2]
        while True:
            try:
                while True:
                    if turn % 2 == 0:
                        uinput = input("Player "+ str((turn % 2) + 2)+ " enter your move ('row column'): ")
                    else:
                        uinput = input("Player "+ str(turn % 2)+ " enter your move ('row column'): ")
                    row = uinput.split()[0]
                    column = uinput.split()[1]
                    if int(row) > maxRow or int(column) > maxColumn:
                        print("Invalid coordinates. Range cannot exceed 2 2.\n")
                        continue
                    break
                array[int(row)][int(column)] = current_player
                break
            except IndexError:
                print("Invalid coordinates. Please enter two integers separated by a space.\n")
                continue

        # Need to implement win condition.

        turn += 1
        for i in range(len(array)):
            print(array[i])

def createArray(rows,cols):
    arr = [["-" for i in range(cols)] for j in range(rows)]
    return arr

def run():
    while True:
        gameMode = input("\n[1] Computer\n[2] Two-Player\n\nEnter game mode to play: ")
        if gameMode == "1":
            computerGame(createArray(3,3))
        elif gameMode == "2":
            localGame(createArray(3,3))
        else:
            print("Please enter a valid game mode.\n")
            continue
        break
