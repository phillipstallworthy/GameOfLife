# Game of Life - https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
# Any live cell with two or three live neighbours survives.
# Any dead cell with three live neighbours becomes a live cell.
# All other live cells die in the next generation. Similarly, all other dead cells stay dead.

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

# game logic
# iterate over each cell
# apply rules as it is
# apply changes - new data structure

# naive strategy
#   single thread
#   creat new data structure each tick
#   keep track of live growth, and apply at the end

# game loop, sort-a
printGol(game)
line = 1; cell = 5; print ("(expect 2) live neighbours of line ", line, " cell ", cell, " = ", countLiveNeigbours(line,cell,game) )
grow(game)
printGol(game)

# Iterate each cell
for line in game:
        for cell in line:
            countLiveNeigbours
            
