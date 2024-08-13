old system worked like this:
[ [ item one, two, and 3 ], [item four, five, and six], ['etc']]
that could be 3 rows, or 1 row, or whatever, there was no seperation between rows

so i would like to rework my system to work like this

[
  [['r1 item 1 box 1', 'r1 item 2 box 1'], ['r1 item 3 box 2']]
  [['r2 item 4 box 1', 'r2 item 4 box 1'], ['r2 item 6 box 2']]
  [['r3 item 7 box 1', 'r3 item 8 box 1'], ['r3 item 9 box 2']]
  [['r4 item 10 box 1', 'r4 item 11 box 1'], ['r4 item 12 box 2']]
  [['r5 item 13 box 1', 'r5 item 14 box 1'], ['r5 item 15 box 2']]
]

this would make the grid system easier to interact with, and bring me great joy.

in the old system, my led controller would be fed info purely via print statements in the databased file
so like this

databased prints out (2,3) to show there is an item at x=2 y=3, and then led controller lights upt that spot

in v2, i would like for the led controller to be directly called, via a function, in databased, so that i have more freedom on configuration without trying to use string slicing to approximate passing arguments, like i have been doing.

I believe I will still keep the bridge system, but I will make it do significantly less it will purely take content from balls.txt and call databased on that content 

this does mean databased will become a much larger file, and maybe that should be taken into consideration. I might make a bunch of abstractions. I wanted to write a library version of databased, so that might happen.
