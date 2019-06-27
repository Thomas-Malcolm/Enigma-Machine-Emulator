# Enigma-Machine-Emulator
Simple Python recreation of an Enigma machine based on the German Navy's 1934 M3 model

This was my first ever personal project completed independent of University courses, completed sometime around March 2019. I've left it unmodified, errors and all, for two reasons:

1. So I can look back in the future and laugh at my terrible code, and ultimately learn from all the beginner mistakes I've made
2. To show my development as a programmer over time

## Requirements
Dependencies:
- tkinter

File format:
All the files have to be in the same directory, including the rotors.txt file

## Basic Use

To use the emulator, run the enigma_gui.py file. With the window open it will encipher the keys you type, and print them down the bottom. Similarly, the emulator can be used to decipher enigma codes, assuming you know the settings used to encode

The three rotors can be swapped out for each other, just like the ones used during WW2. The starting letter for each rotor can be chosen individually, and there are a set of three basic reflectors given to be chosen from. 

To modify the switchboard, open it using the button. Click on the first letter you want to pair, and then the second letter you click on will be paired with the first. To reset the plugboard, use the button at the bottom. The changes will take effect whether you click the Quit button down bottom or close with the default X up top right. 

The ETW rotor can't be changed. To add more rotors/reflectors to be used, modify the rotors.txt file according to the format:
  name : letter_order, turnover_position
  
When you want to reset the whole machine, the reset button in the main window will do so.

## Programming Practices Used
- Introductory GUI
- OOP design
- Method commenting
- Multiple file management
- File I/O
- Error raising

## Lessons Learned

There are some glaringly obvious problems with the code, and probably a lot more I'll realise as I gain more experience over time. As such, here is list of some of the problems I identified as of uploading (27/6/19):

- The enigma_gui.py file is horribly laid out. I didn't know about using classes to organise GUI's at the time - there's not even a main file to run it all, just a few lines at the bottom. As a result there are global variables used all throughout, and a lot of passing variables through each function pointlessly. 
- There's a lot of code that could be just put into a for loop, or put into a function. For example, resetting the on/off lights when resetting to default.
- While I haven't figured it out yet, I'm sure there's a more efficient way to handle the enciphering function - at the moment it passes through a function nine times just to encipher a single letter
- A list of tuples would have been a better way to handle the reverse rotor position, rather than looping over the current letter order of a rotor and generating an entirely new dictionary
- Comments, while extremely important, can become cumbersome if overused and even begin to harm the quality of the code. From looking at other people's code it seems commenting as extreme as I used in enigma_logic.py and rotor_class.py may not always be necessarily. Ironically however, the lack of commenting in enigma_gui.py is an example of what happens when not enough commenting is used. There's definitely a happy medium in the middle, and I guess it's largely dependent on what the code is being used for, but in my future projects I think I'll try to limit myself to shorter descriptions

## Summary

I think I'm unlikely to come back and change this program around much, partly because of the two reasons I gave at the start, and partly because I want to move onto newer projects that account for the errors I made here. As my first independent project I'm proud of it regardless, and enjoyed being able to emulate the machine that provided the motivation for the start of computer engineering.
