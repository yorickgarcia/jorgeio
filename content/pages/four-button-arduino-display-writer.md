title: Four Button Arduino Display Writer
date:11-26-19
category: Projects and Guides

## Intro

---

###### 🚧**Work-In-Progress**🚧

Idea spot-

Learn how to wire an 16x2 LCD display to an arduino and how you can use just a few buttons to write messages on it.

Note to self - Approach: Wire and Check, a step at a time. Same for code?

Section A -Tour and Set-up

---

These types of LCD have become a commoditiy. Just about everyone you might come across is built the same is built the same. This makes it easy for fabricators to choose whatever fits their build best at the best price. It also makes it easier for you, the inventor, to learn a single method for programming these.

##### Learning Objects:
By the end of this guide, you should understand how an LCD display works.

##### Materials

Your kit is made of eight (8) items.  

1. 1 x Ardiuno Uno or a board based on the same processor 
- 1 x long breadboard
- 1 x 16x2 character LCD
- 4 x momentary switches (Buttons)
- 1 x potentiometer
- 64,000 x Wires
    - 12 x Black
    - 8 x Red
    - 3 x Blue
    - 2 x Green
    - 1 x Yellow

![](/images/kit.png)


--- 


# Instructions:

##### Outline
1. Turn on the Backlight
2. Add Contrast Control
3. [Power to the LCD](#section)
4. Sending Bits of Signal
5. Adding a Button to Scroll Characters
6. Scrolling Backwards
7. Changing Position
8. Deleting and Clearing
9. Next Steps

#### Provide power to the breadboard
Breads have long rails running across, usually on both sides to give you several options to tap into your power source. For this project we will use 5 volts from the Arduino. Connect a red wire from the 5V slot into the + rail, and a black wire from the GND slot into the - rail.

![](/images/power.png)

#### Powering the Backlight
You will find them in two variants, 14 pins and 16 pin. The 2 extra pins provide power for the LED backlight that makes it glow this is what we will connect first.

![](/images/led-powered.png)


#### Initializing the LCD
##### Power
That was only the light, now let's provide power the the LCD display. For this we will need a few more wires.
##### Contrast
In the manufacturing process of any item, there are variation even between items on the same run. For this reason, we will also install a potentiotmetr which is just like a slider. Power up the kit again and play with the potentiometer, you should see the screen change. Dial it back to just before the blocks disappear.

#### Sending Bits
Lets send some data! These displays can receive data in two ways, by sending a single 8 bit signal or two 4-bit nibbles. 

#### 

---
#### Sources:  

- <https://www.instructables.com/id/How-to-drive-a-character-LCD-displays-using-DIP-sw/>
- <https://create.arduino.cc/projecthub/dirar/lcd-button-writer-6b94b3>  
- <https://forum.arduino.cc/index.php?topic=542871.0>  
- <https://github.com/sparkfun/SIK-Guide-Code/blob/master/SIK_Circuit_4A-LCDHelloWorld/SIK_Circuit_4A-LCDHelloWorld.ino>  
- <https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v41/circuit-4a-lcd-hello-world>  

# H1
## H2
### H3
#### H4
##### H5
###### H6

Paragraph

- listed
- items
    - nested
- last

this is here for a break
 
1. numbered
2. list
    + nested
3. three