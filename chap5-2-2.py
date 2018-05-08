import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk()
root.title("王様をいっぱい表示")
root.minsize(1600, 800)

canvas = tkinter.Canvas(root, width=1600, height=800)
canvas.pack()
img = ImageTk.PhotoImage(Image.open('img4/chap4-1-1.png').convert('RGB'))

for i in range(7):
    canvas.create_image(100 + i * 200, 180 + i * 50, image=img)
root.mainloop()





