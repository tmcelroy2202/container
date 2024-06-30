If you wish to setup container for use in your home, here are the required materials:
  * Android Phone that can run termux
  * A device with network connectivity that can run python scripts ( in my case, this is a old laptop running linux mint. )
  * LED strip
  * WLED controller ( in my case, an ESP32 )
  * Breadboard jumper wires
  * Power cables for all relevant devices 
  * whatever storage medium you choose.

if you do not own any of those things, here are what I have:
  * Android Phone that can run termux: LG K20 V
    * link example: https://www.ebay.com/itm/335304613201
  * the laptop i have: Lenovo Ideapad 100-15IBD Laptop
    * link example: https://www.ebay.com/itm/235582941409
    * I DO NOT RECOMMEND YOU BUY THIS LAPTOP IT IS TERRIBLE
    * instead i would recommend any of the following:
    * any laptop with an i5 above gen 3 you can find for 40$ or under
    * lenovo x220
      * link example: https://www.ebay.com/itm/266856990048   
    * raspberry pi zero2w with a little 7in display on xfce with a bluetooth keyboard 
      * link example pi: https://www.adafruit.com/product/5291
      * link example 7in display: https://www.aliexpress.us/item/3256806784001385.html
      * link example bluetooth keyboard: https://www.aliexpress.us/item/3256805485944029.html
    * if anyone reading this has suggestions for other devices that are cheaper and could do this job, please open a pull request.
  * LED Strip: WS2812B LED Strip 16.4FT
    * link example: https://www.amazon.com/BTF-LIGHTING-WS2812B1M144LB30-BTF-LIGHTING-WS2812B-IC-RGB-5050SMD-Pure-Gold-Individual-Addressable-LED-Strip-High-Quality-3-28FT-144LED-144LED-m-Flexible-Full-Color-IP30-DC5V-For-DIY-Chasing-Color-Project-No-Adapter-or-Controller/dp/B01CDTEJBG/
  * WLED Controller: ESP32
    * link example: https://www.amazon.com/DORHEA-Development-Microcontroller-NodeMCU-32S-ESP-WROOM-32/dp/B086MJGFVV/
      * note: this is a 3 pack and we are only using 1 for this project
      * there are plenty of cool uses for an ESP32 though and you may have one in the future.
      * or you can send me your extras <3<3<3
      * a 3 pack seems to be the most cost effective reasonable way to buy them though. 3 pack is 16$ and 1 of them is 8$.
      * i got the microusb kind but i bet the usbc kind would be nicer, and they cost 22 cents more, so the price difference is negligible.
      * im just putting the microusb one because i have never used the usbc one. ( if anyone uses the usbc one and it works, let me know, and i will add it as a recommended option )
  * Breadboard jumper wires: any that include male to female wires.
      * link example: https://www.amazon.com/Elegoo-EL-CP-004-Multicolored-Breadboard-arduino/dp/B01EV70C78/
      * you get way more than you need (120pcs and we only need 3) but i dont see a cheaper way to buy just 3. its wires. You might need them again. 
  * Power Cables for all relevant devices:
      * for my laptop, this is the lenovo power cable that came with the laptop. 
        * if you did not go with my laptop, then here are the relevant things:
          * for a raspberry pi zero2w, it would be a microusb cable
            * link example: https://www.amazon.com/RAMPOW-Android-Charging-Braided-Samsung/dp/B01GJC4YMC/
          * for a t480 it would be a usbc cable 
            * link example: https://www.ebay.com/itm/164330933785
              * you probably already got one of these with the laptop though
          * for the android phone i linked, it would be another microusb cable
            * link example: https://www.amazon.com/RAMPOW-Android-Charging-Braided-Samsung/dp/B01GJC4YMC/
            * for most other android phones, it would be usbc.
              * link example: https://www.ebay.com/itm/225378286875
* storage mediums:
  * card catalog:
    * link example: https://www.amazon.com/KIRIGEN-Organizer-Desktop-Storage-Organization/dp/B0BGD9TM9Z/

  * 36 Drawer Stackable Storage Cabinet by irisusa: 
    link example: https://www.irisusainc.com/collections/utility-bins/products/36-drawer-stackable-storage-cabinet-for-hardware-parts-crafts

  * please know that these are NOT the best options in existance. They are what I got, and I did some significant amount of research beforehand, but if anyone reads this and does their own research and finds something better, please let me know. 


# Actual Setup

First thing you are going to want to do, is install wled on the esp32.

I strongly recommend watching this video for that: 

https://www.youtube.com/watch?v=exAWzMfmwQ8

Here's the relevant info about MY setup, for if you are following along directly with what im doing:
* ESP32 is connected to LEDs via breadboard jumper wires 
* I have no external power supply, all power is supplied via the microusb port on the esp32 
  * power limit in the wled app is set to 1000mah because of this 

Once you have wled installed and the lights connected to wled, you are going to want to attach the led lights to your container. You can do this by either attaching LEDs along the x and y axis OR by attaching LEDs along each row. 

Once you have the LEDs attached, you are going to need to go into the wled app, and create segments. These segments should be the individual bits you want to be able to highlight, so for example, in my card catalog, every drawer has a segment. In my grid, every x coordinate and every y coordinate has a segment. 

As you do this, you will notice that there are segments that you do not need to light up, for example, the bits inbetween a row or column. That's fine. Just make a mental note of them for later. Also, when you finish, do not cut off the excess LED strip, because you may want to continue using it later. I would just put it on top of the container, or mount it to the side of the container. 

Once you have the LEDs setup how you want them, there are 2 options:
1. If i have finished the setup environment script, you would just use those segment IDs as 'skipseg'
2. If I have not finished the setup environment script, or if you prefer to do this yourself, then go to ledcontrol.py and do the following:
  * if you have a system that relies on a grid to show where things are, go to the grid function in ledcontrol and edit the logic to be appropriate for your system. When trying to understand how it works, remember that it was written for my system, and look at pictures of my system. If you need help with this, make a github issue with pictures of your system, and explanations of what you are struggling with.
  * If you have a system that relies on highlighting the specific drawer, instead of highlighting an x and y coordinate, then go to the highlight function and setup the logic to work for your system. Mine looks super weird because my LEDs snaked around my card catalog, so every other row was reversed. I got around this with a ton of if statements. You may have a sleeker solution, but this has worked for me. If you need help with adapting this for your system, make a github issue with pictures of your system, and explanations of what you are struggling with 
  * go to the changeid function and change the ip in there to be the IP of your wled instance. Do the same in the turnalldark and turnallwhite functions. I know this is annoying but it should be a non issue once i get the setup environment script done. 

Once the LEDs are setup, run main.py, and leave that open on the python controller device

Open inputs.txt and try to give an example input ( e.g. container add house ) to see if it works properly.

If things are working properly, then get out your android phone, and install termux on it. Preferably termux should be installed from F-Droid.

Open termux up, and ssh into the device running the python script. You then want to cd to the directory you have this repository in, and run ./myscript.sh

Now, go to the google speech recognition keyboard, and try to give some input! ( e.g.  say aloud: container add house )

If all went well, you should now have a working setup !

If you wish to understand more about how things work, Have a read through the rest of the contents of this folder ( docs )
