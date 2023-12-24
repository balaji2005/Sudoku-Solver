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
        "cell00": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell01": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell02": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell03": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell04": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell05": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell06": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell07": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell08": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell10": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell11": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell12": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell13": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell14": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell15": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell16": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell17": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell18": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell20": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell21": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell22": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell23": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell24": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell25": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell26": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell27": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell28": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell30": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell31": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell32": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell33": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell34": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell35": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell36": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell37": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell38": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell40": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell41": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell42": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell43": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell44": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell45": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell46": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell47": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell48": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell50": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell51": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell52": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell53": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell54": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell55": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell56": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell57": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell58": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell60": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell61": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell62": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell63": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell64": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell65": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell66": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell67": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell68": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell70": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell71": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell72": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell73": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell74": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell75": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell76": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell77": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell78": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell80": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell81": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell82": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell83": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell84": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell85": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell86": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell87": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "cell88": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    }

    groups = [
        # Rows
        [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8)],
        [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)],
        [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8)],
        [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8)],
        [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8)],
        [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8)],
        [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8)],
        [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8)],
        [(8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)],

        # Columns
        [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)],
        [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)],
        [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2)],
        [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3)],
        [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4)],
        [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)],
        [(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6)],
        [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7)],
        [(0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8)],

        # Grids
        [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)],
        [(0, 3), (1, 3), (2, 3), (0, 4), (1, 4), (2, 4), (0, 5), (1, 5), (2, 5)],
        [(0, 6), (1, 6), (2, 6), (0, 7), (1, 7), (2, 7), (0, 8), (1, 8), (2, 8)],
        [(3, 0), (4, 0), (5, 0), (3, 1), (4, 1), (5, 1), (3, 2), (4, 2), (5, 2)],
        [(3, 3), (4, 3), (5, 3), (3, 4), (4, 4), (5, 4), (3, 5), (4, 5), (5, 5)],
        [(3, 6), (4, 6), (5, 6), (3, 7), (4, 7), (5, 7), (3, 8), (4, 8), (5, 8)],
        [(6, 0), (7, 0), (8, 0), (6, 1), (7, 1), (8, 1), (6, 2), (7, 2), (8, 2)],
        [(6, 3), (7, 3), (8, 3), (6, 4), (7, 4), (8, 4), (6, 5), (7, 5), (8, 5)],
        [(6, 6), (7, 6), (8, 6), (6, 7), (7, 7), (8, 7), (6, 8), (7, 8), (8, 8)]
    ]

    # Updates the number of the grid when the AI tries to fill it
    # def updateGrid(self, cell):
    #     node = (cell.coord[0], cell.coord[1])
    #     number = cell.number
    #     self.grid[node[0]][node[1]] = number
    #     print(self, node[0], self.grid, sep = " ")
    #     print(f'Entering {number} to {node}')

    # Make it better
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

    # Clears a choice for a cell
    def clear_choice(self, i, j, number):
        if number in self.cells[f'cell{i}{j}']:
            self.cells[f'cell{i}{j}'].remove(number)
        else:
            raise Exception('No CHOICE')
    
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
            raise Exception('Wrong NUMBER')
    
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
    

class Cell:
    
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

# Updates the grid for the given puzzle
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

# if not grid.solved():
#     print(grid)
#     # print('Guessing...')
#     grid.trial()

if (not grid.solved()):
    print()
    print('I couldn\'t solve it completely!😔😞')
    print(grid)
    print(grid.reattemptable())
    # for cell in grid.cells:
    #     print(cell)
else:
    print(grid)