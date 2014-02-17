CAPPA
=====

Chaise Active Pour Personnes Agées

This is a science project for Thierry Jones, student in Ottawa, Canada. The concept is as follows:

1) Senior person sits on chair
2) They press button 1 to activate an exercise video (which is adapted to them, chair exercise video)
3) Once complete, they press a second button which activates the infromation download from a Heart Reate Monitor and publishes the exercise information to the web

Elements of CAPPA

1) Hardware
- Raspberri Pi
- Breadboard
- Peripherals (USB WiFi dongle, Mouse, Keyboard)
- Buttons, and wires for breadboard

2) Software
- Program 1: Python program that listens for button 1 press, which initiates OMX Player and plays the exercise file
- Program 2: Python program that listens for button 2 press, which initiates exercise file parse/write/post to web
- Program 3: Python program that parses XML exercise file, captures key information, and posts an HMTL file to the web

