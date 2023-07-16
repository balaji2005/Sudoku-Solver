class Grid:

    def __init__(self):
        self.grid = [
                        [0, 0, 0,   0, 0, 0,   0, 0, 0],
                        [0, 0, 0,   0, 0, 0,   0, 0, 0],
                        [0, 0, 0,   0, 0, 0,   0, 0, 0],

                        [0, 0, 0,   0, 0, 0,   0, 0, 0],
                        [0, 0, 0,   0, 0, 0,   0, 0, 0],
                        [0, 0, 0,   0, 0, 0,   0, 0, 0],

                        [0, 0, 0,   0, 0, 0,   0, 0, 0],
                        [0, 0, 0,   0, 0, 0,   0, 0, 0],
                        [0, 0, 0,   0, 0, 0,   0, 0, 0]
                    ]
        
    def updateGrid(self, cell):
        node = (cell.coord[0], cell.coord[1])
        number = cell.number
        self.grid[node[0]][node[1]] = number
        print(f'Entering {number} to {node}')

    # Made it better
    def __str__(self) -> str:
        ret = '___________________\n'
        for i in range(9):
            for j in range(9):
                if grid.grid[i][j]:
                    ret += str(grid.grid[i][j]) + ' '
                else:
                    ret += ' ' + ' '
                if j in {2, 5}:
                    ret += ' '
            ret+='\n'
            if i in {2, 5}:
                ret += '\n'
        ret += '___________________\n'
        return ret
    
    def solved(self):
        for i in range(9):
            for j in grid.grid[i]:
                if j == 0:
                    return False
        return True

class Cell:
    def __init__(self, i, j):
        self.coord = (i, j)
        self.choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.number = 0

    def __str__(self):
        return str(self.coord) + ' = ' + str(self.choices)
    
    def clear_choice(self, number):
        self.choices.remove(number)

    def fill(self, number):
        self.choices = []
        self.number = number
        grid.updateGrid(self)
        for group in groups:
            if self in group.cells:
                group.removeCell(self)
                for cell in group.cells:
                    if number in cell.choices:
                        cell.clear_choice(number)
        cells.remove(self)
    
    def updateNumber(self, number):
        self.choices = []
        self.number = number
        for group in groups:
            if self in group.cells:
                group.removeCell(self)
                for cell in group.cells:
                    if number in cell.choices:
                        cell.clear_choice(number)
        cells.remove(self)
    
class Group:
    def __init__(self, type, cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9):
        self.type = type
        self.cells = [cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9]
        self.filledNumbers = []

    def __str__(self):
        return self.type + ' containing ' + self.cells
    
    def removeCell(self, cell):
        self.cells.remove(cell)
        self.filledNumbers.append(cell.number)
        for otherCell in self.cells:
            if cell.number in otherCell.choices:
                otherCell.choices.remove(cell.number)

    def getCells(self, number):
        ret = []
        for cell in self.cells:
            if number in cell.choices:
                ret.append(cell)
        return ret

    def isFilled(self, number):
        if number in self.filledNumbers:
            return True
        return False

def updateCells(grid, cells):
    for i in range(9):
        for j in range(9):
            if grid.grid[i][j] != 0:
                number = grid.grid[i][j]
                for cell in cells:
                    if cell.coord == (i, j):
                        cell.updateNumber(number)
                

# Starting the Player
grid = Grid()

# grid.grid = [
#     [0, 0, 0,   0, 0, 0,   0, 0, 0],
#     [0, 0, 0,   0, 0, 0,   0, 0, 0],
#     [0, 0, 0,   0, 0, 0,   0, 0, 0],

#     [0, 0, 0,   0, 0, 0,   0, 0, 0],
#     [0, 0, 0,   0, 0, 0,   0, 0, 0],
#     [0, 0, 0,   0, 0, 0,   0, 0, 0],

#     [0, 0, 0,   0, 0, 0,   0, 0, 0],
#     [0, 0, 0,   0, 0, 0,   0, 0, 0],
#     [0, 0, 0,   0, 0, 0,   0, 0, 0]
# ]

