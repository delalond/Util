import sys
import random
from sets import Set

def getArgs():
    """Get arguments passed by command line"""
    numArgs = len(sys.argv)
    listArgs = sys.argv
    print 'Number of arguments: %d' % numArgs
    print 'Arguments: %s' %listArgs 
    return listArgs

def generateRandomNum(min, max):
    """Generate random number within a defined range"""
    return random.randint(min, max)

def writeOutput(maxCells, numCells):
    """Write output to file"""
    filename = 'user_' + str(maxCells) + 'MaxCells_' + str(numCells) + '_NumCells.target'
    fp = open(filename, 'w')
    #Write header
    fp.write('Target Cell Fabien\n{\n  ')
    GIDSet = Set()
    #Write individual cells
    i=0
    while i<numCells:
    #for i in range(0, numCells):
        CellGID = generateRandomNum(0, maxCells)
        if (CellGID not in GIDSet):
            GIDSet.add(CellGID)
            s = 'a' + str(CellGID) + ' '
            fp.write(s)
            i = i+1
    print 'Size of list: %d\n' %len(GIDSet) 
    fp.write('\n}')
    fp.close()

#if __name__ == "__main__"
list = getArgs()
print list
print len(list)
print list[1]
print list[2]
writeOutput(int(list[1]), int(list[2]))
#    import doctest
#    doctest.testmod()

