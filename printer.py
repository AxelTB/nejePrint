from PIL import Image
import tkinter as tk
from tkinter import filedialog

import serial
import time
from easygui import *

ser = serial.Serial('/dev/ttyUSB0', 57600)
ser.write(b"\xF6")
rep=ser.read(2);

print('Replied')
reply='bho'
if rep == b'ep' :
	choices = ["Load Image","Preview","Print","Set Burning Time","Quit"]

	while (reply != 'Quit'):
		reply = choicebox("What would you like to do?", choices=choices)

		if reply == choices[0] :
			root = tk.Tk()
			root.withdraw()
			file_path = filedialog.askopenfilename()

			im = Image.open(file_path)

			im = im.resize((512,512), Image.NEAREST)
			im = im.convert('1').transpose(Image.FLIP_TOP_BOTTOM)


			im.save('converted.bmp')

			ser.write(b"\xFE\xFE\xFE\xFE\xFE\xFE\xFE\xFE")
			time.sleep(3)
			ser.write(open("converted.bmp","rb").read())
			time.sleep(3)

			ser.write(b"\xF3")
		elif reply == choices[1]:
			ser.write(b"\xF4")
		elif reply == choices[2]:
			ser.write(b"\xF1")
		elif reply == choices[3]:
			burnTime=int(input("Enter burning time (1-200) : "))
		#ser.write(b"\x10")
			ser.write(bytes([burnTime]))


else :
	print('Printer not connected')
