__author__ = 'Santosh'

import getopt,sys,Board


def main(argv):

    inputFile = ''
    algorithm = ''
    heuristic = ''

    try:
        opts, args = getopt.getopt(argv,"i:a:h:",["ifile=","algorithm=","heuristic="])
    except getopt.GetoptError:
        print("test.py -i <inputfile> -o <outputfile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-a':
            algorithm = arg
            print(algorithm)
        if opt == '-h':
            heuristic = arg
            print(heuristic)
        elif opt in ("-i", "--ifile"):
            inputfile = arg
            if inputFile =="":
                print("test.py -i <inputfile> -o <outputfile>")
                sys.exit(2)


    start(inputFile)



def start(inputFile):
    print("Reading input configurations from file :" + inputFile)

    startStates  =[]
    config =[]
    for line in open(inputFile,"r"):
        if "=" in config:
           startStates.append(createBoardConfig(config))
           config.clear()
        else:
            config.append(line)

    for i in startStates:
        print(i)

def createBoardConfig(config):

    p=[]
    for x in config:
        k=[]
        for c in x:
            k.extend(c)
        p.append(k)

    board = Board(p,None)
    return board




if __name__ == "__main__":
    main()
