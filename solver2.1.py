import copy

EMPTY = ' '

class Grid():

    # Our workspace
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

    # Choices
    choices = {
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

    # The Groups
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

    # Make it better
    def __str__(self) -> str:
        ret = '___________________\n'
        for i in range(9):
            for j in range(9):
                if self.grid[i][j]:
                    ret += str(self.grid[i][j]) + '|'
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
            for j in self.grid[i]:
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
        
    def fill(self, i, j, number):
        if number in self.choices[f'cell{i}{j}']:
            self.choices[f'cell{i}{j}'] = []
            self.grid[i][j] = number

            cell = (i, j)
            for group in self.groups:
                if cell in group:
                    group.remove(cell)
                    for cell1 in group:
                        choices = self.choices[f'cell{cell1[0]}{cell1[1]}']
                        if len(choices) != 0 and number in choices:
                            choices.remove(number)
            self.choices.pop(f'cell{cell[0]}{cell[1]}')
        else:
            raise Exception('Wrong NUMBER')
    
    def updateCell(self, i, j, number):
        self.choices[f'cell{i}{j}'] = []
        for group in self.groups:
            if len(group) != 0 and (i, j) in group:
                group.remove((i, j))
                for cell in group:
                    choices = self.choices[f'cell{cell[0]}{cell[1]}']
                    if len(choices) != 0 and number in choices:
                        choices.remove(number)
        self.choices.pop(f'cell{i}{j}')
     
    def update(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] != 0:
                    number = self.grid[i][j]
                    self.updateCell(i, j, number)

    def cellsWithChoice(self, group, number):
        cellsWithChoice = []

        for cell in group:
            try:
                if number in self.choices[f'cell{cell[0]}{cell[1]}']:
                    cellsWithChoice.append(cell)
            except:
                continue
        return cellsWithChoice
    
    def isFilled(self, group, number):
        for cell in group:
            if self.grid[cell[0]][cell[1]] == number:
                return True
        return False

    def attempt(self):
        noChangeCount = 0
        noChange = True

        while((not self.solved()) and noChangeCount <= 10):
            noChange = True
            i = 0
            for i in range(9):
                for j in range(9):
                    try:
                        if len(self.choices[f'cell{i}{j}']) != 0:
                            if len(self.choices[f'cell{i}{j}']) == 1:
                                self.fill(i, j, self.choices[f'cell{i}{j}'][0])
                                noChange = False
                                noChangeCount = 0
                    except:
                        continue
                
            # for cell in self.cells:
            #     print(cell)

            for number in range(1, 10):
                for group in self.groups:
                    if len(group) == 0:
                        continue
                    cells_with_number_as_choice = self.cellsWithChoice(group, number)
                    if len(cells_with_number_as_choice) == 1:
                        # print(cells_with_number_as_choice[0])
                        self.fill(cells_with_number_as_choice[0][0], cells_with_number_as_choice[0][1], number)
                        noChange = False
                        noChangeCount = 0
            
            # for cell in self.cells:
            #     print(cell)
            
            for number in range(1, 10):
                for group in self.groups:
                    if len(group) == 0:
                        continue
                    if not self.isFilled(group, number):
                        if len(group) == 0:
                            continue
                        for group1 in self.groups:
                            if len(group1) == 0:
                                continue
                            if set(self.cellsWithChoice(group, number)) <= set(group1):
                                for cell in set(group1) - set(self.cellsWithChoice(group, number)):
                                    if len(self.choices[f'cell{cell[0]}{cell[1]}']) == 0:
                                        continue
                                    if number in self.choices[f'cell{cell[0]}{cell[1]}']:
                                        self.choices[f'cell{cell[0]}{cell[1]}'].remove(number)
                                        noChange = False
                                        noChangeCount = 0
            if noChange:
                noChangeCount += 1
            print(self.solved(), noChange,  noChangeCount, sep = " ")

    def possibleChildren(self):
        print(self)
        print(self.choices)
        for h in range(1, 10):
            x = []
            for i in range(9):
                for j in range(9):
                    try:
                        if len(self.choices[f'cell{i}{j}']) == h:
                            x.append((i, j))
                    except:
                        continue
            if len(x) != 0:
                break
        
        cell = x[0]
        returning_list = []

        for i in self.choices[f'cell{cell[0]}{cell[1]}']:
            grid = Grid()
            grid = self
            grid.grid[cell[0]][cell[1]] = i
            grid.update()
            returning_list.append(grid)

        return returning_list

class Stack():

    stack = []

    def add(self, nodes):
        for node in nodes:
            self.stack.append(node)
    
    def len(self):
        return len(self.stack)

    def pop(self):
        ret = self.stack[self.len() - 1]
        self.stack.pop(self.len() - 1)
        return ret
    
    def solve(self):
        node = self.pop()
        if node.solved():
            return node.state
        node.attempt()
        children = node.possibleChildren()
        adding_list = []
        for child in children:
            adding_list.append(child)
        self.add(adding_list)
        self.solve()
   
grid = Grid()

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

grid.update()
grid.attempt()
print(grid.choices)

if (not grid.solved()):

    stack = Stack()

    print(grid.choices)

    stack.add([grid])

    stack.solve()

    print()
    print('I couldn\'t solve it completely!😔😞')
    print(grid)
    print(grid.reattemptable())
else:
    print(grid)