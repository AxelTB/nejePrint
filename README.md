Since I didn't figure out how to make Neje Software work on wine.

commands.txt is kind of a retro-engineering log.
It seems to just save a bitmap somewhere and then prints it.

# nejePrint
Linux script for Neje Laser engraver

Usage:
nejePrint.sh SERIALDEVICE IMAGE [BURNINGTIME]

Image must be 520x520 BMP 1 bit color depth (See mono.bmp)



# python3 Neje Printer
Python 3 based Neje Printer script.

If the printer is running just pause before running the script.

Does:
* Image Conversion (Not square images will be stretched)
* Image Load
* Burning Time Setup (With working printer if software already loaded)
* Preview and print (If you really cannot press the button)
* Go home, Reset, Pause

Does not:
* Converted image Preview
* Printed trace view
* Manual Control



Requires:
* Python3
* Pyserial
* Python EasyGUI


More detailed instructions:
http://axengineering.wordpress.com/2016/06/14/neje-laser-engraver-on-linux/
