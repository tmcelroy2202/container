import os
from datetime import datetime, timedelta
import time
import subprocess
import shlex


while (True):
    file_path = "balls.txt"

    mod_time = os.path.getmtime(file_path)
    mod_datetime = datetime.fromtimestamp(mod_time)

    current_datetime = datetime.now()

    time_diff = current_datetime - mod_datetime

    if time_diff > timedelta(seconds=1):
        print("long enough")
        # if time_diff > timedelta(seconds=1200):
            # subprocess.run(["python3", "ledcontrol.py", -1, -1])
    else:
        time.sleep(1)
        continue

    f = open("balls.txt", "r")

    content = f.read()
    if (content == ""):
        time.sleep(1)
        continue

    print(content)
    if ("container" in content):
        index = content.find("container")
        content = content[index:]
        print(content)
    else:
        time.sleep(1)
        continue

    if ("done" in content):
        index = content.find("done")
        content = content[:index-1]
        print(content)

    content = " ".join(content.split()[1:]).lower()
    args_list = shlex.split(content)
    print(content)
    output = subprocess.check_output(["python3", "databased.py"] + args_list)
    output = output.decode().strip()
    print(output)
    if ( ")" in output ):
        number1 = output[1:output.index(",")]
        number2 = output[output.index(",")+2:-1]
        print(number1)
        print(number2)
        subprocess.run(["python3", "ledcontrol.py", number1, number2])

    f.close()
    f = open("balls.txt", "w")
    f.close()
