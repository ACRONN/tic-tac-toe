def game(array):
    turn = 1
    score = ["O","X"]
    current_player = ""
    win = False
    while win is False:
        current_player = score[turn%2]
        while True:
            try:
                if turn % 2 == 0:
                    uinput = input("Player "+ str((turn % 2) + 2)+ " enter your move ('row column'): ")
                else:
                    uinput = input("Player "+ str(turn % 2)+ " enter your move ('row column'): ")
                row = uinput.split()[0]
                column = uinput.split()[1]
                array[int(row)][int(column)] = current_player
                break
            except IndexError:
                print("Invalid coordinates.\n")
                continue

        # Need to implement win condition.

        turn += 1
        for i in range(len(array)):
            print(array[i])

def createArray(rows,cols):
    arr = [["-" for i in range(cols)] for j in range(rows)]
    return arr

game(createArray(3,3))