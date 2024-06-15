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
    if x < 0 or y < 0:
        return -1
    if len(array) <= y:
        return -1 
    if len(array[y]) <= x:
        return -1
    item = array[y][x]
    return item

def writedb(array):
    with open("db.txt","w") as f:
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

def addpos(thing,x,y):
    itemnames = getdb()
    currarry = getdbcoord(x,y)
    if currarry == -1:
        return -1
    currarry.append(thing)
    if x < 0 or y < 0:
        return -1
    if len(itemnames) <= y:
        return -1
    if len(itemnames[y]) <= x:
        return -1
    writetodbcoord(currarry,x,y)

def findemptiest():
    itemnames = getdb()
    min = 3030303
    mindex = (-1,-1)
    for y in range(len(itemnames)):
        for x in range(len(itemnames[y])):
            if len(itemnames[y][x]) < min:
                # print(len(itemnames[y][x]))
                # print(min)
                # print(itemnames[y][x])
                mindex = (x,y)
                min = len(itemnames[y][x])
    return mindex

def search(thing):
    itemnames = getdb()
    maybe = (-1, -1, -1)
    for x in range(len(itemnames)):
        for y in range(len(itemnames[x])):
            for z in itemnames[x][y]:
                if thing in z:
                    maybe = (y,x,z)
                if thing == z:
                    return (y,x,z)
                    # matches.append(z)
                    # matchespos.append((y,x))
    return maybe
    # return matches,partial,matchespos,partialpos

def remove(thing):
    fullsearch = search(thing)
    matches = fullsearch[0], fullsearch[1]
    # partial = fullsearch[1]
    # matchespos = fullsearch[2]
    # partialpos = fullsearch[3]


    if thing != fullsearch[2]:
        return -1, -1
    theval = fullsearch[2]

    items = getdb()
    # print(thepos)
    # print(theval)
    p1 = int(matches[0])
    p2 = int(matches[1])
    coordarr = getdbcoord(p1,p2)
    coordarr.remove(theval)
    writetodbcoord(coordarr,p1,p2)
    return p1, p2

def removepos(thing,x,y):
    currarry = getdbcoord(x,y)
    itemnames = getdb()
    if currarry == -1:
        return -1
    if x < 0 or y < 0:
        return -1
    if len(itemnames) <= y:
        return -1
    if len(itemnames[y]) <= x:
        return -1
    if thing not in currarry:
        return -1
    currarry.remove(thing)
    writetodbcoord(currarry,x,y)

    


def add(thing):
    # if(type(thing) != str):
    #     return -1
    if not isinstance(thing,str):
        return -1
    fullsearch = search(thing)
    matches = fullsearch[0], fullsearch[1]
    # theval = fullsearch[2]

    if fullsearch[2] != -1:
        theval = fullsearch[2]
        postowrite = matches
    else:
        postowrite = findemptiest()

    pos = getdbcoord(postowrite[0],postowrite[1])
    pos.append(thing)
    writetodbcoord(pos,postowrite[0],postowrite[1])
    return fullsearch[0], fullsearch[1]

    
        
        


    
