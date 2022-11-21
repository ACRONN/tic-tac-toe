class App():
    def run(self):
        import package.gamelogic.gamelogic as gamelogic
        self.tictactoe = gamelogic.TicTacToe()
        while True:
            gameMode = input("\n[1] Computer\n[2] Two-Player\n\nEnter game mode to play: ")
            array = self.tictactoe.createArray(3,3)
            if gameMode == "1":
                self.tictactoe.computerGame(array)
            elif gameMode == "2":
                self.tictactoe.localGame(array)
            else:
                print("Please enter a valid game mode.\n")
                continue
            break

def run():
    app = App()
    app.run()