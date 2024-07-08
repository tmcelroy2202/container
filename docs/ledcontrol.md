I am using WLED on an esp32 to do my lighting. An esp32 is a microcontroller which has decent processing power for super cheap, and allows for me to attach LED lights via pins called GPIO. WLED is software which runs on the ESP32 and hosts a webserver which can be used to control the lights.

WLED has a json api ( https://kno.wled.ge/interfaces/json-api/ ) which can be used to interact with WLED programmatically.


I have created a segment for each slot that I will want to light up ( e.g. a segment for all the lights above the first drawer ). I can then use the WLED JSON API to turn that segment on or off and set it to a specific color. I do this purely by making web requests. 

For example, here is the function I use to set the whole thing dark:

```python
import requests
import json
import sys

def turnalldark(dark = "all"):
    numseg = 31
    skipseg = [16,8]
    payload = {
        "seg": []
    }

    if dark == "all":
        for i in range(numseg):
            payload["seg"].append({
                "id": i,
                "col": [
                    [0, 0, 0]
                ]
            })
    elif dark == "up":
        for i in range(numseg-14):
            payload["seg"].append({
                "id": i+16,
                "col": [
                    [0, 0, 0]
                ]
            })

    if dark != "none":
        url = "http://192.168.1.204/json/state"
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
```

This uses the requests library, and json library, to craft a request to send to the WLED instance, which loops through every single segment of my LED lights, and sets the color of every single one of them to the RGB value 0, 0, 0 which means none of any of the colors, which turns the light off. 

Theoretically, one could totally rewrite this to directly controll LEDs from your device itself, I think, but I have not bothered to look into this, because WLED has worked really really well for me, and I have enjoyed the modularity of my setup. 
