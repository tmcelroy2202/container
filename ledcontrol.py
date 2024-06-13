import requests
import json
import sys

numseg = 16
skipseg = [16,8]

def turnalldark():
    payload = {
        "seg": []
    }

    for i in range(numseg):
        payload["seg"].append({
            "id": i,
            "col": [
                [0, 0, 0]
            ]
        })

    url = "http://192.168.1.204/json/state"
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))


turnalldark()


def changeid(id):
    url = "http://192.168.1.204/json/state"
    payload = {
        "seg": [
            {
                "id": id,
                "col": [
                    [0, 255, 0]
                ]
            }
        ]
    }

    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    print(response.text.encode('utf8'))



def highlight(x, y):
    if x == -1 and y == -1:
        turnalldark()
    else:
    # if ( x > )
        if x <= 3:
            changeid(x+9)
            changeid(y)
        else:
            if y == 1:
                y = 4 
            if y == 2:
                x = 5 
                y = 0
            if y == 3:
                x = 5
                y = 4
            changeid(x+9)
            changeid(y)
            changeid(y+1)
            changeid(y+2)
            changeid(y+3)
    

highlight(int(sys.argv[1]),int(sys.argv[2]))
