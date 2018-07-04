from IPython.display import clear_output
board = None
player = 1
game = 1
xvalues = []
ovalues = []
moves = 0

def startGame():
    global board
    global game
    global player
    global moves
    moves = 0
    game = 1
    player = 1
    board = ["none", ["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"]]
    displayBoard()
    print("^Position Example Board^")
    board = ["none", [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def displayBoard():
    global board
    display = f"""
          *     *
      {board[1][0]}   *  {board[1][1]}  *   {board[1][2]}
          *     *
    * * * * * * * * * *
          *     *
      {board[2][0]}   *  {board[2][1]}  *   {board[2][2]}
          *     *
    * * * * * * * * * *
          *     *
      {board[3][0]}   *  {board[3][1]}  *   {board[3][2]}
          *     *
    """
    print('\n'*100)
    print(display)

def updateBoard(playerIn, xy, player):
    global board
    if player == 1: 
        symbol = "X"
        xvalues.append(playerIn)
    else: 
        symbol = "O"
        ovalues.append(playerIn)
    board[xy[0]][xy[1]] = symbol

def decode(position):
    if position < 4:
        return 3, position-1
    elif position < 7:
        return 2, position-4
    elif position < 10:
        return 1, position-7
    else:
        return 0,0

def getInput(player):
    global board
    global moves
    good = 0
    while good != 2:
        if good == 1:
            playerIn = int(input(f"Player {player}, try again. "))
        elif good == 0:
            playerIn = int(input(f"Player {player}, make a move. "))
            good = 1
        xy = decode(playerIn)
        if playerIn < 10 and board[xy[0]][xy[1]] != "X" and board[xy[0]][xy[1]] != "O":
            good = 2
    updateBoard(playerIn, xy, player)
    moves+=1
    return playerIn

def checkWin(player, lastPlay):
    global board
    for row in board[1:]:
        if(row[1] == row[2] == row[0] != " "):
            print(f'{player} wins with a row!')
            return True
    for y in range(0,3):
        if(board[1][y] == board[2][y] == board[3][y] != " "):
            print(f'{player} wins with a column!')
            return True
    if(board[3][0] == board[2][1] == board[1][2] != " ") or (board[1][0] == board[2][1] == board[3][2] != " "):
        print(f'{player} wins with a diagonal!')
        return True
    return False

def checkPlayAgain():
    inn = input("Play again? (y/n) ")
    if inn == 'y':
        return True
    elif inn == 'n':
        return False

startGame()

while game:
    lastPlay = getInput(player)
    displayBoard()
    win = checkWin(player, lastPlay)
    if win or moves == 9:
        if checkPlayAgain():
            startGame()
        else:
            game = 0
    else: 
        if player == 1 : player = 2
        else: player = 1
else:
    print('Game Over')