grid.grid = [
    list(map(int, input().split())),
    list(map(int, input().split())),
    list(map(int, input().split())),
    list(map(int, input().split())),
    list(map(int, input().split())),
    list(map(int, input().split())),
    list(map(int, input().split())),
    list(map(int, input().split())),
    list(map(int, input().split())),
]

print(grid)

# Row 1
cell_1_1 = Cell(0, 0)
cell_1_2 = Cell(0, 1)
cell_1_3 = Cell(0, 2)
cell_1_4 = Cell(0, 3)
cell_1_5 = Cell(0, 4)
cell_1_6 = Cell(0, 5)
cell_1_7 = Cell(0, 6)
cell_1_8 = Cell(0, 7)
cell_1_9 = Cell(0, 8)

# Row 2
cell_2_1 = Cell(1, 0)
cell_2_2 = Cell(1, 1)
cell_2_3 = Cell(1, 2)
cell_2_4 = Cell(1, 3)
cell_2_5 = Cell(1, 4)
cell_2_6 = Cell(1, 5)
cell_2_7 = Cell(1, 6)
cell_2_8 = Cell(1, 7)
cell_2_9 = Cell(1, 8)

# Row 3
cell_3_1 = Cell(2, 0)
cell_3_2 = Cell(2, 1)
cell_3_3 = Cell(2, 2)
cell_3_4 = Cell(2, 3)
cell_3_5 = Cell(2, 4)
cell_3_6 = Cell(2, 5)
cell_3_7 = Cell(2, 6)
cell_3_8 = Cell(2, 7)
cell_3_9 = Cell(2, 8)

# Row 4
cell_4_1 = Cell(3, 0)
cell_4_2 = Cell(3, 1)
cell_4_3 = Cell(3, 2)
cell_4_4 = Cell(3, 3)
cell_4_5 = Cell(3, 4)
cell_4_6 = Cell(3, 5)
cell_4_7 = Cell(3, 6)
cell_4_8 = Cell(3, 7)
cell_4_9 = Cell(3, 8)

# Row 5
cell_5_1 = Cell(4, 0)
cell_5_2 = Cell(4, 1)
cell_5_3 = Cell(4, 2)
cell_5_4 = Cell(4, 3)
cell_5_5 = Cell(4, 4)
cell_5_6 = Cell(4, 5)
cell_5_7 = Cell(4, 6)
cell_5_8 = Cell(4, 7)
cell_5_9 = Cell(4, 8)

# Row 6
cell_6_1 = Cell(5, 0)
cell_6_2 = Cell(5, 1)
cell_6_3 = Cell(5, 2)
cell_6_4 = Cell(5, 3)
cell_6_5 = Cell(5, 4)
cell_6_6 = Cell(5, 5)
cell_6_7 = Cell(5, 6)
cell_6_8 = Cell(5, 7)
cell_6_9 = Cell(5, 8)

# Row 7
cell_7_1 = Cell(6, 0)
cell_7_2 = Cell(6, 1)
cell_7_3 = Cell(6, 2)
cell_7_4 = Cell(6, 3)
cell_7_5 = Cell(6, 4)
cell_7_6 = Cell(6, 5)
cell_7_7 = Cell(6, 6)
cell_7_8 = Cell(6, 7)
cell_7_9 = Cell(6, 8)

# Row 8
cell_8_1 = Cell(7, 0)
cell_8_2 = Cell(7, 1)
cell_8_3 = Cell(7, 2)
cell_8_4 = Cell(7, 3)
cell_8_5 = Cell(7, 4)
cell_8_6 = Cell(7, 5)
cell_8_7 = Cell(7, 6)
cell_8_8 = Cell(7, 7)
cell_8_9 = Cell(7, 8)

