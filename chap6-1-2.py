import tkinter
from PIL import Image, ImageTk

#drawingmap
def draw_map():
    for y in range(0, MAX_HEIGHT):
        for x in range(0, MAX_WIDTH):
            p = map_data[y][x]
            canvas.create_image(x*62+31, y*62+31, image=images[p])
    #display of brave
    canvas.create_image(brave_x*62+31, brave_y*62+31, image=images[4], tag="brave")

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
images = [ImageTk.PhotoImage(file='img6/chap6-mapfield.png'),
ImageTk.PhotoImage(file='img6/chap6-mapwall.png'),
ImageTk.PhotoImage(file='img6/chap6-mapgoal.png'),
ImageTk.PhotoImage(file='img6/chap6-mapkey.png'),
ImageTk.PhotoImage(file='img6/chap6-mapman.png')]


#mapdata
MAX_WIDTH = 10
MAX_HEIGHT = 7
map_data = [[1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 1, 2, 0, 0, 1, 3, 1],
[1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

#position of brave
brave_x = 1
brave_y = 0

draw_map()
root.mainloop()
