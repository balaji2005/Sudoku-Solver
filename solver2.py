import copy

EMPTY = ' '

class Grid:

    grid = [
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

    cells = {
        (0, 0): 0,
        (0, 1): 0,
        (0, 2): 0,
        (0, 3): 0,
        (0, 4): 0,
        (0, 5): 0,
        (0, 6): 0,
        (0, 7): 0,
        (0, 8): 0,
        (1, 0): 0,
        (1, 1): 0,
        (1, 2): 0,
        (1, 3): 0,
        (1, 4): 0,
        (1, 5): 0,
        (1, 6): 0,
        (1, 7): 0,
        (1, 8): 0,
        (2, 0): 0,
        (2, 1): 0,
        (2, 2): 0,
        (2, 3): 0,
        (2, 4): 0,
        (2, 5): 0,
        (2, 6): 0,
        (2, 7): 0,
        (2, 8): 0,
        (3, 0): 0,
        (3, 1): 0,
        (3, 2): 0,
        (3, 3): 0,
        (3, 4): 0,
        (3, 5): 0,
        (3, 6): 0,
        (3, 7): 0,
        (3, 8): 0,
        (4, 0): 0,
        (4, 1): 0,
        (4, 2): 0,
        (4, 3): 0,
        (4, 4): 0,
        (4, 5): 0,
        (4, 6): 0,
        (4, 7): 0,
        (4, 8): 0,
        (5, 0): 0,
        (5, 1): 0,
        (5, 2): 0,
        (5, 3): 0,
        (5, 4): 0,
        (5, 5): 0,
        (5, 6): 0,
        (5, 7): 0,
        (5, 8): 0,
        (6, 0): 0,
        (6, 1): 0,
        (6, 2): 0,
        (6, 3): 0,
        (6, 4): 0,
        (6, 5): 0,
        (6, 6): 0,
        (6, 7): 0,
        (6, 8): 0,
        (7, 0): 0,
        (7, 1): 0,
        (7, 2): 0,
        (7, 3): 0,
        (7, 4): 0,
        (7, 5): 0,
        (7, 6): 0,
        (7, 7): 0,
        (7, 8): 0,
        (8, 0): 0,
        (8, 1): 0,
        (8, 2): 0,
        (8, 3): 0,
        (8, 4): 0,
        (8, 5): 0,
        (8, 6): 0,
        (8, 7): 0,
        (8, 8): 0
    }

    def __init__(self):
        pass
        
    # Updates the grid to the input
    def update(self):
        i = 0
        while i < len(self.cells):
            x = self.cells[i]
            if grid.grid[x.coord[0]][x.coord[1]] != 0:
                self.cells.remove(x)
                for group in self.groups:
                    if cell in group.cells:
                        group.cells.remove(cell)
                i -= 1
            i += 1
        i = 0

        while i < len(self.groups):
            x = self.groups[i]
            if len(x.cells) == 0:
                self.groups.remove(x)
        
    # Updates the number of the grid when the AI tries to fill it
    def updateGrid(self, cell):
        node = (cell.coord[0], cell.coord[1])
        number = cell.number
        self.grid[node[0]][node[1]] = number
        print(self, node[0], self.grid, sep = " ")
        print(f'Entering {number} to {node}')

    # Made it better
    def __str__(self) -> str:
        ret = '___________________\n'
        for i in range(9):
            for j in range(9):
                if grid.grid[i][j]:
                    ret += str(grid.grid[i][j]) + '|'
                else:
                    ret += EMPTY + '|'
                if j in {2, 5}:
                    ret += ' '
            ret+='\n'
            # if i in {2, 5}:
            #     ret += '\n'
        ret += '___________________\n'
        return ret
    
    # Checks whether the grid is completely filled
    def solved(self):
        for i in range(9):
            for j in grid.grid[i]:
                if j == 0:
                    return False
        return True
    
    # Gives a version of the puzzle that can be inputted into the code again
    def reattemptable(self) -> str:
        ret = '___________________\n'
        for i in range(9):
            for j in range(9):
                ret += str(grid.grid[i][j]) + ' '
            ret+='\n'
        ret += '___________________\n'
        return ret

    # Gives the Sudoku an attempt
    def attempt(self):
        noChangeCount = 0
        noChange = True
        print('attempting')
        while((not self.solved()) and noChangeCount <= 10):
            noChange = True
            i = 0
            print('printing')
            while i < len(self.cells):
                cell = self.cells[i]
                # print(cell)
                if len(cell.choices) == 1:
                    cell.fill(self, cell.choices[0])
                    i -= 1
                    noChange = False
                    noChangeCount = 0
                i += 1
            
            # for cell in self.cells:
            #     print(cell)

            for number in range(1, 10):
                for group in self.groups:
                    if len(group.cells) == 0:
                        continue
                    cells_with_number_as_choice = group.cellsWithChoice(number)
                    if len(cells_with_number_as_choice) == 1:
                        # print(cells_with_number_as_choice[0])
                        cells_with_number_as_choice[0].fill(grid, number)
                        noChange = False
                        noChangeCount = 0
            
            # for cell in self.cells:
            #     print(cell)
            
            for number in range(1, 10):
                for group in self.groups:
                    if len(group.cells) == 0:
                        continue
                    if not group.isFilled(number):
                        if len(group.cells) == 0:
                            continue
                        for group1 in self.groups:
                            if len(group1.cells) == 0:
                                continue
                            if set(group.cellsWithChoice(number)) <= set(group1.cells):
                                for cell in set(group1.cells) - set(group.cellsWithChoice(number)):
                                    if len(cell.choices) == 0:
                                        continue
                                    if number in cell.choices:
                                        cell.choices.remove(number)
                                        noChange = False
                                        noChangeCount = 0
            if noChange:
                noChangeCount += 1
            print(self.solved(), noChange,  noChangeCount, sep = " ")
    
    # Gives the Sudoku a try with a guess
    def trial(self):
        list_of_no_of_choices = []
        print("trial")
        print(self)
        for cell in self.cells:
            print(cell.choices)
            list_of_no_of_choices.append(len(cell.choices))
        m = 10
        for e in list_of_no_of_choices:
            if e == 0:
                continue
            if e < m:
                m = e
        print(list_of_no_of_choices, m, sep = " ")
        cell = self.cells[list_of_no_of_choices.index(m)]
        print(cell)
        for choice in cell.choices:
            grid1 = self.deepcopy()
            # grid1 = self
            # cells1 = cellsdeepcopy(cells)
            # groups1 = groupsdeepcopy(groups)
            print('trial....')
            print(grid1, self, sep = " ")
            try:
                # print('Guessing...')
                cell.fill(grid1, choice)
                grid1.attempt()
                print('is solved')
                print(grid.solved())
                if not grid1.solved():
                    print(grid1)
                    # for cell in grid1.cells:
                        # print(cell.choices)
                    print('trailing...')
                    grid1.trial()
                self = copy.copy(grid1)
                break
            except:
                continue

    # Tries to make a deepcopy of this object
    def deepcopy(self):
        grid = Grid()
        grid.grid = self.grid
        grid.update()
        for i in range(len(grid.cells)):
            grid.cells[i].number = self.cells[i].number
            grid.cells[i].choices = self.cells[i].choices
        for cell in grid.cells:
            print(cell.choices, cell.number, sep = " ")
        return grid

class Cell:
    def __init__(self, i, j):
        self.coord = (i, j)
        self.choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.number = 0

    def __str__(self):
        return str(self.coord) + ' = ' + str(self.choices)
    
    # Clears the choice 
    def clear_choice(self, number):
        self.choices.remove(number)

    # Fills the cell with a number
    def fill(self, grid, number):
        if number in self.choices:
            self.choices = []
            self.number = number
            grid.updateGrid(self)
            print('updating...')
            # print(grid)
            for group in grid.groups:
                if self in group.cells:
                    group.removeCell(self)
                    for cell in group.cells:
                        if len(cell.choices) == 0:
                            continue
                        if number in cell.choices:
                            cell.clear_choice(number)
            # print(grid)
            grid.cells.remove(self)
        else:
            raise Exception('')
    
    # Updates the number in a cell according to the input
    def updateNumber(self, number):
        self.choices = []
        self.number = number
        for group in grid.groups:
            if len(group.cells) == 0:
                continue
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
    
    # Removes a cell from the group
    def removeCell(self, cell):
        self.cells.remove(cell)
        self.filledNumbers.append(cell.number)
        for otherCell in self.cells:
            if cell.number in otherCell.choices:
                otherCell.choices.remove(cell.number)

    # Checks whether a number is already filled in the group
    def isFilled(self, number):
        if number in self.filledNumbers:
            return True
        return False
    
    # List of cells with a number as choice
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

updateCells(grid)

grid.attempt()

for cell in grid.cells:
    print(cell)

if not grid.solved():
    print(grid)
    # print('Guessing...')
    grid.trial()

if (not grid.solved()):
    print()
    print('I couldn\'t solve it completely!😔😞')
    print(grid)
    print(grid.reattemptable())
    # for cell in grid.cells:
    #     print(cell)
else:
    print(grid)