from PIL import Image
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

im = Image.open(file_path)

im = im.resize((512,512), Image.ANTIALIAS)
im = im.convert('1')


im.save('converted.bmp')
