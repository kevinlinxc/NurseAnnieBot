# NurseAnnieBot
A Python script that plays the "Nurse Annie" game made by Boxbox, using OpenCV + Numpy to detect pixel color and win32com to send keyboard input.

Boxbox is a streamer on the platform Twitch.tv, and for his girlfriend's birthday he made her a fun GameMaker Studio 2 game.
Here is a bot that plays the game almost as fast as possible. 

This is my first ever python project so the code is likely not optimized and in general, I'm not sure what I'm doing.


Steps to reproduce on Windows:
1. Install Python and OpenCV, and set up their environmental variables properly
2. Install PIP and use pip to install numpy (I think) using powershell (I tried git bash but it didn't have a console, which is not necessary anyway but for testing it was)
3. Install SparkoCam so that you have a "webcam" that the python script can see. When you need to set up the webcam, you pick Desktop under the device tab of SparkoCam and drag it onto the Nurse Annie window
4. Clone this repository, cd into it, and run ```python annie.py```. You'll get python not recognized error if you didn't install it properly or set up its environmental properties properly
5. Make sure you click on the Nurse Annie window after the python windows open.
6. If it only goes 1-6 times and then stops, and the color square displays a maroon, try moving the Nurse Annie screen around left and right to make the webcam register properly. 
7. Other troubleshooting: sometimes the Nurse Annie game will crash. Any time it crashes or aborts, you have to re pick a window in SparkoCam. You can end the script by typing Control + C in powershell. 

Possible improvements:
I might try getting rid of the console output as that was just for testing, and I can also reduce the time between keyboard presses  until it is optimized. 
