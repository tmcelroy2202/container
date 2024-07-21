import ast
import sys
import os
import subprocess

# functions to be implemented
## searchdb(thing)
    # returns position of an item in the array, tuple with x and y 
## findemptiest()
    # returns the emptiest slot in the array, just the one with the least items in it 
## add(thing)
    # adds a given item to the array, at the emptiest spot.
## remove(thing)
    # removes a given item from the array, at the first spot it finds the item.
## removepos(thing,x,y)
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

def getdb():
    itemnames = []
    datafile = open("cc.txt","r")
    itemnames = ast.literal_eval(datafile.read())
    return itemnames

def getdbcoord(x,y):
    array = getdb()
    if x < 0 or y < 0:
        return -1
    if len(array) <= y:
        return -1 
    if len(array[y]) <= x:
        return -1
    item = array[y][x]
    return item

def getlastcommand():
    with open('cmdhistorylibdbcc.txt') as f:
        for line in f:
            pass
        last_line = line
        return last_line

def writedb(array):
    with open("cc.txt.bak","w") as f:
        print(getdb(), file=f)
    with open("cc.txt","w") as f:
        print(array, file=f)

def writetodbcoord(array,x,y):
    itemnames = getdb()
    if x < 0 or y < 0:
        return -1
    if len(itemnames) <= y:
        return -1
    if len(itemnames[y]) <= x:
        return -1
    itemnames[y][x] = array
    writedb(itemnames)

def writecmd(command, thefile):
    with open(thefile,"a") as f:
        print(command, file=f)
    with open('flag.txt', 'w') as f:
        print('libdbcc', file=f)

def addpos(thing,x,y):
    currarry = getdbcoord(x,y)
    currarry.append(thing)
    writetodbcoord(currarry,x,y)

def findemptiest():
    itemnames = getdb()
    min = 3030303
    mindex = (-1,-1)
    for y in range(len(itemnames)):
        for x in range(len(itemnames[y])):
            if len(itemnames[y][x]) < min:
                mindex = (x,y)
                min = len(itemnames[y][x])
    return mindex

def search(thing):
    itemnames = getdb()
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

def remove(thing):
    fullsearch = search(thing)
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

    items = getdb()
    currarr = getdbcoord(thepos[0], thepos[1])
    currarr.remove(theval)
    writetodbcoord(currarr, thepos[0], thepos[1])
    return thepos[0], thepos[1]

def removepos(thing,x,y):
    currarry = getdbcoord(x,y)
    currarry.remove(thing)
    writetodbcoord(currarry,x,y)

    


def add(thing):
    fullsearch = search(thing)
    # print(fullsearch)
    matches = fullsearch[0]
    partial = fullsearch[1]
    matchespos = fullsearch[2]
    partialpos = fullsearch[3]
    # print('matches', matches)
    # print('partial', partial)
    # print('posmatches', matchespos)
    # print('pospartial', partialpos)
    thepos = "j"

    if thing in fullsearch[0]:
        theval = matches[0]
        thepos = matchespos[0]
        # print('thinksmatch')
    elif partial != []:
        theval = partial[0]
        thepos = partialpos[0]
        # print('thinkspartial')
    else:
        thepose = findemptiest()
        # print("thinksempty")

    if thepos != "j":
        # print(thepos)
        pos = getdbcoord(thepos[0], thepos[1])
        # print(pos)
        pos.append(thing)
        # print(pos)
        writetodbcoord(pos,thepos[0],thepos[1])
        return thepos[0], thepos[1]
    else:
        # print(thepose)
        pos = getdbcoord(thepose[0], thepose[1])
        # print(pos)
        pos.append(thing)
        # print(pos)
        writetodbcoord(pos,thepose[0],thepose[1])
        return thepose[0], thepose[1]
        
        


    
