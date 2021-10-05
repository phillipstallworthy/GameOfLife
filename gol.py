# Game of Life - https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
# Any live cell with two or three live neighbours survives.
# Any dead cell with three live neighbours becomes a live cell.
# All other live cells die in the next generation. Similarly, all other dead cells stay dead.

import copy

# global game data
game = [[0,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,1]]

def printGol(game):
    for line in game:
        for cell in line:
            print(cell, end="")
        print("")
    print("")

def extendLeft(game):
    for line in game:
            line.insert(0,0)

def extendRight(game):
    for line in game:
            line.append(0)

def extendUp(game):
    line = []
    for i in range(len(game[0])):
            line.append(0)
    game.insert(0,line)

def extendDown(game):
    line = []
    for i in range(len(game[0])):
            line.append(0)
    game.append(line)

# if the top, bottom, left or right row or column have a '1' in them, then exetend 
# in that direction as live cells may grow into it. (a shrink function might be interesting too)
# TODO - cell should probably be "item"
def grow(game):

    newGame = copy.deepcopy(game) # also deep copy in generate..combine functions?

    for c in newGame[0]:
        if c == 1:
            extendUp(newGame)
            break
    
    for c in newGame[len(newGame)-1]:
        if c == 1:
            extendDown(newGame)
            break

    for c in newGame:
        if c[0] == 1:
            extendLeft(newGame)
            break

    for c in newGame:
        if c[len(c) - 1 ] == 1:
            extendRight(newGame)
            break
    for c in newGame[0]:
        if c == 1:
            extendUp(newGame)
            break
    
    for c in newGame[len(newGame)-1]:
        if c == 1:
            extendDown(newGame)
            break

    for c in newGame:
        if c[0] == 1:
            extendLeft(newGame)
            break

    for c in newGame:
        if c[len(c) - 1 ] == 1:
            extendRight(newGame)
            break
    return newGame

# line - index
# call - index
# game - list of lists.
def countLiveNeigbours(line,cell,game):
    count = 0
    
    lineLimit = len(game[0]) - 1
    gameLimit = len(game) - 1

    if cell < lineLimit and game[line][cell + 1] == 1:
        count += 1

    if cell >= 0 and game[line][cell - 1] == 1:
        count += 1

    if line > 0 and game[line -1][cell] == 1:
        count += 1

    if line < gameLimit and game[line + 1][cell] == 1:
        count += 1

    if line > 0 and cell >= 0 and game[line - 1][cell - 1] == 1:
        count += 1

    if line > 0 and cell < lineLimit and game[line - 1][cell + 1] == 1:
        count += 1

    if line < gameLimit and cell >= 0 and game[line + 1][cell - 1] == 1:
        count += 1

    if line < gameLimit and cell < lineLimit and game[line + 1][cell + 1] == 1:
        count += 1 

    return count

# game logic
# iterate over each cell
# apply rules as it is
# apply changes - new data structure

# naive strategy
#   single thread
#   creat new data structure each tick
#   keep track of live growth, and apply at the end

# maybe the "map" built in function is useful to apply a functino to every item of an iterable

# Iterate each cell
def generate(game):

    tick = copy.deepcopy(game)
    
    for idxl, line in enumerate(tick):
        for idxc, cell in enumerate(line):
            count = countLiveNeigbours(idxl,idxc,tick)

            if cell == 1 and count == 3:
                tick[idxl][idxc] = 1
                continue

            if cell == 1 and count == 2:
                tick[idxl][idxc] = 1
                continue

            if cell == 0 and count == 3:
                tick[idxl][idxc] = 1
                continue
            
            tick[idxl][idxc] = 0
    return tick

# game loop, sort-a
#printGol(game)
#line = 1; cell = 5; print ("(expect 2) Live neighbours of line",line, "cell", cell, " = ", countLiveNeigbours(line,cell,game) )
#line = 1; cell = 4; print ("(expect 1) Live neighbours of line",line, "cell", cell, " = ", countLiveNeigbours(line,cell,game) )
#print()

printGol(game)

ticks = 10

for i in range(ticks):
    game = grow(game)
    game = generate(game)
    printGol(game)