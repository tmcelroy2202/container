import ledcontrol
import time

ledcontrol.turnallwhite(False)
time.sleep(1)

# turnalldark

# turn both containers dark 
ledcontrol.turnalldark(False)
time.sleep(1)
ledcontrol.turnallwhite(False)
time.sleep(1)
# turn only top dark
ledcontrol.turnalldark(True)

time.sleep(.5)
ledcontrol.turnalldark(False)
# test every single changeid
time.sleep(1)
ledcontrol.changeid(0, "green")
time.sleep(.1)
ledcontrol.changeid(1, "green")
time.sleep(.1)
ledcontrol.changeid(2, "green")
time.sleep(.1)
ledcontrol.changeid(3, "green")
time.sleep(.1)
ledcontrol.changeid(4, "green")
time.sleep(.1)
ledcontrol.changeid(5, "green")
time.sleep(.1)
ledcontrol.changeid(6, "green")
time.sleep(.1)
ledcontrol.changeid(7, "green")
time.sleep(.1)
ledcontrol.changeid(8, "green")
time.sleep(.1)
ledcontrol.changeid(9, "green")
time.sleep(.1)
ledcontrol.changeid(10, "green")
time.sleep(.1)
ledcontrol.changeid(11, "green")
time.sleep(.1)
ledcontrol.changeid(12, "green")
time.sleep(.1)
ledcontrol.changeid(13, "green")
time.sleep(.1)
ledcontrol.changeid(14, "green")
time.sleep(.1)
ledcontrol.changeid(15, "green")
time.sleep(.1)
ledcontrol.changeid(16, "green")
time.sleep(.1)
ledcontrol.changeid(17, "green")
time.sleep(.1)
ledcontrol.changeid(18, "green")
time.sleep(.1)
ledcontrol.changeid(19, "green")
time.sleep(.1)
ledcontrol.changeid(20, "green")
time.sleep(.1)
ledcontrol.changeid(21, "green")
time.sleep(.1)
ledcontrol.changeid(22, "green")
time.sleep(.1)
ledcontrol.changeid(23, "green")
time.sleep(.1)
ledcontrol.changeid(24, "green")
time.sleep(.1)
ledcontrol.changeid(25, "green")
time.sleep(.1)
ledcontrol.changeid(26, "green")
time.sleep(.1)
ledcontrol.changeid(27, "green")
time.sleep(.1)
ledcontrol.changeid(28, "green")
time.sleep(.1)
ledcontrol.changeid(29, "green")
time.sleep(.1)
ledcontrol.changeid(30, "green")
time.sleep(1)

# test grid
ledcontrol.turnalldark(False)
ledcontrol.grid(1,2)
time.sleep(1)
ledcontrol.grid(1,4)
time.sleep(1)
ledcontrol.grid(7,3)
time.sleep(1)
ledcontrol.grid(1,5)
time.sleep(1)
ledcontrol.grid(0,5)

ledcontrol.turnalldark(False)
# test card catalog
ledcontrol.highlight(0,1)
time.sleep(1)
ledcontrol.highlight(2,1)
time.sleep(1)
ledcontrol.highlight(2,3)
time.sleep(1)

ledcontrol.turnalldark(False)
