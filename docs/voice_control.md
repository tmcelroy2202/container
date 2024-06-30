You will see, in the demo video, that I am controlling the system by voice.

It is super convenient, and I do not think I would be willing to use the system without it, but it DEFINITELY DOES NOT work first try every single time. There are a number of cases where things are problematic, for example:

if i say "container add" it might interpret that as "container ad"
if i say "esp32" it might interpret that as "esp 32"
if i say "aux cable" it might interpret that as "ox cable"
if i say "budi cable adapter kit" it might interpret that as "booty cable adapter kit"

USUALLY, with words which are unmistakable, things will work great, but there are definitely cases where voice control has drawbacks.

My current system works via an android phone using google's speech recognition keyboard, typing into termux. The termux input is sent to a file on my server computer live, and if it ever goes more than 3 seconds without sending any input to that file, then it will try to execute the contents of the file as best as it can. This means it will look for the word container in the input, and only process that and the words after it, meaning you can talk leading up to the command input, just not after. It also allows you to say "done" to finish your command, so if you wish to continue talking after, you can use the word done to make sure your extra speech doesn't break your command. 

I have a solution to the bad voice recognition problem though - I manually replace the problem words in the code. e.g. where i say "if action == 'add'" I say "or action == 'ad'". It works fine. It's just annoying to do each time I run into a new problem. It means this solution isnt viable long term, as I am unwilling to recommend that other people do that. Im not even happy with doing it myself. 

That android phone with google speech recognition I imagine could be way better. There are any number of more intensive speech to text services which likely would not misinterpret my speech as often. Here are the common examples im aware of:
  1. Whispercpp
  2. Openai Whisper API
  3. Vosk-API

I am not using any of those though, because one of my requirements is that I need to be able to do live transcription. I cant just send a media file off for transcription. I want my voice transcribed live. i do not know when the person will start or stop talking. 

I could hack my way around this, by using hotword detection to start recording when they say a hotword, and then recording until audio levels drop below a certain threshhold for a certain amount of time. I am not sure how I would do the detection of the audio level dropping. There are any number of projects for hotword detection though, with these being the main ones im aware of:
  1. OpenWakeWord 
  2. Mycroft-precise 
  3. Snowboy 
  4. Porcupine 
  5. EfficientWord-Net 

I would love to use one of them one day to do the intialization of recording, but I do not feel that I am smart enough as of yet. I keep looking into them and having great trouble setting them up ( I AM SO VERY OPEN TO PULL REQUESTS )

For now, the google speech recognition works, is very cheap, and very decent. It does not require me to pay for an API ( e.g. google's own speech recognition API, which I think is what the phone uses. ) and works fast, and much more accurate than vosk-small, which is the best I can run on a local device upstairs ( my laptop )

Vosk I did get to work live transcribing audio, and I also got whisper.cpp small to work, but their accuracy was far worse than the google speech recognition, which I believe is purely because they are small models. I have a server downstairs with plenty of processing power, though and theoretically I could stream microphone input from the android phone down to the computer as a micrphone device and use one of the larger models with vosk or whispercpp. Theoretically. I have not looked very far into this, but again, I AM SO OPEN TO PULL REQUESTS. 

In a perfect world, I would package the speech recognition software WITH this software, or atleast avoid needing a person to setup a secondary server device / server tool for this program. 
