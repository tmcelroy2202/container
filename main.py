import libdb
import libdbcc
import ledcontrol
import bridgeutils
import time
import subprocess

while(True):
    file_path = "inputs.txt"
    if bridgeutils.morethan3sec(file_path):
        ourcommand = bridgeutils.getcommand(file_path)
        if ourcommand == -1:
            time.sleep(1)
            continue
    else:
        time.sleep(1)
        continue


    action = ourcommand.split(" ")[0]
    ledcontrol.turnalldark()

    undoflag = False

    if action == "undo" or action == "reverse" or action == "fuck":
        undoflag = True

        file = open('flag.txt', 'r')
        thelib = file.read().strip()
        if thelib == 'libdbcc':
            command = libdbcc.getlastcommand()
            # parenidx = command.index('(')
            # endidx = command.index(',ee ') + 4
            # action = command[:command.index('(')]
            # thing = command[parenidx:]
            # thing = command[:endidx]
            # thing = thing.strip()
            # pos = command[endidx:-2]
            action = command[:command.index('(')]
            thing = command[command.index('(')+1:command.index(',ee ')]
            thing = thing.strip()
            pos = command[command.index(',ee ')+4:-2]
            pos = tuple(map(int,pos.split(', ')))
            if action == "addpos":
                libdbcc.removepos(thing,pos[0],pos[1])
                ledcontrol.highlight(pos[0],pos[1], 'red')
                subprocess.run(["espeak", "-v", "en", "item terminated from card catalog"], check=True)
            elif action == "removepos":
                libdbcc.addpos(thing,pos[0],pos[1])
                ledcontrol.highlight(pos[0],pos[1], 'green')
                subprocess.run(["espeak", "-v", "en", "item added to card catalog"], check=True)
            elif action == "search":
                ledcontrol.turnalldark()
        if thelib == 'libdb':
            command = libdb.getlastcommand()
            action = command[:command.index('(')]
            thing = command[command.index('(')+1:command.index(',ee ')]
            thing = thing.strip()
            pos = command[command.index(',ee ')+4:-2]
            pos = tuple(map(int,pos.split(', ')))
            x = pos[0]
            y = pos[1]
            if action == "addpos":
                pos = libdb.removepos(thing,pos[0],pos[1])
                ledcontrol.grid(x, y, 'red')
                subprocess.run(["espeak", "-v", "en", "item terminated from containers"], check=True)
            elif action == "removepos":
                pos = libdb.addpos(thing,pos[0],pos[1])
                ledcontrol.grid(pos[0], pos[1], 'green')
                subprocess.run(["espeak", "-v", "en", "item added to containers"], check=True)
            elif action == "search":
                ledcontrol.turnalldark()
            # action = command

    if action == "clear":
        ledcontrol.turnalldark()
    
    if undoflag == False:
        thing = ourcommand[ourcommand.index(action)+len(action):].strip()

    if thing == "esp 32":
        thing = "esp32"

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
        onedone = False

        for coord in matchespos:
            if found == False:
                dark = "all"
            if onedone == False and found == True:
                dark = "up"
            else: 
                dark = "none"
            ledcontrol.highlight(coord[0], coord[1], "green", found)
            print("true match:", coord)
            foundup = True
            onedone = True
        for coord in partialpos:
            if found == False:
                dark = "all"
            if onedone == False:
                dark = "up"
            else: 
                dark = "none"
            ledcontrol.highlight(coord[0], coord[1], "yellow", found)
            print("partial match:", coord)
            foundup = True
            onedone = True
        if found == False and foundup == False:
            ledcontrol.turnalldark()
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

        if currdb[0] == -1 and currdb[1] == -1 and curcc[0] == [] and curcc[1] == []:
            if len(conarr) < len(concc):
                pos = libdb.add(thing)
                cmdstring = 'addpos(' + thing + ',ee ' + str(pos[0]) + ', ' + str(pos[1]) + ')'
                libdb.writecmd(cmdstring, 'cmdhistorylibdb.txt')
                ledcontrol.grid(pos[0], pos[1])
                subprocess.run(["espeak", "-v", "en", "item added to containers"], check=True)
            else:
                pos = libdbcc.add(thing)
                cmdstring = 'addpos(' + thing + ',ee ' + str(pos[0]) + ', ' + str(pos[1]) + ')'
                libdbcc.writecmd(cmdstring, 'cmdhistorylibdbcc.txt')
                ledcontrol.highlight(pos[0], pos[1])
                subprocess.run(["espeak", "-v", "en", "item added to card catalog"], check=True)
        elif curcc[0] != []:
            pos = libdbcc.add(thing)
            cmdstring = 'addpos(' + thing + ',ee ' + str(pos[0]) + ', ' + str(pos[1]) + ')'
            libdbcc.writecmd(cmdstring, 'cmdhistorylibdbcc.txt')
            ledcontrol.highlight(pos[0], pos[1])
            subprocess.run(["espeak", "-v", "en", "item added to card catalog"], check=True)
        elif currdb[0] != -1:
            pos = libdb.add(thing)
            cmdstring = 'addpos(' + thing + ',ee ' + str(pos[0]) + ', ' + str(pos[1]) + ')'
            libdb.writecmd(cmdstring, 'cmdhistorylibdb.txt')
            ledcontrol.grid(pos[0], pos[1])
            subprocess.run(["espeak", "-v", "en", "item added to containers"], check=True)
        elif curcc[1] != []:
            pos = libdbcc.add(thing)
            cmdstring = 'addpos(' + thing + ',ee ' + str(pos[0]) + ', ' + str(pos[1]) + ')'
            libdbcc.writecmd(cmdstring, 'cmdhistorylibdbcc.txt')
            ledcontrol.highlight(pos[0], pos[1])
            subprocess.run(["espeak", "-v", "en", "item added to card catalog"], check=True)

            

    if action == "remove":
        conres = libdb.search(thing)
        concc = libdbcc.search(thing)
        if concc[0] != []:
            toremove = concc
            pos = libdbcc.remove(thing)
            ledcontrol.highlight(pos[0],pos[1], 'red')
            subprocess.run(["espeak", "-v", "en", "item terminated from card catalog"], check=True)
        elif conres[0] != -1:
            toremove = conres 
            pos = libdb.remove(thing)
            ledcontrol.grid(pos[0],pos[1], 'red')
            subprocess.run(["espeak", "-v", "en", "item terminated from containers"], check=True)
        else:
            subprocess.run(["espeak", "-v", "en", "item not found"], check=True)


        


        



