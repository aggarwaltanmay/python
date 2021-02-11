
def drawfield(field):
    for row in range(5):
        if row%2 == 0:
            practicalrow = int(row/2)
            for column in range(5):
                if column%2 == 0:
                    practicalcolumn = int(column/2)
                    if column!= 4:
                        print(field[practicalcolumn][practicalrow],end ="")
                    else:
                        print(field[practicalcolumn][practicalrow])
                else:
                    print("|",end="")
            else:
                print("-----")
Player = 1
CurrentField = [[" "," "," "],[" "," "," ",],[" "," "," "]]
drawfield(CurrentField)
while(True):
    print("Player Turn :",Player)
    MoveRow = int(input("Enter the row\n"))
    MoveColumn = int(input("Enter the column\n"))
    if Player == 1:

        if CurrentField[[MoveColumn][MoveRow]] == " ":
            CurrentField[[MoveColumn][MoveRow]] = "X"
            Player = 2
    else:

        if CurrentField[[MoveColumn][MoveRow]] == " ":
            CurrentField[[MoveColumn][MoveRow]] = "O"
            Player = 1
    drawfield(CurrentField)