import requests
import json
import sys


def turnalldark(upperonly = False):
    numseg = 31
    skipseg = [16,8]
    payload = {
        "seg": []
    }

    if upperonly == False:
        for i in range(numseg):
            payload["seg"].append({
                "id": i,
                "col": [
                    [0, 0, 0]
                ]
            })
    elif upperonly == True:
        for i in range(numseg-14):
            payload["seg"].append({
                "id": i+16,
                "col": [
                    [0, 0, 0]
                ]
            })

    url = "http://192.168.1.204/json/state"
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))


# turnalldark()


def changeid(id, color):
    if color == "green":
        thecolor = [0,255,0]
    elif color == "red":
        thecolor = [255,0,0]
    elif color == "blue":
        thecolor = [0,0,255]
    elif color == "yellow":
        thecolor = [255,255,0]
    else:
        thecolor = [0,255,0]

    url = "http://192.168.1.204/json/state"
    payload = {
        "seg": [
            {
                "id": id,
                "col": [
                    # [0, 255, 0]
                    thecolor
                ]
            }
        ]
    }

    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    print(response.text.encode('utf8'))



def grid(x, y, color="green"):
    if x == -1 and y == -1:
        turnalldark()
    else:
    # if ( x > )
        turnalldark()
        if x <= 3:
            changeid(x+9,color)
            changeid(y,color)
        else:
            if y == 1:
                y = 4 
            if y == 2:
                x = 5 
                y = 0
            if y == 3:
                x = 5
                y = 4
            changeid(x+9,color)
            changeid(y,color)
            changeid(y+1,color)
            changeid(y+2,color)
            changeid(y+3,color)

def highlight(x,y, color='green', found=True):
    if x == -1 and y == -1:
        turnalldark(found)
    else:
        turnalldark(found)
        id = -1
        # ok so i know this is terrible but i really didnt wanna think very hard right now so i am hardcoding this
        if x == 0 and y == 0:
            id = 2
        if x == 1 and y == 0:
            id = 1
        if x == 2 and y == 0:
            id = 0
        if x == 0 and y == 1:
            id = 4
        if x == 1 and y == 1:
            id = 5
        if x == 2 and y == 1:
            id = 6
        if x == 0 and y == 2:
            id = 10
        if x == 1 and y == 2:
            id = 9
        if x == 2 and y == 2:
            id = 8
        if x == 0 and y == 3:
            id = 12
        if x == 1 and y == 3:
            id = 13
        if x == 2 and y == 3:
            id = 14
        id += 16
        changeid(id, color)
            

# changeid(int(sys.argv[1]))
# highlight(int(sys.argv[1]),int(sys.argv[2]))
