# container


container is a tool for interaction with my storage system.

It is built around a card catalog and one of those plastic bin organizers.

[[/images/pic.jpg]]

demo video:

container uses a voice control system to allow you to interact with and build a database of items inside your storage system. It allows you to search your database, and have LED lights show where that item is in real life. It also minimizes how much you have to think about it, by making it the default way you interact with your system. It was designed around the reality that if a system was at all annoying, I would never use it. If I had to remember to add something to my database after putting it in a drawer, I would just never do that. It would be too much work. container gets around this by managing your storage FOR you. Instead of you deciding where to put something, and logging where you put it, you just tell container you want to add something, and then container tells you where to put it, and automatically logs that you put it there. 

container has a few core components:
  * an android device which runs the google speech keyboard to allow for voice input. SSHs into the server and runs a script on the server to allow it to take that voice input and write it to a file ( inputs.txt )
  * a server device, which parses all your voice input, hosts / interacts with the databases, and does the sending of requests to the wled instance
  * a wled instance connected to an led strip on your local network


Requirements:
  * Android Phone
  * A device with network connectivity that can run python scripts
  * LED strip
  * WLED controller ( in my case, an ESP32 )
  * Breadboard jumper wires
  * Power cables for all relevant devices 
  * whatever storage medium you choose.
  
For a setup tutorial, see setup.md


Similar projects:
  * https://www.instructables.com/StorageBot-voice-controlled-robotic-parts-finder/
  * https://orbitingprojects.blogspot.com/2012/05/light-it-up-component-organizer.html
  * https://www.youtube.com/watch?v=7C4i-2IqSS4
  * https://www.youtube.com/watch?v=7WAhquGQq3o
  my thoughts on these can be found here: https://notes.tommyhost.ing/Self/Storage-System/Problem-and-Idea#idea
