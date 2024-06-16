import os
from datetime import datetime, timedelta
import time
import subprocess
import shlex

def morethan3sec(file_path):
    mod_time = os.path.getmtime(file_path)
    mod_datetime = datetime.fromtimestamp(mod_time)

    current_datetime = datetime.now()

    time_diff = current_datetime - mod_datetime

    if time_diff > timedelta(seconds=1):
        return True
    else:
        return False

def getcommand(file_path):
    f = open(file_path)
    content = f.read()
    if content == "":
        return -1
    content = content.lower()

    if "container" in content:
        index = content.find("container")
        content = content[index:]
    else:
        return -1

    if "done" in content:
        index = content.find("done")
        content = content[:index-1]

    # content = container seArch fAkE airpods
    content = " ".join(content.split()[1:]).lower()
    # content = search fake airpods
    return content

def clearbridge(file_path):
    f = open(file_path,'w')
    f.close()

    
