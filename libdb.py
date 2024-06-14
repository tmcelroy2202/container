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
    # returns the contents of db.txt as an array
## getdbcoord(x,y)
    # returns whatever is at this coordinate in the database
## writedb(array)
    # write the contents of the given array to db.txt
## writetodbcoord(array,x,y)
    # overwrites a position in the database with another array.

def getdb():
    itemnames = []
    datafile = open("db.txt","r")
    itemnames = ast.literal_eval(datafile.read())
    return itemnames

def getdbcoord(x,y):
    array = getdb()
    item = array[y][x]
    return item

def writedb(array):
    with open("db.txt","w") as f:
        print(itemnames, file=f)

def writetodbcoord(array,x,y):
    itemnames = getdb()
    itemnames[y][x] = array
    writedb(itemnames)

def addpos(thing,x,y):
    currarry = getdbcord(x,y)
    currarry.add(thing)
    writetodbcoord(currarry,x,y)

def findemptiest():
    itemnames = getdb()
    min = 3030303
    mindex = (-1,-1)
    for y in range(len(itemnames)):
        for x in range(len(itemnames[y])):
            if len(itemnames[y][x]) < min:
                mindex = (y,x)
                min = len(itemnames[y])
    return mindex

def search(thing):
    itemnames = getdb()
    maybe = (-1, -1, None)
    for x in range(len(itemnames)):
        for y in range(len(itemnames[x])):
            for z in itemnames[x][y]:
                if thing in z:
                    maybe = (x,y,z)
                if thing == z:
                    return (x,y,z)
                    # matches.append(z)
                    # matchespos.append((y,x))
    return maybe
    # return matches,partial,matchespos,partialpos

def remove(thing):
    fullsearch = search(thing)
    print(fullsearch)
    matches = fullsearch[0], fullsearch[1]
    # partial = fullsearch[1]
    # matchespos = fullsearch[2]
    # partialpos = fullsearch[3]


    if thing == fullsearch[2]:
        theval = fullsearch[2]
    else:
        return -1, -1

    items = getdb()
    # print(thepos)
    # print(theval)
    p1 = int(matches[0])
    p2 = int(matches[1])
    print(items[p1][p2])
    items[p1][p2].remove(theval)
    writedb(items)
    return p1, p2

def removepos(thing,x,y):
    currarry = getdbcord(x,y)
    currarry.remove(thing)
    writetodbcoord(currarry,x,y)

    


def add(thing):
    fullsearch = search(thing)
    matches = fullsearch[0], fullsearch[1]
    # theval = fullsearch[2]

    if thing in fullsearch[2]:
        theval = fullsearch[2]
        postowrite = matches
    elif partial != []:
        theval = partial[0]
        thepos = partialpos[0]
        postowrite = matches
    else:
        postowrite = findemptiest()

    pos = getdbcoord(fullsearch[0],fullsearch[1])
    pos.append(thing)
    writetodbcoord(pos,fullsearch[0],fullsearch[1])
    return fullsearch[0], fullsearch[1]

    
        
        


    
