import time
import ledcontrol

vstart = time.time()

gstart = time.time()
ledcontrol.grid(1,2)
gend = time.time()
print('grid', gend-gstart)

hstart = time.time()
ledcontrol.highlight(1,2)
hend = time.time()
print('highlight', hend-hstart)

ostart = time.time()
ledcontrol.turnalldark()
oend = time.time()
print("turnalldark", oend-ostart)
