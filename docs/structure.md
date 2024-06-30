Here is the flow of how you send an action to the system:
1. You go on the android phone and hit the microphone button, which starts the google speech to text keyboard listening in the backgroudn
2. You start talking, and as you talk your speech is transcribed as text into termux, which sends all the text to a file on the computer 
3. The computer checks that file once every second, and if it has been recently updated, it waits until there have been 3 seconds or more since the last update, and then it reads the file.
4. The computer extrapolates what your command is ( e.g. do you want to add? or remove ? and what are you adding?? ) and resets that inputs file to blank. 
5. The computer decides which container system to put it in. It does this by checking if either of them have the exact item you're trying to put in, and if neither of them do, it just goes with the one with the emptiest location. 
6. The computer uses the relevant library ( libdb for the transparent plastic containers, and libdbcc for the card catalog ) to complete your action.
7. libdb or libdbcc write what needs to be written to the database file ( db.txt or dbcc.txt ) ( a version of the database with that bit removed or with a new thing added to it ) and returns the coordinates it just did stuff to 
8. The computer passes the coordinates provided by the library to the ledcontrol script, along with the relevant color ( if adding, green, if removing red, etc ). 
9. The ledcontrol script builds a payload and sends it to the wled instance. 
10. The main script loops over again, and starts checking for new commands. 