# Row 9
cell_9_1 = Cell(8, 0)
cell_9_2 = Cell(8, 1)
cell_9_3 = Cell(8, 2)
cell_9_4 = Cell(8, 3)
cell_9_5 = Cell(8, 4)
cell_9_6 = Cell(8, 5)
cell_9_7 = Cell(8, 6)
cell_9_8 = Cell(8, 7)
cell_9_9 = Cell(8, 8)

# Rows
group1 = Group('Row', cell_1_1, cell_1_2, cell_1_3, cell_1_4, cell_1_5, cell_1_6, cell_1_7, cell_1_8, cell_1_9)
group2 = Group('Row', cell_2_1, cell_2_2, cell_2_3, cell_2_4, cell_2_5, cell_2_6, cell_2_7, cell_2_8, cell_2_9)
group3 = Group('Row', cell_3_1, cell_3_2, cell_3_3, cell_3_4, cell_3_5, cell_3_6, cell_3_7, cell_3_8, cell_3_9)
group4 = Group('Row', cell_4_1, cell_4_2, cell_4_3, cell_4_4, cell_4_5, cell_4_6, cell_4_7, cell_4_8, cell_4_9)
group5 = Group('Row', cell_5_1, cell_5_2, cell_5_3, cell_5_4, cell_5_5, cell_5_6, cell_5_7, cell_5_8, cell_5_9)
group6 = Group('Row', cell_6_1, cell_6_2, cell_6_3, cell_6_4, cell_6_5, cell_6_6, cell_6_7, cell_6_8, cell_6_9)
group7 = Group('Row', cell_7_1, cell_7_2, cell_7_3, cell_7_4, cell_7_5, cell_7_6, cell_7_7, cell_7_8, cell_7_9)
group8 = Group('Row', cell_8_1, cell_8_2, cell_8_3, cell_8_4, cell_8_5, cell_8_6, cell_8_7, cell_8_8, cell_8_9)
group9 = Group('Row', cell_9_1, cell_9_2, cell_9_3, cell_9_4, cell_9_5, cell_9_6, cell_9_7, cell_9_8, cell_9_9)

# Columns
group10 = Group('Column', cell_1_1, cell_2_1, cell_3_1, cell_4_1, cell_5_1, cell_6_1, cell_7_1, cell_8_1, cell_9_1)
group11 = Group('Column', cell_1_2, cell_2_2, cell_3_2, cell_4_2, cell_5_2, cell_6_2, cell_7_2, cell_8_2, cell_9_2)
group12 = Group('Column', cell_1_3, cell_2_3, cell_3_3, cell_4_3, cell_5_3, cell_6_3, cell_7_3, cell_8_3, cell_9_3)
group13 = Group('Column', cell_1_4, cell_2_4, cell_3_4, cell_4_4, cell_5_4, cell_6_4, cell_7_4, cell_8_4, cell_9_4)
group14 = Group('Column', cell_1_5, cell_2_5, cell_3_5, cell_4_5, cell_5_5, cell_6_5, cell_7_5, cell_8_5, cell_9_5)
group15 = Group('Column', cell_1_6, cell_2_6, cell_3_6, cell_4_6, cell_5_6, cell_6_6, cell_7_6, cell_8_6, cell_9_6)
group16 = Group('Column', cell_1_7, cell_2_7, cell_3_7, cell_4_7, cell_5_7, cell_6_7, cell_7_7, cell_8_7, cell_9_7)
group17 = Group('Column', cell_1_8, cell_2_8, cell_3_8, cell_4_8, cell_5_8, cell_6_8, cell_7_8, cell_8_8, cell_9_8)
group18 = Group('Column', cell_1_9, cell_2_9, cell_3_9, cell_4_9, cell_5_9, cell_6_9, cell_7_9, cell_8_9, cell_9_9)

