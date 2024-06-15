import ast
import libdb

file = open("db.txt.valid")
contents = file.read()
file.close()

def reset():
    file = open("db.txt.valid")
    contents = file.read()
    file.close()

    file = open("db.txt", "w")
    file.write(contents)
    file.close()

reset()

if libdb.getdb() != ast.literal_eval(contents):
    print('test failed: getdb() is not equal to the valid database example')
    print(libdb.getdb())
    print(contents)

# search

if libdb.search("esp32") != (0,1, 'esp32'):
    print('test failed: esp32 search != 0,1')
    print(libdb.search("esp32"))

# these SHOULD be 1 because they are column 2 and we are doing zero based indexing. its just a really wide column.
if libdb.search("ziploc bags") != (1,5,'ziploc bags'):
    print('test failed: ziploc bags search != 1,5')
    print(libdb.search("ziploc bags"))
if libdb.search("budi circle") != (1,4, 'budi circle'):
    print('test failed: budi circle search != 5,4')
    print(libdb.search("budi circle"))

if libdb.search("brick") != (0,5, 'brick'):
    print('test failed: brick search != 0,5')
    print(libdb.search("brick"))

if libdb.search('notinmyarray') != (-1,-1, -1):
    print('test failed for item not in array')
    print(libdb.search('notinmyarray'))

# getdbcoord

if libdb.getdbcoord(7,1) != ['wired earbuds']:
    print('test failed: getdbcoord(1,7) != ["wired earbuds"]')
    print(libdb.getdbcoord(7,1))


if libdb.getdbcoord(1,5) != ['ziploc bags']:
    print('test failed: getdbcoord(5,1) != ["ziploc bags"]')
    print(libdb.getdbcoord(1,5))

if libdb.getdbcoord(500,500) != -1:
    print('test failed: invalid indexes return wrong thing')
    print(libdb.getdbcoord(500,500))

if libdb.getdbcoord(-1,-1) != -1:
    print('test failed: invalid indexes return wrong thing')
    print(libdb.getdbcoord(-1,-1))

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

libdb.writedb(testarray1)
if libdb.getdb() != testarray1:
    print('test failed: writetodb not writing same contents as given')
    print(libdb.getdb())
    print(testarray1)

reset()
libdb.writedb(testarray2)
if libdb.getdb() != testarray2:
    print('test failed: writetodb not writing same contents as given')
    print(libdb.getdb())
    print(testarray2)


# writetodbcoord 

reset()
libdb.writedb(testarray2)
if libdb.getdb() != testarray2:
    print('test failed: writetodb not writing same contents as given')
    print(libdb.getdb())
    print(testarray2)

libdb.writetodbcoord(testarray3,1,0)
if libdb.getdb() != testarray4:
    print('test failed: writetodbcoord not writing same contents as given')
    print(libdb.getdb())
    print(testarray4)

reset()
libdb.writedb(testarray2)
if libdb.getdb() != testarray2:
    print('test failed: writetodb not writing same contents as given')
    print(libdb.getdb())
    print(testarray2)

libdb.writetodbcoord(testarray3,1,2)
if libdb.getdb() != testarray5:
    print('test failed: writetodbcoord not writing same contents as given')
    print(libdb.getdb())
    print(testarray5)

reset()
if libdb.writetodbcoord(testarray3,50,50) != -1:
    print('test failed: out of bounds writetodbcoord not returning right')
    print(libdb.writetodbcoord(testarray3,50,50))

reset()
if libdb.writetodbcoord(testarray3,-1,-1) != -1:
    print('test failed: out of bounds writetodbcoord not returning right')
    print(libdb.writetodbcoord(testarray3,-1,-1))

# findemptiest

reset()
if libdb.findemptiest() != (3,3):
    print("test failed: findemptiest() does not return 3,3")
    print(libdb.findemptiest())
    print(libdb.getdbcoord(libdb.findemptiest()[0], libdb.findemptiest()[1]))
# addpos

libdb.addpos('test1', 3, 3) 
if libdb.getdbcoord(3,3) != ['test1']:
    print('test failed: addpos(3,3) does not add as specified')
reset()

libdb.addpos('test2',0,2)
if libdb.getdbcoord(0,2) != ['usb a to c c to c combo cable', 'test2']:
    print('test failed: addpos("test2", 2, 0) does not add as specified')
    print(libdb.getdbcoord(0,2))

reset()
if libdb.addpos('jjjj', 500, 500) != -1:
    print("test failed: addpos out of bounds positive does not return -1")
    

reset()
if libdb.addpos('jjjj', -1, -1) != -1:
    print("test failed: addpos out of bounds negative does not return -1")

# removepos

reset()
libdb.removepos('ziploc bags', 1, 5)
if libdb.getdbcoord(1,5) != []:
    print('test failed: removepos("ziploc bags", 1, 5) did not remove as specified')
    print(libdb.getdbcoord(1,5))

reset()
libdb.removepos('usb a to c c to c combo cable',0,2) 
if libdb.getdbcoord(0,2) != []:
    print('test failed: removepos("usb a to c c to c combo cable", 0, 2) did not remove as specified')
    print(libdb.getdbcoord(0,2))

reset()
if(libdb.removepos('jjjjjjj',0,2) != -1):
    print('test failed: removepos("jjjjjj",0,2) did not return -1 like it should because i have no jjjjj')

reset()
if(libdb.removepos('jjjjj',500,500)) != -1:
    print('test failed: removepos("jjjjj",500,500) did not return -1 like it should, both because of the 500,500 and the jjjjj')

reset()
if(libdb.removepos('jjjjj',-30,-30)) != -1:
    print('test failed: removepos("jjjjj",-30,-30) did not return -1 like it should, both because of the -30,-30 and the jjjjj')

# add

reset()
libdb.add("esp32")
if ( libdb.getdbcoord(0,1) != ['esp32', 'esp32', 'esp32', 'raspberry pi zero2w', 'esp32']):
    print('test failed: add("esp32") did not correctly add or did not add in right position')
    print(libdb.getdbcoord(0,1))

reset()
libdb.add('ziploc bags')
if ( libdb.getdbcoord(1,5) != ['ziploc bags', 'ziploc bags']):
    print('test failed: add("ziploc bags") did not correctly add or did not add in right position')
    print(libdb.getdbcoord(1,5))

reset()
if (libdb.add(1010101010) != -1):
    print('test failed: pass wrong type to add function did not correctly return -1')

reset()
if libdb.remove("esp32") != (0,1):
    print('test failed: libdb.remove("esp32") does not return 0,1 like it should')
if libdb.getdbcoord(0,1) != ['esp32', 'esp32', 'raspberry pi zero2w']:
    print('test failed: remove("esp32") did not correctly remove esp32')

reset()
if libdb.remove("ziploc bags") != (1,5):
    print('test failed, remove("ziploc bags" does not return 0,1 like it should)')
if libdb.getdbcoord(1,5) != []:
    print("test failed: remove('ziploc bags' does not remove ziploc bags correctly)")


# print(libdb.add(1030330))
# print(libdb.search('1030330'))

