import ast
import sys
import os
import subprocess


def search(thing, array):
    maybe = (-1, -1)
    for i in range(len(array)):
        for j in range(len(array[i])):
            if (thing == array[i][j]):
                # return i, j
                row = int(i / 8)
                col = i - (row * 8)
                num = row,col
                return num
            if (thing in array[i][j]):
                # maybe = i, j
                row = int(i / 8)
                col = i - (row * 8 )
                maybe = row, col
    return maybe


def findemptiest(array):
    emptiest = 0
    for i in range(1, len(array)):
        if len(array[i]) < len(array[emptiest]):
            emptiest = i
    return emptiest


itemnames = []

datafile = open("db.txt", "r")
itemnames = ast.literal_eval(datafile.readline())

amasschoice = ""
for i, value in enumerate(sys.argv):
    if i > 0:
        amasschoice += value + " "

splitchoice = amasschoice.split(' ')

action = splitchoice[0]

item = ""
for i, value in enumerate(splitchoice):
    if i > 0:
        item += value + " "
item = item.strip()


if action == "search":
    print(search(item, itemnames))
    subprocess.run(["espeak", "-v", "en", "searched successfully"], check=True)

if action == "add":
    idxexisting = search(item, itemnames)
    if idxexisting != (-1,-1):
        # print(idxexisting)
        # print("if full, run same command again, with 'new' instead of 'add'")
        # print("confirming: you have added it, yes?")
        # assume it is confirmed until we hook into voice for confirmation
        # itemnames[idxexisting].append(item)
        realidx = idxexisting[0]*8 + idxexisting[1]
        itemnames[realidx].append(item)
        # print("heres your new list")
        # print(itemnames)
        # row = int(i / 8)
        # col = i - (row * 8 )
        # nums = row, col
        print(idxexisting)
        subprocess.run(["espeak", "-v", "en", "added successfully"], check=True)
    else:
        idx = findemptiest(itemnames)
        # print(idx)
        # print("confirming: you have added it, yes?")
        itemnames[idx].append(item)
        #print("heres your new list")
        # print(itemnames)
        print(search(item,itemnames))
        subprocess.run(["espeak", "-v", "en", "item added"], check=True)
        # row = int(i / 8)
        # col = i - (row * 8 )
        # nums = row,col
        # print(nums)

if action == "new":
    idx = findemptiest(itemnames)
    # print(idx)
    # print("confirming: you have added it, yes?")
    itemnames[idx].append(item)
    # print("heres your new list")
    # print(itemnames)
    # row = int(i / 8)
    # col = i - (row * 8 )
    # nums = row, col
    # print(nums)
    print(search(item,itemnames))
    subprocess.run(["espeak", "-v", "en", "item added"], check=True)


if action == "remove":
    itemidx = search(item, itemnames)
    # print(itemidx)
    if itemidx == (-1, -1):
        # print("item not found")
        subprocess.run(["espeak", "-v", "en", "item not found"], check=True)
    else:
        itemi = itemidx[0]*8 + itemidx[1]
        idxinlist = -1
        for i in range ( len(itemnames[itemi])):
            if ( item in itemnames[itemi][i]):
                idxinlist = i
        itemnames[itemi].pop(idxinlist)
        # print("item removed at index " + str(itemidx[0]) + ", " +  str(itemidx[1]))
        # print("here is your new list")
        # print(itemnames)
        # row = int(i / 8)
        # col = i - (row * 8 )
        # nums = row, col
        # print(nums)
        print(itemidx)
        subprocess.run(["espeak", "-v", "en", "item terminated"], check=True)

if action == "clear":
    print((-1, -1))

with open("db.txt", "w") as f:
    print(itemnames, file=f)


