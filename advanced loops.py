for row in range (5):
    if row%2 == 0:
        print(" | | ")
    else:
        print("-----")

def playingBoardCreated(rows, columns):
    if(createPlayingBoard(rows, columns)):
        print('Here is your playing board.')
    else:
        print('Err, No playing board for you.')
