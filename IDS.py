from itertools import starmap

__author__ = 'santosh'

from Board import *
import sys
import time

openList = list()
closeList = list()

numberOfNodes = 0

CUTOFF = 1
GOAL_FOUND = 2
DEADEND = 3

terminationCause = CUTOFF



def depthLimitedSearch(startNode, bound):
    # put the startnode in closeList as this node is now processed

    global closeList
    global terminationCause
    global openList
    global numberOfNodes

    numberOfNodes += 1
    closeList.append(startNode)
    result=False

    #print("Bound Level =" +str(bound))

    if (bound == 0 and checkGoalState(startNode)):
        terminationCause = GOAL_FOUND
        return True

    if bound > 0:

        #print("Expanding at bound= " + str(bound) + "\n" + str(startNode))
        neighbourList = generateNeighbours(startNode)
        #print("\nPrinting neighbour List...Length of neighbourList = " + str(neighbourList.__len__()))

        # for i in neighbourList:
        #  print(i)



        for x in neighbourList:
            #print("Recursively expanding...\n" + str(x))
            result = result or depthLimitedSearch(x, bound - 1)
            if (terminationCause == GOAL_FOUND):
                return True
    else:

        #print("Checking neighbour exists or not")
        neighbourList = generateNeighbours(startNode)

        if neighbourList.__len__() > 0:
            terminationCause = CUTOFF
            return True
        else:
            terminationCause = DEADEND
            return False


    return result


def generateNeighbours(parent):
    neighbourList = list()

    neighbour=""
    global openList
    deltas = [[-2, 0], [2, 0], [0, -2], [0, 2]]

    neighboursGenerated = 0
    for x in range(7):
        for y in range(7):


            for delta in deltas:
                dx = delta[0]
                dy = delta[1]
                # print("Trying with")
                # print("x = " + str(x) + " dx = " + str(dx))
                # print("y = " + str(y) + " dy = " + str(dy))

                if (validmove(x, y, dx, dy,parent)):
                    #print("Move validated")
                    neighbour = move(x, y, dx, dy, parent)
                    neighboursGenerated = neighboursGenerated + 1
                    #print("Neighbour Generated :\n" + str(neighbour))

                    if neighbour not in openList:
                        #print("Not in openList")
                        openList.append(neighbour)
                        neighbourList.append(neighbour)
                        #print(neighbourList)


    #print("\nPrinting neighbour List...Length of neighbourList = " + str(neighbourList.__len__()))

    # for i in neighbourList:
    #     print(i)
    return neighbourList




def IDS(startState):

    startBoardConfig = Board(startState,None)

    global terminationCause
    global openList
    global numberOfNodes

    terminationCause = CUTOFF
    bound = 0

    result=True

    while (result):

        numberOfNodes = 0
        openList.clear()
        openList.append(startBoardConfig)
        closeList.clear()

        result = depthLimitedSearch(startBoardConfig,bound)

        #print("terminationCause " + str(result))

        if terminationCause == GOAL_FOUND:
            print("Goal Reached..print state at depth" + str(bound))
            break

        bound += 1

    if terminationCause == DEADEND:
        print("No Goal Possible from this node")



    print("\n\nClose List Lenghth " + str(len(closeList)))

    path=list()
    goal = closeList[len(closeList)-1]
    while(goal is  not None):
        path.append(goal)
        goal = goal.parent

    # for i in reversed(path):
    #     print(i)



    print("\n\n===========Summary stats=================\n\n")
    print("Memory needed: " + str(numberOfNodes))


if __name__ == "__main__":

    startTime = time.time()
    boardCfg = [['-', '-', '0', '0', '0', '-', '-'], ['-', '-', '0', 'X', '0', '-', '-'], ['0', '0', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', '0', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X'], ['-', '-', 'X', 'X', 'X', '-', '-'], ['-', '-', 'X', 'X', 'X', '-', '-']]
    goalCfg = [['-', '-', '0', '0', '0', '-', '-'], ['-', '-', '0', 'X', '0', '-', '-'], ['0', 'X', 'X', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0'], ['-', '-', '0', '0', '0', '-', '-'], ['-', '-', '0', '0', '0', '-', '-']]
    test = [['-', '-', '0', '0', '0', '-', '-'], ['-', '-', '0', 'X', '0', '-', '-'], ['0', '0', 'X', 'X', 'X', '0', '0'], ['0', '0', '0', 'X', '0', '0', '0'], ['0', '0', '0', 'X', '0', '0', '0'], ['-', '-', '0', '0', '0', '-', '-'], ['-', '-', '0', '0', '0', '-', '-']]
    test2 = [['-', '-', 'X', 'X', 'X', '-', '-'], ['-', '-', 'X', 'X', 'X', '-', '-'], ['X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', '0', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X'], ['-', '-', 'X', 'X', 'X', '-', '-'], ['-', '-', 'X', 'X', 'X', '-', '-']]
    x = Board(test,None)
    #print(str(x))
    IDS(test)
    print("Total time needed : " + str(time.time() - startTime) + " seconds")
