import time
import datetime

grid = [
    [5, 4, 0, 0, 6, 0, 0, 7, 8],
    [3, 0, 6, 1, 8, 0, 0, 2, 0],
    [0, 9, 2, 0, 0, 4, 5, 0, 0],
    [6, 0, 9, 0, 0, 0, 7, 0, 5],
    [7, 1, 0, 4, 9, 6, 0, 0, 0],
    [4, 0, 8, 0, 0, 3, 1, 0, 0],
    [0, 0, 0, 0, 3, 0, 9, 0, 0],
    [1, 8, 0, 0, 0, 0, 2, 5, 7],
    [9, 5, 0, 0, 2, 7, 0, 0, 0],
]

strt = datetime.datetime.now()


def PrintSudokuGrid(board):
    print("-" + "----" * 9)
    for i, row in enumerate(board):
        print(("|" + " {}   {}   {} |" * 3).format(*[x if x != 0 else " " for x in row]))
        if i % 3 == 2:
            print("-" + "----" * 9)
        else:
            print("-" + "   -" * 9)

# Verify All rows and columns if the value is not repeating and sum of all rows is 45
def ValueVerification(row_col):
    global is_in_list
    p = d = 0

    for i in range(len(row_col)):
        is_in_list = row_col.count(row_col[i])
        if is_in_list == 1:
            is_in_list = 1
            p = p + row_col[i]
        else:
            is_in_list = 0

    if p == 45 and is_in_list == 1:
        return True
    else:
        return False

# Get all Empty Indexes
def PossibleIndex(row):
    index = []
    for num in range(9):
        if grid[row][num] == 0:
            index.append(num)
    return index

# Get all Possible value to fill the empty indexes
def PossibleValue(row, grids):
    value = []
    for num in range(1, 10):
        if num not in grids[row]:
            value.append(num)
    return value

def ColumnValue(col, grid):
    columns = []
    for c in range(len(grid)):
        columns.append(grid[c][col])
    return columns

# Returns Index Values of the Specific Cube
def getRowColRange(n):
    if n == 0:
        return [0, 1, 2]
    elif n == 1:
        return [3, 4, 5]
    elif n == 2:
        return [6, 7, 8]

# Gets All Values of the Cube
def getCubeContent(i, j, sgrid):
    row = getRowColRange(i)
    col = getRowColRange(j)
    cube_content = []
    for rowV in row:
        for colV in col:
            cube_content.append(sgrid[rowV][colV])
    return cube_content

# Get Row and Column Indexes Within a Cube
def cubeRowCol(i):
    if i < 3:
        return 0
    elif 3 <= i <= 5:
        return 1
    else:
        return 2

# Checks Sudoku If the Values not repeating In Row, Column & Cube
def SudokuCheck(gridfinal):
    horizontal = 0
    for h in range(len(gridfinal)):
        results = ValueVerification(gridfinal[h])
        if results:
            horizontal += 1
        else:
            horizontal = 0

    vertical = 0
    for v in range(len(gridfinal)):
        col = []
        for k in range(len(gridfinal)):
            col.append(gridfinal[k][v])
        results = ValueVerification(col)
        if results:
            vertical += 1
        else:
            vertical = 0

    col_result = []
    col_index = [1, 4, 7]

    for item in col_index:
        for value in range(1, 8):
            if value % 3 == 1:
                col_result.append(ValueVerification(getCubeContent(cubeRowCol(item), cubeRowCol(value), gridfinal)))

    if False not in col_result and len(col_result) == 9:
        cube = 1
    else:
        cube = 0

    if cube == 1 and horizontal == 9 and vertical == 9:
        return True
    else:
        return False

def possibleIndex(row):
    index = []
    for num in range(9):
        if grid[row][num] == 0:
            index.append(num)
    return index

PrintSudokuGrid(grid)

result = False
failValue = 0

while not result:
    loopValue = 0
    for i in range(len(grid)):
        rowIndex = possibleIndex(i)
        rowPossibleValue = PossibleValue(i, grid)
        finalPossibleValue = []

        for item in rowIndex:
            colValue = ColumnValue(item, grid)
            cubeValue = getCubeContent(cubeRowCol(i), cubeRowCol(item), grid)

            for positionValue in rowPossibleValue:
                if positionValue not in colValue and positionValue not in cubeValue:
                    finalPossibleValue.append(positionValue)

            if len(finalPossibleValue) == 1:
                loopValue += 1
                grid[i][item] = finalPossibleValue[0]
                print("Printing Solution....\n")
                time.sleep(0.001)
                PrintSudokuGrid(grid)
            finalPossibleValue = []
        resultFinal = SudokuCheck(grid)

        if resultFinal:
            print("Successfully Solved!!\n")
            result = True
        else:
            if loopValue == 0:
                failValue += 1
            if failValue == 2:
                print("All Single Value Tried!")
                break

time_taken = datetime.datetime.now()
print("Total Time Taken")
print(time_taken - strt)
print(grid)