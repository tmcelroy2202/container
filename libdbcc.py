import ast
import sys
import os
import subprocess

# functions to be implemented
## searchdb(thing)
    # returns position of an item in the array, tuple with x and y 
## findemptiest()
    # returns the emptiest slot in the array, just the one with the least items in it 
# add(thing)
    # adds a given item to the array, at the emptiest spot.
## remove(thing)
    # removes a given item from the array, at the first spot it finds the item.
# removepos(thing,x,y)
    # removes a given item from the array, but only the item at the given position. so if i said removepos(brick,4,3) it would remove the brick which is located at x=4 y=3. if there was no brick at x=4 y=3, it would tell the user that there was no such thing at that location. If there were multiple bricks, it would remove the first one it found.
## addpos(thing,x,y)
    # adds a given item to a specific position in the array, e.g. if i say addpos(brick,4,3) it adds a brick to x=4 y=3, regardless of how empty that container is. 
## getdb() 
    # returns the contents of cc.txt as an array
## getdbcoord(x,y)
    # returns whatever is at this coordinate in the database
## writedb(array)
    # write the contents of the given array to cc.txt
## writetodbcoord(array,x,y)
    # overwrites a position in the database with another array.

def getdbcc():
    itemnames = []
    datafile = open("cc.txt","r")
    itemnames = ast.literal_eval(datafile.read())
    return itemnames

def getdbcoordcc(x,y):
    array = getdbcc()
    item = array[y][x]
    return item

def writedbcc(array):
    with open("cc.txt","w") as f:
        print(array, file=f)

def writetodbcoordcc(array,x,y):
    itemnames = getdbcc()
    itemnames[y][x] = array
    writedbcc(itemnames)

def addposcc(thing,x,y):
    currarry = getdbcordcc(x,y)
    currarry.add(thing)
    writetodbcoordcc(currarry,x,y)

def findemptiestcc():
    itemnames = getdbcc()
    min = 3030303
    mindex = (-1,-1)
    for x in range(len(itemnames)):
        for y in range(len(itemnames[x])):
            if len(itemnames[x][y]) < min:
                mindex = (x,y)
                min = len(itemnames[x][y])
    return mindex

def searchcc(thing):
    itemnames = getdbcc()
    maybe = ""
    matches = []
    partial = []
    matchespos = []
    partialpos = []
    for x in range(len(itemnames)):
        for y in range(len(itemnames[x])):
            for z in itemnames[x][y]:
                if thing in z:
                    partial.append(z)
                    partialpos.append((y,x))
                if thing == z:
                    matches.append(z)
                    matchespos.append((y,x))
    for i,val in enumerate(partialpos):
        for j in matchespos:
            if val == j:
                partialpos.pop(i)
                partial.pop(i)
    return matches,partial,matchespos,partialpos

def removecc(thing):
    print(thing)
    fullsearch = searchcc(thing)
    matches = fullsearch[0]
    partial = fullsearch[1]
    matchespos = fullsearch[2]
    partialpos = fullsearch[3]

    if thing in fullsearch[0]:
        theval = matches[0]
        thepos = matchespos[0]
    elif partial != []:
        theval = partial[0]
        thepos = partialpos[0]
    else:
        return -1, -1

    items = getdbcc()
    print(thepos)
    print(theval)
    p1 = int(thepos[0])
    p2 = int(thepos[1])
    items[p2][p1].remove(theval)
    writedbcc(items)
    return p1, p2

def removeposcc(thing,x,y):
    currarry = getdbcordcc(x,y)
    currarry.remove(thing)
    writetodbcoordcc(currarry,x,y)

    


def addcc(thing):
    fullsearch = searchcc(thing)
    print(fullsearch)
    matches = fullsearch[0]
    partial = fullsearch[1]
    matchespos = fullsearch[2]
    partialpos = fullsearch[3]
    print('matches', matches)
    print('partial', partial)
    print('posmatches', matchespos)
    print('pospartial', partialpos)
    thepos = "j"

    if thing in fullsearch[0]:
        theval = matches[0]
        thepos = matchespos[0]
    elif partial != []:
        theval = partial[0]
        thepos = partialpos[0]
    else:
        thepose = findemptiestcc()

    if thepos != "j":
        print(thepos)
        pos = getdbcoordcc(thepos[0], thepos[1])
        print(pos)
        pos.append(thing)
        print(pos)
        writetodbcoordcc(pos,thepos[0],thepos[1])
        return thepos[0], thepos[1]
    else:
        print(thepose)
        pos = getdbcoordcc(thepose[1], thepose[0])
        print(pos)
        pos.append(thing)
        print(pos)
        writetodbcoordcc(pos,thepose[1],thepose[0])
        return thepose[1], thepose[0]
        
        


    
