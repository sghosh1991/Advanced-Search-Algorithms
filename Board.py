__author__ = 'Santosh'

import copy
from heuristic import *


class Board:
    PEG = 'X'
    INVALID = '-'
    EMPTY = '0'


    def __init__(self, config, parent):
        """

        :rtype : Board
        """
        # print("In init")
        self.config = config
        self.parent = parent
        if (parent is None):
            # print("Parent is none")
            self.pathCost = 0
        else:

            self.pathCost = parent.pathCost + 1
        self.key = ''.join([''.join(x) for x in config])
        self.heuristicCost = 1
        self.totalCost = self.pathCost + self.heuristicCost
        # print("At init end Value of total cost" + str(self.totalCost))

    def __hash__(self):
        print("In hash")
        return hash(self.key)

    def __eq__(self, other):
        #print("In eq" + str(type(other)))
        return (self.config == other.config)

    def __lt__(self, other):
        return self.totalCost < other.totalCost

    def __str__(self):
        stringToReturn = ''
        for i in range(7):
            # print('\n')
            for j in self.config[i]:
                # rint(j + " ", end="")
                stringToReturn = stringToReturn + j + " "
            stringToReturn = stringToReturn + "\n"
        return stringToReturn

    def getKey(self):
        print("GetKey not implemented")
        return self.key


def invalidPosition(x, y):
    #print("x=" + str(x) + " y= " + str(y))
    if (x < 0 or x >= 7 or y < 0 or y >= 7):
        #print("Out of board")
        return True
    elif (x < 2 and y < 2) or (x > 4 and y < 2) or (x < 2 and y > 4 ) or (x > 4 and y > 4):
        #print("out of bounds")
        return True

    return False


# def move(self,x,y,dx,dy):
# self.config[]

def validmove(x, y, dx, dy, currBoard):
    stepx = int(x + dx / 2)
    stepy = int(y + dy / 2)
    jumpx = x + dx
    jumpy = y + dy

    if invalidPosition(x, y) or invalidPosition(stepx, stepy) or invalidPosition(jumpx, jumpy):
        #print("Invalid Position")
        return False

    initPos = currBoard.config[x][y]
    skipPos = currBoard.config[stepx][stepy]
    finalPos = currBoard.config[jumpx][jumpy]

    # print("\ninitial position.. x = " + str(x) + " y = " + str(y) + " Value = " + str(initPos))
    # print("skip position.. stepx = " + str(stepx) + " stepy = " + str(stepy) + " Value = " + str(skipPos))
    # print("Final position.. jumpx = " + str(jumpx) + " jumpy = " + str(jumpy) + " Value = " + str(finalPos) + "\n")

    #print(Board.PEG)

    if (initPos == Board.INVALID or initPos == Board.EMPTY or finalPos == Board.INVALID or finalPos == Board.PEG or skipPos == Board.EMPTY or skipPos == Board.INVALID):
        #print("No move possible")
        return False

    return True


def move(x, y, dx, dy, parent):
    #print("In move... ")
    # create the config of the neighbour from the parent
    newBoardConfig = copy.deepcopy(parent.config)

    #print(parent)
    #print("neconfig is parentconfig? " + str(newBoardConfig is parent.config))
    #print("neconfig == parentconfig? " + str(newBoardConfig == parent.config))

    # modify the config value
    newBoardConfig[x][y] = Board.EMPTY
    newBoardConfig[int(x + dx / 2)][int(y + dy / 2)] = Board.EMPTY
    newBoardConfig[x + dx][y + dy] = Board.PEG

    #print(parent)
    # create the board config object
    neighbour = Board(newBoardConfig, parent)
    # neighbour.heuristicCost = weightedCostMatrix(neighbour)
    neighbour.heuristicCost = manhattanDistance(neighbour)
    neighbour.totalCost = neighbour.pathCost + neighbour.heuristicCost

    #print("neighbours parent \n" + str(neighbour.parent))

    #print(parent)

    return neighbour


def checkGoalState(boardConfig):
    #If board config is goal return True
    #print("Check goal state")

    numOfPEGS = 0

    if not (boardConfig.config[3][3] == Board.PEG):
        return False
    else:
        for i in range(7):
            for j in range(7):
                if boardConfig.config[i][j] == Board.PEG:
                    numOfPEGS += 1
                    if numOfPEGS > 1:
                        #print("Number of pegs is :" + str(numOfPEGS))
                        return False

    return True



if __name__ == '__main__':
    boardCfg = ['--XXX--', '--XXX--', 'XXXXXXX', 'XXX0XXX', 'XXXXXXX', '--XXX--', '--XXX--']
    board = Board(boardCfg)
    board.printBoard()
    # __main__();
