import tkinter
from PIL import Image, ImageTk

#window
root = tkinter.Tk()
root.title("ダンジョン")
root.minsize(840, 454)
root.option_add("*font", ["メイリオ", 14])

#canvas
canvas = tkinter.Canvas(width=620, height=434)
canvas.place(x=10, y=10)
canvas.create_rectangle(0, 0, 620, 434, fill="gray", tag="drawField")

#scan
image1 = ImageTk.PhotoImage(Image.open('img6/chap6-mapfield.png').convert('RGB')),
image2 = ImageTk.PhotoImage(Image.open('img6/chap6-mapwall.png').convert('RGB')),
image3 = ImageTk.PhotoImage(Image.open('img6/chap6-mapgoal.png').convert('RGB')),
image4 = ImageTk.PhotoImage(Image.open('img6/chap6-mapkey.png').convert('RGB')),
image5 = ImageTk.PhotoImage(Image.open('img6/chap6-mapman.png').convert('RGB')),




root.mainloop()
