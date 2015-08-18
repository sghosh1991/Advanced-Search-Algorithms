__author__ = 'Santosh'

import queue
from Board import *

from operator import itemgetter, attrgetter, methodcaller

openList = queue.PriorityQueue()

closeList = list()

openListLookUp = {}

p=list()


def getOldNeighbour(list,node):

    #gets the old node from the close list. closeList is a simple List
    print("Finding old nodes")
    for x in list:
        if x == node:
            print("Found old node")
            return node

if __name__ == "__main__":

    obj1=Board([['1', '1', 'X', 'X', 'X', '-', '-'], ['-', '-', 'X', 'P', 'X', '-', '-'], ['X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', '0', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X'], ['-', '-', 'X', 'X', 'X', '-', '-'], ['-', '-', 'X', 'X', 'X', '-', '-']],None)

    obj2=Board([['2', '2', 'X', 'X', 'X', '-', '-'], ['-', '-', 'X', 'P', 'X', '-', '-'], ['X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', '0', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X'], ['-', '-', 'X', 'P', 'P', '-', '-'], ['-', '-', 'X', 'X', 'X', '-', '-']],obj1)
    obj3=Board([['-', '-', 'X', 'X', 'X', '-', '-'], ['-', '-', 'X', 'P', 'X', '-', '-'], ['X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', '0', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X'], ['-', '-', 'X', 'X', 'X', '-', '-'], ['7', '7', '7', 'X', 'X', '-', '-']],obj2)
    obj4=Board([['-', '-', 'X', 'X', 'X', '-', '-'], ['-', '-', 'X', 'P', 'X', '-', '-'], ['X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', '0', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X'], ['-', '-', 'X', 'X', 'X', '-', '-'], ['7', '7', '7', 'X', 'X', '-', '-']],obj2)

    obj2.totalCost = 1
    p.append(obj1)
    p.append(obj2)
    p.append(obj3)
    p.append(obj4)


    minObj = min(p,key=attrgetter('totalCost'))


    print(str(minObj.totalCost) + "---->" + minObj.key)

    #minObj.totalCost=12


    for x in p:
        print(x.key + str(x.totalCost))

    p.remove(minObj)
    #p.append(minObj)

    print("\n" + str(minObj.totalCost) + "------>" + minObj.key)

    for x in p:
        print(x.key + str(x.totalCost))

    # x = getOldNeighbour(p,obj2)
    # x.totalCost = 5
    #
    # closeList.append(x)
    # p.remove(x)
    #
    # print("\n")

    # for x in p:
    #     print(x.key + str(x.totalCost))
    #
    # for key in closeList:
    #     print(key)
    #     print(str(key.totalCost))



