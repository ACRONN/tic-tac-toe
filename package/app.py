

def userinput(array):
    turn = 1
    score = ["O","X"]
    current_player = "a"
    while True:
        current_player = score[turn%2]
        uinput = input("Player "+ str(turn%2)+ " enter your move 'row collumn'")
        row = uinput.split()[0]
        collumn =uinput.split()[1]
        array[int(row)][int(collumn)] = current_player
        turn +=1
        for i in range(len(array)):
            print(array[i])