# Grids
group19 = Group('Grid', cell_1_1, cell_1_2, cell_1_3, cell_2_1, cell_2_2, cell_2_3, cell_3_1, cell_3_2, cell_3_3)
group20 = Group('Grid', cell_1_4, cell_1_5, cell_1_6, cell_2_4, cell_2_5, cell_2_6, cell_3_4, cell_3_5, cell_3_6)
group21 = Group('Grid', cell_1_7, cell_1_8, cell_1_9, cell_2_7, cell_2_8, cell_2_9, cell_3_7, cell_3_8, cell_3_9)
group22 = Group('Grid', cell_4_1, cell_4_2, cell_4_3, cell_5_1, cell_5_2, cell_5_3, cell_6_1, cell_6_2, cell_6_3)
group23 = Group('Grid', cell_4_4, cell_4_5, cell_4_6, cell_5_4, cell_5_5, cell_5_6, cell_6_4, cell_6_5, cell_6_6)
group24 = Group('Grid', cell_4_7, cell_4_8, cell_4_9, cell_5_7, cell_5_8, cell_5_9, cell_6_7, cell_6_8, cell_6_9)
group25 = Group('Grid', cell_7_1, cell_7_2, cell_7_3, cell_8_1, cell_8_2, cell_8_3, cell_9_1, cell_9_2, cell_9_3)
group26 = Group('Grid', cell_7_4, cell_7_5, cell_7_6, cell_8_4, cell_8_5, cell_8_6, cell_9_4, cell_9_5, cell_9_6)
group27 = Group('Grid', cell_7_7, cell_7_8, cell_7_9, cell_8_7, cell_8_8, cell_8_9, cell_9_7, cell_9_8, cell_9_9)

cells = [
    cell_1_1, cell_1_2, cell_1_3, cell_1_4, cell_1_5, cell_1_6, cell_1_7, cell_1_8, cell_1_9, 
    cell_2_1, cell_2_2, cell_2_3, cell_2_4, cell_2_5, cell_2_6, cell_2_7, cell_2_8, cell_2_9, 
    cell_3_1, cell_3_2, cell_3_3, cell_3_4, cell_3_5, cell_3_6, cell_3_7, cell_3_8, cell_3_9, 
    cell_4_1, cell_4_2, cell_4_3, cell_4_4, cell_4_5, cell_4_6, cell_4_7, cell_4_8, cell_4_9, 
    cell_5_1, cell_5_2, cell_5_3, cell_5_4, cell_5_5, cell_5_6, cell_5_7, cell_5_8, cell_5_9, 
    cell_6_1, cell_6_2, cell_6_3, cell_6_4, cell_6_5, cell_6_6, cell_6_7, cell_6_8, cell_6_9, 
    cell_7_1, cell_7_2, cell_7_3, cell_7_4, cell_7_5, cell_7_6, cell_7_7, cell_7_8, cell_7_9, 
    cell_8_1, cell_8_2, cell_8_3, cell_8_4, cell_8_5, cell_8_6, cell_8_7, cell_8_8, cell_8_9, 
    cell_9_1, cell_9_2, cell_9_3, cell_9_4, cell_9_5, cell_9_6, cell_9_7, cell_9_8, cell_9_9
]

groups = [
    group1,
    group2,
    group3,
    group4,
    group5,
    group6,
    group7,
    group8,
    group9,
    group10,
    group11,
    group12,
    group13,
    group14,
    group15,
    group16,
    group17,
    group18,
    group19,
    group20,
    group21,
    group22,
    group23,
    group24,
    group25,
    group26,
    group27
]

noChangeCount = 0
noChange = True

updateCells(grid, cells)

while(not grid.solved() and noChangeCount <= 10):
    noChange = True
    for cell in cells:
        print(cell)
        if len(cell.choices) == 1:
            cell.fill(cell.choices[0])
            noChange = False
            noChangeCount = 0
    for number in range(9):
        for group in groups:
            if not group.isFilled(number):
                for group1 in groups:
                    if set(group.getCells(number)) <= set(group1.cells):
                        for cell in set(group1.cells) - set(group.getCells(number)):
                            if number in cell.choices:
                                cell.choices.remove(number)
                                noChange = False
                                noChangeCount = 0
    if noChange:
        noChangeCount += 1

if (not grid.solved()):
    print('I couldn\'t solve it completely!😔😞')
    print(grid)
else:
    print(grid)