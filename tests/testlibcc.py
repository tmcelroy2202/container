import libdbcc
import ast
import time
start_time = time.time()

file = open("cc.txt.valid")
contents = file.read()
file.close()

def reset():
    file = open("cc.txt.valid")
    contents = file.read()
    file.close()

    file = open("cc.txt", 'w')
    file.write(contents)
    file.close()

reset()

if libdbcc.getdb() != ast.literal_eval(contents):
    print("test failed: getdb() is not equal to the valid database example")
    print(libdbcc.getdb())
    print(contents)

if libdbcc.getdbcoord(1,0) != ['usb a to see cable usb a to c cable']:
    print("test failed: getdbcoord(0,1) did not return the correct value")
    print(libdbcc.getdbcoord(1,0))

if libdbcc.getdbcoord(2,3) != ['mini hdmi to hdmi adapter']:
    print("test failed: getdbcoord(3,2) did not return the correct value")
    print(libdbcc.getdbcoord(2,3))

if libdbcc.getdbcoord(999,999) != -1:
    print("test failed: did not return -1 for an over bounds query of getdbcoord")

if libdbcc.getdbcoord(-1,-1) != -1:
    print("test failed: did not return -1 for an under bounds query of getdbcoord")

testarray1 = [
    [
        ['hello'],
        ['there'],
        ['howru']
    ],
    [
        ['hey'],
        ['bro'],
        ['im good']
    ],
    [
        ['great to hear'],
        ['hope you make'],
        [' a speedy rec'],
        ['overy man!!!!']
    ]
]

testarray2 = [
    [
        [],
        [],
        []
    ],
    [
        [],
        [],
        []
    ],
    [
        [],
        [],
        [],
        []
    ]
]


testarray3 = [['hey'], ['there'], ['mmmm']]

testarray4 = [
    [
        [],
        [['hey'], ['there'], ['mmmm']],
        []
    ],
    [
        [],
        [],
        []
    ],
    [
        [],
        [],
        [],
        []
    ]
]

testarray5 = [
    [
        [],
        [],
        []
    ],
    [
        [],
        [],
        []
    ],
    [
        [],
        [['hey'], ['there'], ['mmmm']],
        [],
        []
    ]
]

# writedb
reset()
libdbcc.writedb(testarray1)
if libdbcc.getdb() != testarray1:
    print("test failed: writetodb not writing same contents as given")
    print(libdbcc.getdb())
    print(testarray1)

reset()
libdbcc.writedb(testarray2)
if libdbcc.getdb() != testarray2:
    print('test failed: writetodb not writing same contents as given')
    print(libdbcc.getdb())
    print(testarray2)

# writetodbcoord

libdbcc.writetodbcoord(testarray3,1,0)
if libdbcc.getdb() != testarray4:
    print("test failed: writetodbcoord not writing same contents as given")
    print(libdbcc.getdb())
    print(testarray4)

reset()
libdbcc.writedb(testarray2)
if libdbcc.getdb() != testarray2:
    print('test failed: writetodb not writing same contents as given')
    print(libdbcc.getdb())
    print(testarray2)

libdbcc.writetodbcoord(testarray3,1,2)
if libdbcc.getdb() != testarray5:
    print('test failed: writetodbcoord not writing same contents as given')
    print(libdbcc.getdb())
    print(testarray5)

reset()

if libdbcc.writetodbcoord(testarray3,50,50) != -1:
    print('test failed: out of bounds writetodbcoord not returning right')
    print(libdbcc.writetodbcoord(testarray3,50, 50))

reset()
if libdbcc.writetodbcoord(testarray3,-1,-1) != -1:
    print('test failed: out of bounds writetodbcoord not returning right')
    print(libdbcc.writetodbcoord(testarray3,-1,-1))

# findemptiest

reset()
if libdbcc.findemptiest() != (2,1):
    print("test failed: findemptiest() does not return 2,1")
    print(libdbcc.findemptiest())
    print(libdbcc.getdbcoord(libdbcc.findemptiest()[0], libdbcc.findemptiest()[1]))

# addpos

reset()
libdbcc.addpos('test1',2,1)
if libdbcc.getdbcoord(2,1) != ['test1']:
    print('test failed: addpos(2,1) does not add as specified ')

