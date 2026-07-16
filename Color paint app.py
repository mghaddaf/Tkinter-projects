import tkinter
from tkinter.colorchooser import askcolor
screen = tkinter.Tk()
screen.geometry("1000x1000")
screen.title("Paint app")
color = "Red"
penthickness = 1
oldx = None
oldy = None
eraseron = False

def draw(event):
    global oldx, oldy
    global penthickness
    pencolor = color
    penthickness = Scale1.get()
    if oldx and oldy:
        Canvas1.create_line(oldx, oldy, event.x, event.y, fill = pencolor, width = penthickness)
    oldx = event.x
    oldy = event.y

def reset(event):
    global oldx, oldy
    oldx = None
    oldy = None


def penbutton():
    eraseron = False
def brushbutton():
    pass
def colorbutton():
    global color
    color = askcolor()[1]

def eraserbutton():
    global eraseron
    eraseron = True
Button1 = tkinter.Button(screen, text = "pen", command = penbutton)
Button2 = tkinter.Button(screen, text = "brush", command = brushbutton)
Button3 = tkinter.Button(screen, text = "color", command = colorbutton)
Button4 = tkinter.Button(screen, text = "eraser", command = eraserbutton)
Scale1 = tkinter.Scale(screen, from_ = 1, to = 5)
Canvas1 = tkinter.Canvas(screen, background = "white")
Canvas1.bind("<B1-Motion>", draw)
Canvas1.bind("<ButtonRelease-1>", reset)
Button1.grid(row = 1, column = 1)
Button2.grid(row = 1, column = 2)
Button3.grid(row = 1, column = 3)
Button4.grid(row = 1, column = 4)
Scale1.grid(row = 1, column = 5)
Canvas1.grid(row = 2, column = 1, columnspan = 5)
screen.mainloop()