Since I didn't figure out how to make Neje Software work on wine.

commands.txt is kind of a retro-engineering log.
It seems to just save a bitmap somewhere and then prints it.

# nejePrint
Linux script for Neje Laser engraver.
Use it just to check for compatibility as follow:
* Connect the printer to the pc
* Use dmesg to check on which port is the printer (Usually /dev/ttyUSB0)
* ./nejePrint.sh /dev/ttyUSB0 mono.bmp
* Press button on printer when program say so
* If it works you should install the python version

Usage:
nejePrint.sh SERIALDEVICE IMAGE [BURNINGTIME]

Parameters:
  SERIALDEVICE (Usually /dev/ttyUSB0, running dmesg after you connect the printer shuold tell you something more)
  IMAGE Image to be printed must be 512x512 BMP 1 bit color depth and vertically flipped (See mono.bmp)
  BURNINGTIME 1-240 (Not Implemented)



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
