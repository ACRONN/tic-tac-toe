class TicTacToe():
    def __init__(self):
        self.maxRow = 2
        self.maxColumn = 2
    def computerGame(self, array):
        pass
    def localGame(self, array):
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
                        if int(row) > self.maxRow or int(column) > self.maxColumn:
                            print("Invalid coordinates. Range cannot exceed 2 2.\n")
                            continue
                        break
                    if array[int(row)][int(column)] != "X" or array[int(row)][int(column)] != "O":
                        array[int(row)][int(column)] = current_player
                    else:
                        print("Coordinate already played.\n")
                        continue
                    break
                except IndexError:
                    print("Invalid coordinates. Please enter two integers separated by a space.\n")
                    continue

            # Need to implement win condition.

            turn += 1
            for i in range(len(array)):
                print(array[i])

    def createArray(self, rows, cols):
        arr = [["-" for i in range(cols)] for j in range(rows)]
        return arr
