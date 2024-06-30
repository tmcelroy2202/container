ip = input("What is the ip of your wled instance")
ip = ip + "/json/state/"
ip = "http://" + ip

hasgrid = input("Do you have a grid system? (y/n)").lower()

hascc = input("do you have a card catalog system / highlight style system (y/n)").lower()

if hasgrid == "yes" or hasgrid == "y" or hasgrid == "yeah" or hasgrid =="definitely":
    hasgrid = True
else:
    hasgrid = False

if hascc == "yes" or hascc == "y" or hascc == "yeah" or hascc =="definitely":
    hascc = True
else:
    hascc = False

print('in summary:')
print(' to interact with the json api of your wled instance, we will use the ip: ' + ip )
if hasgrid == True:
    print('you do have a grid system')
else: 
    print('you do not have a grid system')
if hascc == True:
    print('you do have a highlight style / card catalog style system')
else:
    print('you do not have a highlight style / card catalog style system')
wegood = input("is this right? ( y/n )")
wegood = wegood.lower()
if wegood == 'y' or wegood == 'yes' or wegood == 'yeah' or wegood == 'sure' or wegood == 'definitely':
    file = open('env.txt', 'w')
    file.write(ip + "\n")
    file.write(hasgrid + "\n")
    file.write(hascc + "\n")
else:
    print("ok then run this script again thanks.")
    exit()



