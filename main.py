import libdb
import libdbcc
import ledcontrol
import bridgeutils
import time
import subprocess

while(True):
    file_path = "balls.txt"
    if bridgeutils.morethan3sec(file_path):
        ourcommand = bridgeutils.getcommand(file_path)
        if ourcommand == -1:
            time.sleep(1)
            continue
    else:
        time.sleep(1)
        continue

    action = ourcommand.split(" ")[0]

    if action == "clear":
        ledcontrol.turnalldark()
    
    thing = ourcommand[ourcommand.index(action)+len(action):].strip()

    if thing == "":
        time.sleep(1)
        continue

    bridgeutils.clearbridge(file_path)

    if action == "search":
        found = False
        fullsearch = libdb.search(thing)

        if thing == fullsearch[2]:
            ledcontrol.grid(fullsearch[0], fullsearch[1], "green")
            found = True
        elif fullsearch[2] == -1:
            found = False
        elif thing in fullsearch[2]:
            ledcontrol.grid(fullsearch[0], fullsearch[1], "yellow")
            found = True

        fullsearch = libdbcc.search(thing)
    
        matches = fullsearch[0]
        partial = fullsearch[1]
        matchespos = fullsearch[2]
        partialpos = fullsearch[3]
        foundup = False

        for coord in matchespos:
            ledcontrol.highlight(coord[0], coord[1], "green", found)
            print("true match:", coord)
            foundup = True
        for coord in partialpos:
            ledcontrol.highlight(coord[0], coord[1], "yellow", found)
            print("partial match:", coord)
            foundup = True
        if found == False and foundup == False:
            ledcontrol.turnalldark(False)
            subprocess.run(["espeak", "-v", "en", "item not found"], check=True)
        else:
            subprocess.run(["espeak", "-v", "en", "searched successfully"], check=True)

    if action == "add" or action == "plus" or action == "insert" or action == "ad":
        emptycon = libdb.findemptiest()
        conarr = libdb.getdbcoord(emptycon[0], emptycon[1])
        emptycc = libdbcc.findemptiest()
        concc = libdbcc.getdbcoord(emptycc[0], emptycc[1])
        currdb = libdb.search(thing)
        curcc = libdbcc.search(thing)
        print('heyu')

        if currdb[0] == -1 and currdb[1] == -1 and curcc[0] == [] and curcc[1] == []:
            if len(conarr) < len(concc):
                pos = libdb.add(thing)
                ledcontrol.grid(pos[0], pos[1])
                subprocess.run(["espeak", "-v", "en", "item added to containers"], check=True)
            else:
                pos = libdbcc.add(thing)
                ledcontrol.highlight(pos[0], pos[1])
                subprocess.run(["espeak", "-v", "en", "item added to card catalog"], check=True)
        elif curcc[0] != []:
            pos = libdbcc.add(thing)
            ledcontrol.highlight(pos[0], pos[1])
            subprocess.run(["espeak", "-v", "en", "item added to card catalog"], check=True)
        elif currdb[0] != -1:
            pos = libdb.add(thing)
            ledcontrol.grid(pos[0], pos[1])
            subprocess.run(["espeak", "-v", "en", "item added to containers"], check=True)
        elif curcc[1] != []:
            pos = libdbcc.add(thing)
            ledcontrol.highlight(pos[0], pos[1])
            subprocess.run(["espeak", "-v", "en", "item added to card catalog"], check=True)

            

    if action == "remove":
        conres = libdb.search(thing)
        concc = libdbcc.search(thing)
        if conres[0] != -1:
            toremove = conres 
            pos = libdb.remove(thing)
            ledcontrol.grid(pos[0],pos[1], 'red')
            subprocess.run(["espeak", "-v", "en", "item terminated from containers"], check=True)
        elif concc[0] != []:
            toremove = concc
            pos = libdbcc.remove(thing)
            ledcontrol.highlight(pos[0],pos[1], 'red')
            subprocess.run(["espeak", "-v", "en", "item terminated from card catalog"], check=True)
        else:
            subprocess.run(["espeak", "-v", "en", "item not found"], check=True)


        


        



