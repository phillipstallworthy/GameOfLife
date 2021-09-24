# Game of Life - https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
# Any live cell with two or three live neighbours survives.
# Any dead cell with three live neighbours becomes a live cell.
# All other live cells die in the next generation. Similarly, all other dead cells stay dead.

# global data
game = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

def printGol(game):
    for line in game:
        for cell in line:
            print(cell, end="")
        print("")
    print("")

def extendLeft(game, growth):
    for idx, line in enumerate(game):
        if idx in growth:
            line.insert(0,1)
        else:
            line.insert(0,0)

def extentRight(game, growth):
    for idx, line in enumerate(game):
        if idx in growth:
            line.append(1)
        else:
            line.append(0)

def extendUp(game, growth):
    line = []
    for i in range(len(game[0])):
        if i in growth:
            line.append(1)
        else:
            line.append(0)
    game.insert(0,line)

def extendDown(game, growth):
    line = []
    for i in range(len(game[0])):
        if i in growth:
            line.append(1)
        else:
            line.append(0)
    game.append(line)

# Iteragte each cell
#for line in game:
        #for cell in line:
            #countLiveNeigbours


# game logic
# iterate over each cell
# apply rules as it is
# apply changes - new data structure

# naive strategy
#   single thread
#   creat new data structure each tick
#   keep track of live growth, and apply at the end

def countLiveNeigbours(line,cell,game):
    count = 0
    if game[line][cell + 1] == 1:
        count += 1

    if game[line][cell - 1] == 1:
        count += 1

    if game[line -1][cell] == 1:
        count += 1

    if game[line + 1][cell] == 1:
        count += 1

    if game[line - 1][cell - 1] == 1:
        count += 1

    if game[line - 1][cell + 1] == 1:
        count += 1

    if game[line + 1][cell - 1] == 1:
        count += 1

    if game[line + 1][cell + 1] == 1:
        count += 1 

    return count

# game loop, sort-a
printGol(game)
extendLeft(game,[1,4])
extendLeft(game,[1,4])
extendLeft(game,[1,4])
extendLeft(game,[1,4])
printGol(game)
extentRight(game,[0,3])
extentRight(game,[0,3])
extentRight(game,[0,3])
extentRight(game,[0,3])
printGol(game)
extendUp(game,[2,5,6])
extendUp(game,[2,5,6])
extendUp(game,[2,5,6])
extendUp(game,[2,5,6])
printGol(game)
extendDown(game,[2,5,6,11])
extendDown(game,[2,5,6,11])
extendDown(game,[2,5,6,11])
extendDown(game,[2,5,6,11])
printGol(game)

line = 1; cell = 1; print ("(expect 3) live neighbours of line ", line, " cell ", cell, " = ", countLiveNeigbours(line,cell,game) )
line = 0; cell = 0; print ("(expect 0) live neighbours of line ", line, " cell ", cell, " = ", countLiveNeigbours(line,cell,game) )
line = 5; cell = 0; print ("(expect 2) live neighbours of line ", line, " cell ", cell, " = ", countLiveNeigbours(line,cell,game) )
line = 10; cell = 6; print ("(expect 5) live neighbours of line ", line, " cell ", cell, " = ", countLiveNeigbours(line,cell,game) )