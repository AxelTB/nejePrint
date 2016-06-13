from PIL import Image
import tkinter as tk
from tkinter import filedialog

import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 57600)
ser.write(b"\xF6")
rep=ser.read(2);

print('Replied')
print(rep)

if rep == b'ep' :
	root = tk.Tk()
	root.withdraw()
	file_path = filedialog.askopenfilename()

	im = Image.open(file_path)

	im = im.resize((512,512), Image.ANTIALIAS)
	im = im.convert('1')


	im.save('converted.bmp')

	ser.write(b"\xFE\xFE\xFE\xFE\xFE\xFE\xFE\xFE")
	time.sleep(3)
	ser.write(open("converted.bmp","rb").read())
	time.sleep(3)

	ser.write(b"\xF3")
	time.sleep(5)

	ser.write(b"\x10")
	time.sleep(1)

	ser.write(b"\xF4")
else :
	print('Printer not connected')
