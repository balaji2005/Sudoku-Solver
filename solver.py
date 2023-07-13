class Sentence:

    def __init__(self, nodes, numbers):
        self.nodes = nodes
        self.numbers = numbers

    def __str__(self):
        return str(self.nodes) + ' = ' + str(self.numbers)
    
    def remove(self, tup):
        self.nodes -= {tup[0]}
        self.numbers -= {tup[1]}

    def check(self):
        if len(self.nodes) == len(self.numbers):
            return True
        return False

class Grid():

    def __init__(self):
        self.grid = [[0, 0, 0,   0, 0, 0,   0, 0, 0],
                     [0, 0, 0,   0, 0, 0,   0, 0, 0],
                     [0, 0, 0,   0, 0, 0,   0, 0, 0],
 
                     [0, 0, 0,   0, 0, 0,   0, 0, 0],
                     [0, 0, 0,   0, 0, 0,   0, 0, 0],
                     [0, 0, 0,   0, 0, 0,   0, 0, 0],

                     [0, 0, 0,   0, 0, 0,   0, 0, 0],
                     [0, 0, 0,   0, 0, 0,   0, 0, 0],
                     [0, 0, 0,   0, 0, 0,   0, 0, 0]]
        
    def enter(self, node, number):
        self.grid[node[0]][node[1]] = number

    # Make it better
    def __str__(self) -> str:
        ret = '___________________\n'
        for i in range(9):
            for j in range(9):
                ret += str(grid.grid[i][j]) + ' '
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

def checkKnowledge(knowledge):
    for sentence in knowledge:
        if not sentence.check():
            return False
    return True

# Always i < j
def compare(i, j, knowledge, grid, nothingToCompare):
    if len(knowledge[i].nodes.intersection(knowledge[j].nodes)) == len(knowledge[i].numbers.intersection(knowledge[j].numbers)) and len(knowledge[i].nodes.intersection(knowledge[j].nodes)) > 0:
        sentence = Sentence(knowledge[i].nodes.intersection(knowledge[j].nodes), knowledge[i].numbers.intersection(knowledge[j].numbers))
        knowledge.append(sentence)
        knowledge[i] = Sentence(knowledge[i].nodes - sentence.nodes,  knowledge[i].numbers - sentence.numbers)
        knowledge[j] = Sentence(knowledge[j].nodes - sentence.nodes,  knowledge[j].numbers - sentence.numbers)

        if (len(knowledge[j].nodes) == 1):
            # print('Deleted1')
            grid.enter(list(knowledge[j].nodes)[0], list(knowledge[j].numbers)[0])
            updateNode(knowledge, list(knowledge[j].nodes)[0], list(knowledge[j].numbers)[0])
            del knowledge[j]
        if (len(knowledge[i].nodes) == 1):
            # print('Deleted2')
            # print(i, j)
            # for sentence in knowledge:
            #     print(sentence)
            # print(knowledge[i])
            grid.enter(list(knowledge[i].nodes)[0], list(knowledge[i].numbers)[0])
            updateNode(knowledge, list(knowledge[i].nodes)[0], list(knowledge[i].numbers)[0])
            del knowledge[i]
        
        if (len(knowledge[j].nodes) == 0):
            del knowledge[j]
        if (len(knowledge[i].nodes) == 0):
            del knowledge[i]
        nothingToCompare = False

def updateKnowledge(knowledge, grid):
    gr = []
    for i in range(9):
        for j in range(9):
            if grid.grid[i][j] != 0:
                gr.append(((i, j), grid.grid[i][j]))
    for sentence in knowledge:
        for i in range(len(gr)):
            if gr[i][0] in sentence.nodes:
                sentence.remove(gr[i])

def updateNode(knowledge, node, number):
    for sentence in knowledge:
        if node in sentence.nodes:
            sentence.remove((node, number))

# Starting the Player
grid = Grid()

grid.grid = [
    [1, 2, 9,   0, 8, 3,   4, 0, 7],
    [6, 0, 0,   0, 1, 5,   0, 0, 0],
    [0, 7, 5,   0, 2, 4,   6, 1, 8],

    [4, 9, 0,   0, 0, 0,   0, 7, 6],
    [0, 3, 7,   0, 4, 0,   0, 0, 0],
    [0, 0, 0,   1, 0, 0,   3, 0, 0],

    [0, 0, 0,   2, 6, 0,   7, 0, 5],
    [9, 0, 0,   0, 7, 0,   0, 0, 0],
    [0, 0, 2,   4, 0, 0,   0, 3, 1]
]

print(grid)

knowledge = [

    # Knowledge about rows
    Sentence(
        {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8)},
        {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
    ),
    Sentence(
        {(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)},
        {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
    ),
    Sentence(
        {(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8)},
        {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
    ),
    Sentence(
        {(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8)},
        {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
    ),
    Sentence(
        {(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8)},
        {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
    ),
    Sentence(
        {(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8)},
        {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
    ),
    Sentence(
        {(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8)},
        {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
    ),
    Sentence(
        {(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8)},
        {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
    ),
    Sentence(
        {(8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)},
        {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
    ),

    # Knowledge about columns
    Sentence(
        {(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)},
        {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
    ),
    Sentence(
        {(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)},
        {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
    ),
    Sentence(
        {(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2)},
        {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
    ),
    Sentence(
        {(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3)},
        {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
    ),
    Sentence(
        {(0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4)},
        {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
    ),
    Sentence(
        {(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)},
        {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
    ),
    Sentence(
        {(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6)},
        {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
    ),
    Sentence(
        {(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7)},
        {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
    ),
    Sentence(
        {(0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8)},
        {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
    ),

    # Knowledge about first column of 3x3 grids
    Sentence(
        {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)},
        {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
    ),
    Sentence(
        {(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)},
        {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
    ),
    Sentence(
        {(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)},
        {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
    ),

    # Knowledge about second column of 3x3 grids
    Sentence(
        {(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)},
        {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
    ),
    Sentence(
        {(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)},
        {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
    ),
    Sentence(
        {(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)},
        {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
    ),

    # Knowledge about third column of 3x3 grids
    Sentence(
        {(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)},
        {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
    ),
    Sentence(
        {(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)},
        {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
    ),
    Sentence(
        {(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)},
        {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9}
    )
]

updateKnowledge(knowledge, grid)

# print(checkKnowledge(knowledge))

# for sentence in knowledge:
#     print(sentence)

nothingToCompare = False

while (not grid.solved()):
    for i in range(len(knowledge)):
        # print(grid)
        if i < len(knowledge):
            if len(knowledge[i].nodes) == 1:
                grid.enter(list(knowledge[i].nodes)[0], list(knowledge[i].numbers)[0])
                updateNode(knowledge, list(knowledge[i].nodes)[0], list(knowledge[i].numbers)[0])
                del knowledge[i]
                continue
            for j in range(len(knowledge)):
                if i > j and i < len(knowledge):
                    compare(j, i, knowledge, grid, nothingToCompare)
                elif j > i and j < len(knowledge):
                    compare(i, j, knowledge, grid, nothingToCompare)

print(grid)