# import goassign from assign
from assign import goassign
from dimensions import getdimensions

x,y = getdimensions()
grid = goassign(x,y)
print(grid)

def getgridcc():
    x,y = getdimensions()
    grid = goassign(x,y)

def getgriddb():
    x,y = getdimensions()


def getgridandcc():
    inbetween = input("what is the id of the segment between the grid and the card catalog ? ")
    first = input("what comes first? grid or cardcatalog ( answer: grid or cc)")
    if first == "cc":
        ccarr = getgridcc()
        gridsize = getgriddb()
    elif first == "grid":
        gridsize = getgriddb()
        ccarr = getgridcc()

    
