__author__ = 'santosh'

import Board

def manhattanDistance(node):

    # Returns the manhattan distance of each of the pegs from the center

    distance = 0
    for x in range(7):
        for y in range(7):
            if(node.config[x][y] == Board.Board.PEG):
                distance += abs(x-3) + abs(y-3)
    return distance



def weightedCostMatrix(node):

    weightedCost = 0

    costMatrix=[[0, 0, 4, 0, 4, 0, 0],[0, 0, 0, 0, 0, 0, 0],[4, 0, 3, 0, 3, 0, 4 ],[0, 0, 0, 1, 0, 0, 0],[4, 0, 3, 0, 3, 0, 4 ],[0, 0, 0, 0, 0, 0, 0],[0, 0, 4, 0, 4, 0, 0]]



    for i in range(7):
        for j in range(7):
            if(node.config[i][j] == Board.Board.PEG):
                weightedCost += costMatrix[i][j]

    return weightedCost