libdbcc.addpos('test2',2,0)
if libdbcc.getdbcoord(2,0) != ['usb a to micro b cable', 'usb a to micro b cable', 'test2']:
    print('test failed: addpos("test2", 2, 0) does not add as specified')
    print(libdbcc.getdbcoord(2,0))

# search

searchres = libdbcc.search("test")
matches = searchres[0]
partial = searchres[1]
matchespos = searchres[2]
partialpos = searchres[3]
for i in range(len(matchespos)):
    if matches[i] not in libdbcc.getdbcoord(matchespos[i][0], matchespos[i][1]):
        print('test failed: match coordinate does not match the value specified')
    if "test" != matches[i]:
        print('test failed: returned a match that doesnt match the search')
    
for i in range(len(partialpos)):
    if partial[i] not in libdbcc.getdbcoord(partialpos[i][0], partialpos[i][1]):
        print('test failed: partial match coordinate does not match the value specified')
    if "test" not in partial[i]:
        print("test failed: returned a partial match that doesnt contain test")
if matches != [] or matchespos != []:
    print("returned exact matches when there are none")
    print(matches)
    print(matchespos)

if partial != ['test2', 'test1'] or partialpos != [(2,0), (2,1)]:
    print("returned incorrect partial matches.")
    print(partial)
    print(partialpos)


searchres = libdbcc.search("test2")
matches = searchres[0]
partial = searchres[1]
matchespos = searchres[2]
partialpos = searchres[3]
for i in range(len(matchespos)):
    if matches[i] not in libdbcc.getdbcoord(matchespos[i][0], matchespos[i][1]):
        print('test failed: match coordinate does not match the value specified')
    if "test2" != matches[i]:
        print('test failed: returned a match that doesnt match the search')
    
for i in range(len(partialpos)):
    if partial[i] not in libdbcc.getdbcoord(partialpos[i][0], partialpos[i][1]):
        print('test failed: partial match coordinate does not match the value specified')
    if "test" not in partial[i]:
        print("test failed: returned a partial match that doesnt contain test")
if matches != ['test2'] or matchespos != [(2,0)]:
    print("returned incorrect matches")
    print(matches)
    print(matchespos)

if partial != [] or partialpos != []:
    print("returned partial matches when there are none")
    print(partial)
    print(partialpos)

libdbcc.remove("test2")
searchres = libdbcc.search("test2")
matches = searchres[0]
partial = searchres[1]
matchespos = searchres[2]
partialpos = searchres[3]
if matches != [] or matchespos != []:
    print('remove has failed to remove the item')
    print(matches[0])
    print(matchespos[0])
    print(libdbcc.getdbcoord(matchespos[0][0], matchespos[0][1]))

if partial != [] or partialpos != []:
    print('partial results when there are none')

reset()
libdbcc.add("test1")
searchres = libdbcc.search("test1")
matches = searchres[0]
partial = searchres[1]
matchespos = searchres[2]
partialpos = searchres[3]
if matches != ['test1'] or matchespos != [(2,1)]:
    print("returned incorrect matches")
    print(matches)
    print(matchespos)

if partial != [] or partialpos != []:
    print("returned partial matches when there are none")
    print(partial)
    print(partialpos)

if libdbcc.getdbcoord(2,1) != ['test1']:
    print('wrong position')
    print(libdbcc.getdbcoord(2,1))
    print(matches)

reset()
libdbcc.add('flash drive')
searchres = libdbcc.search("flash drive")
matches = searchres[0]
partial = searchres[1]
matchespos = searchres[2]
partialpos = searchres[3]
if matches != ['flash drive', 'flash drive', 'flash drive', 'flash drive'] or matchespos != [(0,1),(0,1),(0,1),(0,1)]:
    print("returned incorrect matches")
    print(matches)
    print(matchespos)

if partial != [] or partialpos != []:
    print("returned partial matches when there are none")
    print(partial)
    print(partialpos)

if libdbcc.getdbcoord(0,1) != ['flash drive', 'flash drive', 'flash drive', 'flash drive']:
    print('wrong position')
    print(libdbcc.getdbcoord(2,1))
    print(matches)

reset()

end_time = time.time()
print("num of seconds:", (end_time - start_time))
