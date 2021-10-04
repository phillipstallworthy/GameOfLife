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

    for c in game[0]:
        if c == 1:
            extendUp(game)
            break
    
    for c in game[len(game)-1]:
        if c == 1:
            extendDown(game)
            break

    for c in game:
        if c[0] == 1:
            extendLeft(game)
            break

    for c in game:
        if c[len(c) - 1 ] == 1:
            extendRight(game)
            break
    for c in game[0]:
        if c == 1:
            extendUp(game)
            break
    
    for c in game[len(game)-1]:
        if c == 1:
            extendDown(game)
            break

    for c in game:
        if c[0] == 1:
            extendLeft(game)
            break

    for c in game:
        if c[len(c) - 1 ] == 1:
            extendRight(game)
            break

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

    for idxl, line in enumerate(game):
        for idxc, cell in enumerate(line):
            count = countLiveNeigbours(idxl,idxc,game)

            #print ("line",idxl,"cell",idxc,"count",count)

            if cell == 1 and count == 3:
                #print("alive ******************* 3 live neighbours")
                tick[idxl][idxc] = 1
                #printGol(tick)
                continue

            if cell == 1 and count == 2:
                #print("alive ******************* 2 live neighbours")
                tick[idxl][idxc] = 1
                #printGol(tick)
                continue

            if cell == 0 and count == 3:
                #print("dead to alive 3 live neighbours")
                tick[idxl][idxc] = 1
                continue
            
            #if cell == 1:
            #    print ("Alive to dead +++++++++++++++++++")
            #else: 
            #    print("stays dead")
            
            #print("2")
            tick[idxl][idxc] = 0
            #print("")
    return tick

# game loop, sort-a
#printGol(game)
#line = 1; cell = 5; print ("(expect 2) Live neighbours of line",line, "cell", cell, " = ", countLiveNeigbours(line,cell,game) )
#line = 1; cell = 4; print ("(expect 1) Live neighbours of line",line, "cell", cell, " = ", countLiveNeigbours(line,cell,game) )
#print()

grow(game)
#printGol(game)

#line = 2; cell = 5; print ("(expect 1) Live neighbours of line",line, "cell", cell, " = ", countLiveNeigbours(line,cell,game) )
#print()

game = generate(game)
printGol(game)

game = generate(game)
printGol(game)

game = generate(game)
printGol(game)