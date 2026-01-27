def chessboard():
    board = ""
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                board += "*"
            else:
                board += "o"
        board += "\n"
    return board    
print(chessboard())
   

