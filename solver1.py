import copy

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
        
        # Row 1
        self.cell_1_1 = Cell(0, 0)
        self.cell_1_2 = Cell(0, 1)
        self.cell_1_3 = Cell(0, 2)
        self.cell_1_4 = Cell(0, 3)
        self.cell_1_5 = Cell(0, 4)
        self.cell_1_6 = Cell(0, 5)
        self.cell_1_7 = Cell(0, 6)
        self.cell_1_8 = Cell(0, 7)
        self.cell_1_9 = Cell(0, 8)

        # Row 2
        self.cell_2_1 = Cell(1, 0)
        self.cell_2_2 = Cell(1, 1)
        self.cell_2_3 = Cell(1, 2)
        self.cell_2_4 = Cell(1, 3)
        self.cell_2_5 = Cell(1, 4)
        self.cell_2_6 = Cell(1, 5)
        self.cell_2_7 = Cell(1, 6)
        self.cell_2_8 = Cell(1, 7)
        self.cell_2_9 = Cell(1, 8)

        # Row 3
        self.cell_3_1 = Cell(2, 0)
        self.cell_3_2 = Cell(2, 1)
        self.cell_3_3 = Cell(2, 2)
        self.cell_3_4 = Cell(2, 3)
        self.cell_3_5 = Cell(2, 4)
        self.cell_3_6 = Cell(2, 5)
        self.cell_3_7 = Cell(2, 6)
        self.cell_3_8 = Cell(2, 7)
        self.cell_3_9 = Cell(2, 8)

        # Row 4
        self.cell_4_1 = Cell(3, 0)
        self.cell_4_2 = Cell(3, 1)
        self.cell_4_3 = Cell(3, 2)
        self.cell_4_4 = Cell(3, 3)
        self.cell_4_5 = Cell(3, 4)
        self.cell_4_6 = Cell(3, 5)
        self.cell_4_7 = Cell(3, 6)
        self.cell_4_8 = Cell(3, 7)
        self.cell_4_9 = Cell(3, 8)

        # Row 5
        self.cell_5_1 = Cell(4, 0)
        self.cell_5_2 = Cell(4, 1)
        self.cell_5_3 = Cell(4, 2)
        self.cell_5_4 = Cell(4, 3)
        self.cell_5_5 = Cell(4, 4)
        self.cell_5_6 = Cell(4, 5)
        self.cell_5_7 = Cell(4, 6)
        self.cell_5_8 = Cell(4, 7)
        self.cell_5_9 = Cell(4, 8)

        # Row 6
        self.cell_6_1 = Cell(5, 0)
        self.cell_6_2 = Cell(5, 1)
        self.cell_6_3 = Cell(5, 2)
        self.cell_6_4 = Cell(5, 3)
        self.cell_6_5 = Cell(5, 4)
        self.cell_6_6 = Cell(5, 5)
        self.cell_6_7 = Cell(5, 6)
        self.cell_6_8 = Cell(5, 7)
        self.cell_6_9 = Cell(5, 8)

        # Row 7
        self.cell_7_1 = Cell(6, 0)
        self.cell_7_2 = Cell(6, 1)
        self.cell_7_3 = Cell(6, 2)
        self.cell_7_4 = Cell(6, 3)
        self.cell_7_5 = Cell(6, 4)
        self.cell_7_6 = Cell(6, 5)
        self.cell_7_7 = Cell(6, 6)
        self.cell_7_8 = Cell(6, 7)
        self.cell_7_9 = Cell(6, 8)

        # Row 8
        self.cell_8_1 = Cell(7, 0)
        self.cell_8_2 = Cell(7, 1)
        self.cell_8_3 = Cell(7, 2)
        self.cell_8_4 = Cell(7, 3)
        self.cell_8_5 = Cell(7, 4)
        self.cell_8_6 = Cell(7, 5)
        self.cell_8_7 = Cell(7, 6)
        self.cell_8_8 = Cell(7, 7)
        self.cell_8_9 = Cell(7, 8)

        # Row 9
        self.cell_9_1 = Cell(8, 0)
        self.cell_9_2 = Cell(8, 1)
        self.cell_9_3 = Cell(8, 2)
        self.cell_9_4 = Cell(8, 3)
        self.cell_9_5 = Cell(8, 4)
        self.cell_9_6 = Cell(8, 5)
        self.cell_9_7 = Cell(8, 6)
        self.cell_9_8 = Cell(8, 7)
        self.cell_9_9 = Cell(8, 8)

        # Rows
        self.group1 = Group('Row', self.cell_1_1, self.cell_1_2, self.cell_1_3, self.cell_1_4, self.cell_1_5, self.cell_1_6, self.cell_1_7, self.cell_1_8, self.cell_1_9)
        self.group2 = Group('Row', self.cell_2_1, self.cell_2_2, self.cell_2_3, self.cell_2_4, self.cell_2_5, self.cell_2_6, self.cell_2_7, self.cell_2_8, self.cell_2_9)
        self.group3 = Group('Row', self.cell_3_1, self.cell_3_2, self.cell_3_3, self.cell_3_4, self.cell_3_5, self.cell_3_6, self.cell_3_7, self.cell_3_8, self.cell_3_9)
        self.group4 = Group('Row', self.cell_4_1, self.cell_4_2, self.cell_4_3, self.cell_4_4, self.cell_4_5, self.cell_4_6, self.cell_4_7, self.cell_4_8, self.cell_4_9)
        self.group5 = Group('Row', self.cell_5_1, self.cell_5_2, self.cell_5_3, self.cell_5_4, self.cell_5_5, self.cell_5_6, self.cell_5_7, self.cell_5_8, self.cell_5_9)
        self.group6 = Group('Row', self.cell_6_1, self.cell_6_2, self.cell_6_3, self.cell_6_4, self.cell_6_5, self.cell_6_6, self.cell_6_7, self.cell_6_8, self.cell_6_9)
        self.group7 = Group('Row', self.cell_7_1, self.cell_7_2, self.cell_7_3, self.cell_7_4, self.cell_7_5, self.cell_7_6, self.cell_7_7, self.cell_7_8, self.cell_7_9)
        self.group8 = Group('Row', self.cell_8_1, self.cell_8_2, self.cell_8_3, self.cell_8_4, self.cell_8_5, self.cell_8_6, self.cell_8_7, self.cell_8_8, self.cell_8_9)
        self.group9 = Group('Row', self.cell_9_1, self.cell_9_2, self.cell_9_3, self.cell_9_4, self.cell_9_5, self.cell_9_6, self.cell_9_7, self.cell_9_8, self.cell_9_9)

        # Columns
        self.group10 = Group('Column', self.cell_1_1, self.cell_2_1, self.cell_3_1, self.cell_4_1, self.cell_5_1, self.cell_6_1, self.cell_7_1, self.cell_8_1, self.cell_9_1)
        self.group11 = Group('Column', self.cell_1_2, self.cell_2_2, self.cell_3_2, self.cell_4_2, self.cell_5_2, self.cell_6_2, self.cell_7_2, self.cell_8_2, self.cell_9_2)
        self.group12 = Group('Column', self.cell_1_3, self.cell_2_3, self.cell_3_3, self.cell_4_3, self.cell_5_3, self.cell_6_3, self.cell_7_3, self.cell_8_3, self.cell_9_3)
        self.group13 = Group('Column', self.cell_1_4, self.cell_2_4, self.cell_3_4, self.cell_4_4, self.cell_5_4, self.cell_6_4, self.cell_7_4, self.cell_8_4, self.cell_9_4)
        self.group14 = Group('Column', self.cell_1_5, self.cell_2_5, self.cell_3_5, self.cell_4_5, self.cell_5_5, self.cell_6_5, self.cell_7_5, self.cell_8_5, self.cell_9_5)
        self.group15 = Group('Column', self.cell_1_6, self.cell_2_6, self.cell_3_6, self.cell_4_6, self.cell_5_6, self.cell_6_6, self.cell_7_6, self.cell_8_6, self.cell_9_6)
        self.group16 = Group('Column', self.cell_1_7, self.cell_2_7, self.cell_3_7, self.cell_4_7, self.cell_5_7, self.cell_6_7, self.cell_7_7, self.cell_8_7, self.cell_9_7)
        self.group17 = Group('Column', self.cell_1_8, self.cell_2_8, self.cell_3_8, self.cell_4_8, self.cell_5_8, self.cell_6_8, self.cell_7_8, self.cell_8_8, self.cell_9_8)
        self.group18 = Group('Column', self.cell_1_9, self.cell_2_9, self.cell_3_9, self.cell_4_9, self.cell_5_9, self.cell_6_9, self.cell_7_9, self.cell_8_9, self.cell_9_9)

        # Grids
        self.group19 = Group('Grid', self.cell_1_1, self.cell_1_2, self.cell_1_3, self.cell_2_1, self.cell_2_2, self.cell_2_3, self.cell_3_1, self.cell_3_2, self.cell_3_3)
        self.group20 = Group('Grid', self.cell_1_4, self.cell_1_5, self.cell_1_6, self.cell_2_4, self.cell_2_5, self.cell_2_6, self.cell_3_4, self.cell_3_5, self.cell_3_6)
        self.group21 = Group('Grid', self.cell_1_7, self.cell_1_8, self.cell_1_9, self.cell_2_7, self.cell_2_8, self.cell_2_9, self.cell_3_7, self.cell_3_8, self.cell_3_9)
        self.group22 = Group('Grid', self.cell_4_1, self.cell_4_2, self.cell_4_3, self.cell_5_1, self.cell_5_2, self.cell_5_3, self.cell_6_1, self.cell_6_2, self.cell_6_3)
        self.group23 = Group('Grid', self.cell_4_4, self.cell_4_5, self.cell_4_6, self.cell_5_4, self.cell_5_5, self.cell_5_6, self.cell_6_4, self.cell_6_5, self.cell_6_6)
        self.group24 = Group('Grid', self.cell_4_7, self.cell_4_8, self.cell_4_9, self.cell_5_7, self.cell_5_8, self.cell_5_9, self.cell_6_7, self.cell_6_8, self.cell_6_9)
        self.group25 = Group('Grid', self.cell_7_1, self.cell_7_2, self.cell_7_3, self.cell_8_1, self.cell_8_2, self.cell_8_3, self.cell_9_1, self.cell_9_2, self.cell_9_3)
        self.group26 = Group('Grid', self.cell_7_4, self.cell_7_5, self.cell_7_6, self.cell_8_4, self.cell_8_5, self.cell_8_6, self.cell_9_4, self.cell_9_5, self.cell_9_6)
        self.group27 = Group('Grid', self.cell_7_7, self.cell_7_8, self.cell_7_9, self.cell_8_7, self.cell_8_8, self.cell_8_9, self.cell_9_7, self.cell_9_8, self.cell_9_9)

        self.cells = [
            self.cell_1_1, self.cell_1_2, self.cell_1_3, self.cell_1_4, self.cell_1_5, self.cell_1_6, self.cell_1_7, self.cell_1_8, self.cell_1_9, 
            self.cell_2_1, self.cell_2_2, self.cell_2_3, self.cell_2_4, self.cell_2_5, self.cell_2_6, self.cell_2_7, self.cell_2_8, self.cell_2_9, 
            self.cell_3_1, self.cell_3_2, self.cell_3_3, self.cell_3_4, self.cell_3_5, self.cell_3_6, self.cell_3_7, self.cell_3_8, self.cell_3_9, 
            self.cell_4_1, self.cell_4_2, self.cell_4_3, self.cell_4_4, self.cell_4_5, self.cell_4_6, self.cell_4_7, self.cell_4_8, self.cell_4_9, 
            self.cell_5_1, self.cell_5_2, self.cell_5_3, self.cell_5_4, self.cell_5_5, self.cell_5_6, self.cell_5_7, self.cell_5_8, self.cell_5_9, 
            self.cell_6_1, self.cell_6_2, self.cell_6_3, self.cell_6_4, self.cell_6_5, self.cell_6_6, self.cell_6_7, self.cell_6_8, self.cell_6_9, 
            self.cell_7_1, self.cell_7_2, self.cell_7_3, self.cell_7_4, self.cell_7_5, self.cell_7_6, self.cell_7_7, self.cell_7_8, self.cell_7_9, 
            self.cell_8_1, self.cell_8_2, self.cell_8_3, self.cell_8_4, self.cell_8_5, self.cell_8_6, self.cell_8_7, self.cell_8_8, self.cell_8_9, 
            self.cell_9_1, self.cell_9_2, self.cell_9_3, self.cell_9_4, self.cell_9_5, self.cell_9_6, self.cell_9_7, self.cell_9_8, self.cell_9_9
        ]

        self.groups = [
            self.group1,
            self.group2,
            self.group3,
            self.group4,
            self.group5,
            self.group6,
            self.group7,
            self.group8,
            self.group9,
            self.group10,
            self.group11,
            self.group12,
            self.group13,
            self.group14,
            self.group15,
            self.group16,
            self.group17,
            self.group18,
            self.group19,
            self.group20,
            self.group21,
            self.group22,
            self.group23,
            self.group24,
            self.group25,
            self.group26,
            self.group27
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
                # if grid.grid[i][j]:
                ret += str(grid.grid[i][j]) + ' '
                # else:
                #     ret += ' ' + ' '
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

    def fill(self, grid, number):
        if number in self.choices:
            self.choices = []
            self.number = number
            grid.updateGrid(self)
            for group in grid.groups:
                if self in group.cells:
                    group.removeCell(self)
                    for cell in group.cells:
                        if number in cell.choices:
                            cell.clear_choice(number)
            grid.cells.remove(self)
        else:
            raise Exception('')
    
    def updateNumber(self, number):
        self.choices = []
        self.number = number
        for group in grid.groups:
            if self in group.cells:
                group.removeCell(self)
                for cell in group.cells:
                    if number in cell.choices:
                        cell.clear_choice(number)
        grid.cells.remove(self)
    
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
    
    def cellsWithChoice(self, number):
        ret = []
        for cell in self.cells:
            if number in cell.choices:
                ret.append(cell)
        return ret

def updateCells(grid):
    for i in range(9):
        for j in range(9):
            if grid.grid[i][j] != 0:
                number = grid.grid[i][j]
                for cell in grid.cells:
                    if cell.coord == (i, j):
                        cell.updateNumber(number)
                
# def cellsdeepcopy(cells):
#     cells1 = []
#     for cell in cells:
#         cells1.append(copy.deepcopy(cell))
#     return cells1

# def groupsdeepcopy(cells):
#     groups1 = []
#     for cell in groups:
#         groups1.append(copy.deepcopy(cell))
#     return groups1
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

noChangeCount = 0
noChange = True

def attempt(grid,noChange, noChangeCount):
    while(not grid.solved() and noChangeCount <= 10):
        noChange = True
        for cell in grid.cells:
            print(cell)
            if len(cell.choices) == 1:
                cell.fill(grid, cell.choices[0])
                noChange = False
                noChangeCount = 0

        for number in range(1, 10):
            for group in grid.groups:
                cells_with_number_as_choice = group.cellsWithChoice(number)
                if len(cells_with_number_as_choice) == 1:
                    cells_with_number_as_choice[0].fill(grid, number)
                    noChange = False
                    noChangeCount = 0

        for number in range(1, 10):
            for group in grid.groups:
                if not group.isFilled(number):
                    for group1 in grid.groups:
                        if set(group.getCells(number)) <= set(group1.cells):
                            for cell in set(group1.cells) - set(group.getCells(number)):
                                if number in cell.choices:
                                    cell.choices.remove(number)
                                    noChange = False
                                    noChangeCount = 0
        if noChange:
            noChangeCount += 1
        for group in grid.groups:
            if len(group.cells) == 0:
                grid.groups.remove(group)

def trial(grid, noChange, noChangeCount):
    list_of_no_of_choices = []
    for cell in grid.cells:
        list_of_no_of_choices.append(len(cell.choices))
    cell = grid.cells[list_of_no_of_choices.index(max(list_of_no_of_choices))]
    for choice in cell.choices:
        grid1 = Grid()
        grid1 = copy.deepcopy(grid)
        # cells1 = cellsdeepcopy(cells)
        # groups1 = groupsdeepcopy(groups)
        try:
            cell.fill(grid1, choice)
            attempt(grid1, noChange, noChangeCount)
            if not grid.solved():
                print('Guessing...')
                noChange = True
                noChangeCount = 0
                trial(grid1, noChange, noChangeCount)
            grid = grid1
            break
        except:
            continue

updateCells(grid)

attempt(grid, noChange, noChangeCount)

noChange = True
noChangeCount = 0
if not grid.solved():
    print('Guessing...')
    trial(grid, noChange, noChangeCount)


if (not grid.solved()):
    print()
    print('I couldn\'t solve it completely!😔😞')
    print(grid)
    for cell in grid.cells:
        print(cell)
else:
    print(grid)