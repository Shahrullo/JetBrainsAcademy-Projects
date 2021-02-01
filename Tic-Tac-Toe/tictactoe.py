####### Combinations #######
def comb(s):
    var = []
    var.append(s[0] + s[1] + s[2])
    var.append(s[3] + s[4] + s[5])
    var.append(s[6] + s[7] + s[8])
    var.append(s[0] + s[3] + s[6])
    var.append(s[1] + s[4] + s[7])
    var.append(s[2] + s[5] + s[8])
    var.append(s[0] + s[4] + s[8])
    var.append(s[2] + s[4] + s[6])
    return var

####### Matrix Combinations #######
def toMatrix(s):
    matrix = [[0 for x in range(3)] for y in range(3)]
    matrix[0][0] = s[6]
    matrix[0][1] = s[3]
    matrix[0][2] = s[0]
    matrix[1][0] = s[7]
    matrix[1][1] = s[4]
    matrix[1][2] = s[1]
    matrix[2][0] = s[8]
    matrix[2][1] = s[5]
    matrix[2][2] = s[2]
    return matrix

def fromMatrix(matrix):
    s = ['_' for i in range(9)]
    s[6] = matrix[0][0]
    s[3] = matrix[0][1]
    s[0] = matrix[0][2]
    s[7] = matrix[1][0]
    s[4] = matrix[1][1]
    s[1] = matrix[1][2]
    s[8] = matrix[2][0]
    s[5] = matrix[2][1]
    s[2] = matrix[2][2]
    return s

####### Test ###########
def test(var):
    if ("XXX" in comb(var) and "OOO" in comb(var)) \
            or (abs(var.count("X") - var.count("O")) > 1):
        res = "Impossible"
    elif "XXX" not in comb(var) and "OOO" not in comb(var) \
            and any("_" in t for t in comb(var)):
        res = "Game not finished"
    elif "XXX" not in comb(var) and "OOO" not in comb(var):
        res = "Draw"
    elif "XXX" in comb(var):
        res = "X wins"
    elif "OOO" in comb(var):
        res = "O wins"

    return res

####### Conditions ###########
def condition(s, row, col):
    if row.isalpha() or col.isalpha():
        print('You should enter numbers!')
        return False
    elif int(row) > 3 or int(col) > 3:
        print('Coordinates should be from 1 to 3!')
        return False
    matrix = toMatrix(s)
    if matrix[int(row) - 1][int(col) - 1] == 'X' or matrix[int(row) - 1][int(col) - 1] == 'O':
        print('This cell is occupied! Choose another one!')
        return False

    return True

####### Get Play #######
def getPlay(s, row, col, new):
    matrix = toMatrix(s)
    matrix[int(row) - 1][int(col) - 1] = new
    return fromMatrix(matrix)

def start(option):
    if option == 'O':
        return 'X'
    else:
        return 'O'

######## display the game #######
def display(s):
    print('---------')
    print(f'| {s[0]} {s[1]} {s[2]} |')
    print(f'| {s[3]} {s[4]} {s[5]} |')
    print(f'| {s[6]} {s[7]} {s[8]} |')
    print('---------')
    
s = ['_' for i in range(9)]
display(s)

option = 'O'
res = None

####### start engine #######
while res != "X wins" and res != "O wins" and res != "Draw":
    coord = input('Enter the coordinates: ').split()
    if len(coord) > 1:
        while not (condition(s, coord[0], coord[1])):
            coord = input('Enter the coordinates: ').split()
        option = start(option)
        s = getPlay(s, coord[0], coord[1], option)
        display(s)
        res = test(s)
        print(res)