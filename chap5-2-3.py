import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk()
root.title("王様をいっぱい表示")
root.minsize(1600, 800)

canvas = tkinter.Canvas(root, width=1600, height=800)
canvas.pack()
img = ImageTk.PhotoImage(Image.open('img4/chap4-1-1.png').convert('RGB'))

#座標用変数
x = 100
y = 180

while x < 1600 and y < 480:
    canvas.create_image(x, y, image=img)
    x = x + 200
    y = y + 50
root.mainloop()