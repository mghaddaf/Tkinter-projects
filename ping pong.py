import tkinter
screen = tkinter.Tk()
screen.geometry("700x500")
screen.title("Ping Pong")
Canvas1 = tkinter.Canvas(screen, width = 700, height = 500, bg = "black")
Canvas1.pack()
Canvas1.create_line(350, 0, 350, 500, fill = "White", width = 5)
Canvas1.create_oval(300, 200, 400, 300, outline= "White", width = 5)
class Player():
    def  __init__(self, startx, starty, endx, endy, color):
        self.player = Canvas1.create_rectangle(startx, starty, endx, endy, outline = color, fill = color, width = 5)
        self.velocityy = 0.1

    def move(self):
        Canvas1.move(self.player, 0, self.velocityy)
        playerpos = Canvas1.coords(self.player)
        if playerpos[1] < 0 or playerpos[1] > 390:
            self.velocityy = 0
class Ball():
    def __init__(self, width, color):
        self.ball = Canvas1.create_oval(340, 240, 360, 260, fill = color)
        self.velocityx = 0.05
        self.velocityy = 0.05
    def move(self):
        Canvas1.move(self.ball, self.velocityx, self.velocityy)
        ballpos = Canvas1.coords(self.ball)
        if ballpos[0] > 680 or ballpos[0] < 0:
            self.velocityx = self.velocityx * -1
        if ballpos[1] > 480 or ballpos[1] < 0:
            self.velocityy = self.velocityy * -1

Player1 = Player(10, 300, 20, 200, "red")
Player2 = Player(690, 300, 680, 200, "blue")
Ball1 = Ball(1, "yellow")

while True:
    Ball1.move()
    screen.update_idletasks()
    screen.update()
    Player1.move()
    Player2.move()
    screen.update_idletasks()
    screen.update()
screen.mainloop()