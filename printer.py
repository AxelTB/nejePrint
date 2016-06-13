from PIL import Image
import tkinter as tk
from tkinter import filedialog

import serial
import time
from easygui import *

ser = serial.Serial('/dev/ttyUSB0', 57600)
ser.write(b"\xF6")
rep=ser.read(2);

reply='bho'
if rep == b'ep' :
	choices = ["Convert Image","Load Converted Image","Preview","Print","Set Burning Time","Send Laser Home", "Reset Printer","Pause","Quit"]

	while (reply != 'Quit'):
		reply = choicebox("What would you like to do?", choices=choices)

		if reply == choices[0] :
			root = tk.Tk()
			root.withdraw()
			#file_path = filedialog.askopenfilename()
			file_path = fileopenbox()
			im = Image.open(file_path)

			im = im.resize((512,512), Image.NEAREST)
			im = im.convert('1').transpose(Image.FLIP_TOP_BOTTOM)


			im.save('converted.bmp')
			msgbox("Check converted.bmp for a (Vertically flipped) preview")
		elif reply == choices[1]:
				print('Sending converted.bmp to machine, please wait')
				ser.write(b"\xFE\xFE\xFE\xFE\xFE\xFE\xFE\xFE")
				time.sleep(3)
				print('.')
				ser.write(open("converted.bmp","rb").read())
				print('.')
				time.sleep(3)
				print('Done!')

				ser.write(b"\xF3")
		elif reply == choices[2]:
			ser.write(b"\xF4")
		elif reply == choices[3]:
			ser.write(b"\xF1")
		elif reply == choices[4]:
			burnTime=int(input("Enter burning time (1-240) : "))
		#ser.write(b"\x10")
			ser.write(bytes([burnTime]))
		elif reply == choices[5]:
			ser.write(b"\xF3")
		elif reply == choices[6]:
			ser.write(b"\xF9")
		elif reply == choices[7]:
			ser.write(b"\xF2")

else :
	print('Printer not connected')
