

__author__ = 'Santosh'

from Board import *
import time
from operator import itemgetter, attrgetter, methodcaller
import sys

openList = list()
closeList = list()

nodesExpanded = 0


def aStar(startState):

    global openList
    global closeList
    global nodesExpanded

    openList.append(startState)
    failure = True

    while openList.__sizeof__() >0:
        currBoardConfig = min(openList,key=attrgetter('totalCost'))
        openList.remove(currBoardConfig)
        nodesExpanded += 1

        #print("\n Expanding \n" + str(currBoardConfig))
        if(checkGoalState(currBoardConfig)):
            print("Goal Found")
            printPath()
            failure = False
            break
        generateNeighbours(currBoardConfig)
        #print("\n...Printing open list....\n")

        # for x in openList:
        #     print(x)
        #     print("Path Cost of  this node: " + str(x.pathCost))
        #     print("Heuristic Cost of  this node: " + str(x.heuristicCost))
        #     print("Total Cost of  this node: " + str(x.totalCost))


    #out of loop means opnList is empty, So print error and exit

    if(failure):
        print("Goal state cannot be reached from this state")

    printPath()




def printPath():
    #Print the moves taken using the close list
    global closeList
    print("\n\n===========Summary stats=================\n\n")
    print("Memory needed: " + str(len(openList)))


def generateNeighbours(parent):


    global openList
    global closeList

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
                    #print("Parent before is : \n" +str(parent))
                    neighbour = move(x, y, dx, dy, parent)
                    neighboursGenerated += 1
                    #print("Parent after is : \n" +str(parent))
                    #print("Neighbour Generated :\n" + str(neighbour))
                    addNeighboursToList(neighbour,parent)

    #print("No of neighbours : " + str(neighboursGenerated))




def addNeighboursToList(neighbour,parent):

    """
    Adds the neighbour to the closeList, openList and openListLookup

    :param currentBoard:
    :param parent:
    :return:
    """
    #key= neighbour.getKey()


    global openList
    global closeList

    if( neighbour not in closeList or neighbour not in openList):

        openList.append(neighbour)

    else:

        ## Modify the f(n) and g(n) values of the neighbour



        if(neighbour in openList):

            print("neighbour already present in open list")
            oldNeighbour = getOldNeighbour(openList,neighbour)
            oldNeighbour.pathCost = min(oldNeighbour.pathCost,neighbour.pathCost)
            oldNeighbour.totalCost =  neighbour.pathCost + neighbour.heuristicCost


        elif(neighbour in closeList):
            print("neighbour already present in close list")
            oldNeighbour = getOldNeighbour(openList,neighbour)


            newPathCost = min(oldNeighbour.pathCost,neighbour.pathCost)
            newTotalCost =  newPathCost + neighbour.heuristicCost

            if(oldNeighbour.totalCost > newTotalCost):
                openList.append(oldNeighbour)
                closeList.remove(oldNeighbour)






def getOldNeighbour(list,node):

    #gets the old node from the close list. closeList is a simple List
    """

    :rtype : old node reference
    """
    print("Finding old nodes")
    for x in list:
        if x == node:
            print("Found old node")
            return node


if __name__ == '__main__':

        startTime = time.time()

        #goalCfg = [['-', '-', '0', '0', '0', '-', '-'], ['-', '-', '0', 'X', '0', '-', '-'], ['0', 'X', 'X', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0'], ['-', '-', '0', '0', '0', '-', '-'], ['-', '-', '0', '0', '0', '-', '-']]
        x1 = ['--000--','--0X0--','0XX0000','0000000','0000000','--000--','--000--']
        x2= ['--000--','--0X0--','00XXX00','000X000','000X000','--000--','--000--']
        x3 = ['--XXX--','--XXX--','XXXXXXX','XXX0XXX','XXXXXXX','--XXX--','--XXX--']
        p=[]
        for x in x3:
            k=[]
            for c in x:
                k.extend(c)
            p.append(k)

        board = Board(p,None)
        print(board)

        aStar(board)

        print("Total time needed : " + str(time.time() - startTime) + " seconds")
